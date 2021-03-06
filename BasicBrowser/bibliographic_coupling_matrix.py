import django, os, sys, time, resource, re, gc, shutil
from multiprocess import Pool
from functools import partial
import numpy as np
from functools import partial
from scipy.sparse import coo_matrix, csr_matrix, find, tril
import networkx as nx

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BasicBrowser.settings")
django.setup()

from scoping.models import *

def process_citation(c):
    x = x

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

###################################
# function, to be done in parallel,
# which pull citations from docs,
# adds them to db,
# and links citations and docs
def bib_couple(i, bc_matrix, rev_m_dict):
    bc = BibCouple(
        doc1_id=rev_m_dict[bc_matrix[1][i]],
        doc2_id=rev_m_dict[bc_matrix[0][i]],
        cocites=bc_matrix[2][i],
    )
    return bc

def populate_matrix(cdo,m_dict,n_dict):
    django.db.connections.close_all()
    i = m_dict[cdo.doc.pk]
    j = n_dict[cdo.citation.pk]
    S[i,j] = 1

def print_top_words(t):
    topic_idx = t
    topic = enumerate(nmf.components_[t])
    topic = nmf.components_[t]
    print("Topic #%d:" % topic_idx)
    print("Score: {}".format(topic.sum()))
    print()
    print("\n".join([Doc.objects.get(pk=rev_m_dict[i]).title
    for i in topic.argsort()[:-10 - 1:-1]]))
    print()

def print_top_topics(t):
    topic_idx = t

    topic = doctops[t]
    print("Topic #%d:" % topic_idx)
    print("\n".join([str(i) for i in topic.argsort()[:-10 - 1:-1]]))
    print()


def main():
    qid = sys.argv[1]

    for cdo in CDO.objects.values('doc','citation').distinct()[:5]:
        print(cdo)
        #CDO.objects.filter(pk__in=CDO.objects.filter(doc=).values_list('id', flat=True)[1:]).delete()

    sys.exit()
    #time.sleep(14400)

    q = Query.objects.get(pk=qid)

    mdocs = Doc.objects.filter(
        query=q,
        wosarticle__cr__isnull=False
    )

    cdos = CDO.objects.filter(
        doc__query=q
    )

    # cdos = CDO.objects.filter(
    #     doc__in=mdocs.values_list('UT',flat=True)
    # )


    m = mdocs.count()
    m_dict = dict(zip(
        list(mdocs.values_list('UT',flat=True)),
        list(range(m))
    ))


    rev_m_dict = dict(zip(
        list(range(m)),
        list(mdocs.values_list('UT',flat=True))
    ))

    del mdocs


    n = Citation.objects.count()
    n_dict = dict(zip(
        list(Citation.objects.all().values_list('id',flat=True)),
        list(range(n))
    ))

    print("ROWIDS")
    row_ids = list(cdos.values_list('doc__UT',flat=True))
    rows = np.array([m_dict[x] for x in row_ids])

    print("colids")
    col_ids = list(cdos.values_list('citation__id',flat=True))
    cols = np.array([n_dict[x] for x in col_ids])

    print("data")
    data = np.array([1]*cdos.count())

    print("matrix")
    Scoo = coo_matrix((data, (rows,cols)),shape=(m,n))

    del cdos
    del row_ids
    del rows
    del col_ids
    del cols
    del data
    del n_dict

    gc.collect()


    S = Scoo.tocsr()
    del Scoo
    gc.collect()

    print("transpose")
    St = S.transpose()

    print("multiply")
    Cmat = S*St

    del S
    del St
    gc.collect()

    ltri = tril(Cmat,k=-1)


    G = nx.from_scipy_sparse_matrix(ltri)

    cnode = m_dict[Doc.objects.get(UT='WOS:000297683800015').UT]

    paths = nx.single_source_shortest_path(G,cnode)

    deg = nx.degree_centrality(G)
    ecent = nx.eigenvector_centrality(G)

    x = nx.core_number(G)

    for i in range(G.number_of_nodes()):
        d = Doc.objects.get(pk=rev_m_dict[i])
        d.k = x[i]
        d.degree = deg[i]
        d.eigen_cent = ecent[i]
        try:
            d.distance = len(paths[i])
        except:
            pass
        d.save()

    del x
    del G
    del deg
    del ecent
    gc.collect()

    bcmatrix = find(tril(Cmat,k=-1))

    N = len(bcmatrix[0])

    bcrange = list(range(N))
    print(N)

    chunk_size = 5000

    BibCouple.objects.all().delete()

    for i in range(N//chunk_size+1):

        f = i*chunk_size
        print(f)
        l = (i+1)*chunk_size-1
        if l > N:
            l = N-1

        bcs = []
        chunk = bcrange[f:l]
        pool = Pool(processes=5)
        bcs.append(pool.map(partial(bib_couple,
                        bc_matrix = bcmatrix,
                        rev_m_dict=rev_m_dict),chunk))
        pool.terminate()
        gc.collect()

        django.db.connections.close_all()
        bcs = flatten(bcs)
        BibCouple.objects.bulk_create(bcs)


if __name__ == '__main__':
    t0 = time.time()
    main()
    totalTime = time.time() - t0

    tm = int(totalTime//60)
    ts = round(totalTime-(tm*60),2)

    print("done! total time: " + str(tm) + " minutes and " + str(ts) + " seconds")
    print("a maximum of " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000) + " MB was used")
