from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
from utils.utils import *
from scoping.utils import utils
import os
from django.db import connection, transaction
from psycopg2.extras import *
import time
import subprocess
from django.conf import settings
#import scoping


@shared_task
def add(x, y):
    return x + y

# @shared_task
# def query_doc_category(qid,cid):
#     docs = Doc.objects.filter(query=)

@shared_task
def handle_update_tag(tid):
    t = Tag.objects.get(pk=tid)
    t.update_tag()
    return t.id

@shared_task
def order_dos(dos):
    for i,d in enumerate(dos):
        do = DocOwnership.objects.get(pk=d)
        do.order=i
        do.save()

@shared_task
def update_projs(pids,add_docprojects=False):

    projs = Project.objects.filter(id__in=pids)

    for p in projs:
        p.queries = p.query_set.distinct().count()
        p.docs = p.docproject_set.count()
        p.reldocs = p.docproject_set.filter(relevant=1).count()
        if add_docprojects:
            docs = set(list(Doc.objects.filter(query__project=p).values_list('pk',flat=True)))
            dps = [(d,p.id,0) for d in docs]
            cursor = connection.cursor()
            p.doc_set.clear()
            execute_values(
                cursor,
                "INSERT INTO scoping_docproject (doc_id, project_id, relevant) VALUES %s",
                dps
            )
        p.tms = len(set(list(RunStats.objects.filter(query__project=p).values_list('pk',flat=True))))
        p.save()
    return

@shared_task
def update_techs(pid):
    technologies = Category.objects.filter(project_id=pid)
    for t in technologies:
        t.queries = t.query_set.count()
        tdocs = Doc.objects.filter(category=t).values_list('id',flat=True)
        itdocs = Doc.objects.filter(query__category=t,query__type="default").values_list('id',flat=True)
        t.docs = len(set(tdocs).intersection(itdocs))
        t.nqs = t.queries
        t.ndocs = t.docs
        t.save()
    return

@shared_task
def upload_docs(qid, update):
    print(upload_docs.request.id)
    from celery.task.control import  inspect
    i = inspect()
    s = i.reserved()
    a = i.active()
    list(flatten(list(a.values()) + list(s.values())))
    for t in flatten(list(a.values()) + list(s.values())):
        if "upload_docs" in t["name"]:
            if eval(t['args'])[0] == qid:
                if str(t['id']) != str(upload_docs.request.id):
                    print("already running!")
                    return qid
    q = Query.objects.get(pk=qid)
    q.doc_set.clear()
    q.upload_log = ""
    q.save()

    title = str(q.id)

    if q.query_file.name is '':
        fname = settings.QUERY_DIR+title+"/results.txt"
    else:
        fname = q.query_file.path

    print(q.title)

    if ".xml" in q.query_file.name.lower():
        r_count = utils.read_xml(q,update)

    elif ".RIS" in q.query_file.name or ".ris" in q.query_file.name:
        r_count = read_ris(q,update)

    elif q.database =="WoS":
        print("WoS")
        with open(fname, encoding="utf-8") as res:
            if q.wos_db is not None and q.wos_db is not '':
                from django.db import connection
                connection.close()
                r_count = read_wos(res, q, update, deduplicate=True)
            else:
                r_count = read_wos(res, q, update)

    else:
        print("Scopus")
        if q.query_file.name is '':
            fname = fname.replace('results','s_results')
        with open(fname, encoding="utf-8") as res:
            r_count = read_scopus(res, q, update)

    print(r_count)
    django.db.connections.close_all()
    q.r_count = r_count
    q.save()

    t = Tag(
        title="all",
        text="all",
        query=q
    )
    t.save()
    for d in q.doc_set.all().iterator():
        d.tag.add(t)

    t.update_tag()


    return(q.id)

@shared_task
def download_metacodes(pid):
    return

@shared_task
def do_query(qid, background=True):
    q = Query.objects.get(pk=qid)
    q.doc_set.clear()
    # Do internal queries
    if q.database=="intern":
        args = q.text.split(" ")
        # Original one for combining qs
        if "manually uploaded" in q.text:
            print("manually uploaded")
        elif args[1].strip() in ["AND", "OR", "NOT"]:
            q.queries.add(Query.objects.get(pk=args[0]))
            q.queries.add(Query.objects.get(pk=args[2]))
            q1 = set(Doc.objects.filter(query=args[0]).values_list('id',flat=True))
            op = args[1]
            q2 = set(Doc.objects.filter(query=args[2]).values_list('id',flat=True))
            if op =="AND":
                ids = q1 & q2
            elif op =="OR":
                ids = q1 | q2
            elif op == "NOT":
                ids = q1 - q2
            combine = Doc.objects.filter(id__in=ids)
        else:
            # more complicated filters
            if args[0].strip()=="*":
                q1 = Doc.objects.all()
                q1ids = None
                cids = q1ids
            else:
                q1 = Doc.objects.filter(query=args[0])
                q.queries.add(pk=args[0])
                q1ids = q1.values_list('id',flat=True)
                cids = q1ids
            for a in range(1,len(args)):
                parts = args[a].split(":")
                print(parts)
                # Deal WITH tech filters
                if parts[0] == "TECH":
                    tech, tdocs, tobj = get_tech_docs(parts[1])
                    tids = tdocs.values_list('id',flat=True)
                    if q1ids is not None:
                        cids = list(set(q1ids).intersection(set(tids)))
                    else:
                        cids = tids
                    q1ids = cids
                    combine = Doc.objects.filter(pk__in=cids)
                # Deal with relevance filters
                if parts[0] == "IS":
                    if parts[1] == "RELEVANT":
                        combine = Doc.objects.filter(
                            pk__in=cids,
                            docownership__relevant=1
                        ) | Doc.objects.filter(
                            pk__in=cids,
                            category__isnull=False
                        )
                    if parts[1] == "TRELEVANT":
                        combine = Doc.objects.filter(
                            pk__in=cids,
                            docownership__relevant=1,
                            docownership__query__category=tobj
                        ) | Doc.objects.filter(
                            pk__in=cids,
                            category=tobj
                        )

        t = Tag(
            title="all",
            text="all",
            query=q
        )
        t.save()
        for d in combine.distinct('id'):
            d.query.add(q)
            d.tag.add(t)
        q.r_count = len(combine.distinct('id'))
        q.save()

        t.update_tag()

    else:
        # write the query into a text file
        fname = q.txtfile()
        with open(fname,encoding='utf-8',mode="w") as qfile:
            qfile.write(q.text.encode("utf-8").decode("utf-8"))

        time.sleep(1)

        args = [
            "/home/galm/software/django/tmv/venv/bin/python3",
            "/home/galm/software/scrapewos/bin/scrapeQuery.py",
            "-s",
            q.database
        ]

        if q.creator.username in ["galm","khat","hilj","lamw","minj"]:
            args += ["-lim", "2000000"]
        if q.credentials:
            args += [
                "-cred_uname",q.creator.profile.cred_uname,
                "-cred_pwd", q.creator.profile.cred_pwd,
                "-cred_org", q.creator.profile.cred_org,
                "-credentials", "True"
            ]

        if q.collections:
            args += [
                "-collections", q.collections
            ]

        if q.wos_db:
            args += [
                "-wos_db", q.wos_db
            ]

        args+=[fname]

        print(args)

        print(" ".join(args))

        # run "scrapeQuery.py" on the text file in the background
        if background:
            subprocess.Popen(args)
        else:
            subprocess.call(args)

    return qid
