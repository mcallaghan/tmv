from django.conf.urls import url

from . import views

app_name = 'scoping'

urlpatterns = [
    #### Index pages / query set-up (user input)
    url(r'^$', views.index, name='index'),
    url(r'^snowball$', views.snowball, name='snowball'),
    #### Query processing
    url(r'^start_snowballing$', views.start_snowballing, name='start_snowballing'),
    url(r'^doquery$', views.doquery, name='doquery'),
    url(r'^do_snowballing/(?P<qid>[0-9]+)/(?P<q2id>[0-9]+)$', views.do_snowballing, name='do_snowballing'),
    url(r'^dodocadd$', views.dodocadd, name='dodocadd'),
    url(r'^querying/(?P<qid>[0-9]+)/(?P<substep>[0-9]+)/(?P<docadded>[0-9]+)/(?P<q2id>[0-9]+)$', views.querying, name='querying'),
    url(r'^querying/(?P<qid>[0-9]+)/(?P<substep>[0-9]+)/(?P<docadded>[0-9]+)/$', views.querying, name='querying'),
    url(r'^querying/(?P<qid>[0-9]+)/$', views.querying, name='querying'),
    url(r'^snowball_progress/(?P<sbs>[0-9]+)/$', views.snowball_progress, name='snowball_progress'),
    #### Manage Query
    url(r'^query/(?P<qid>[0-9]+)/$', views.query, name='query'),
    #### Manage SBS
    url(r'^sbs_allocateDocsToUser/(?P<qid>[0-9]+)/(?P<q2id>[0-9]+)$', views.sbs_allocateDocsToUser, name='sbs_allocateDocsToUser'),
    url(r'^sbs_setAllQDocsToIrrelevant/(?P<qid>[0-9]+)/(?P<q2id>[0-9]+)/(?P<sbsid>[0-9]+)$', views.sbs_setAllQDocsToIrrelevant, name='sbs_setAllQDocsToIrrelevant'),
    url(r'^sbsKeepDoc/(?P<qid>[0-9]+)/(?P<did>.+)$', views.sbsKeepDoc, name='sbsKeepDoc'),
    url(r'^sbsExcludeDoc/(?P<qid>[0-9]+)/(?P<did>.+)$', views.sbsExcludeDoc, name='sbsExcludeDoc'),
    url(r'^delete_query/(?P<qid>[0-9]+)$', views.delete_query, name='delete'),
    url(r'^delete_sbs/(?P<sbsid>[0-9]+)$', views.delete_sbs, name='delete'),
    #### Others
    url(r'^switchmode$', views.switch_mode, name='switch_mode'),
    url(r'^technologies',views.technologies, name='technologies'),
    url(r'^technology/(?P<tid>[0-9]+)$',views.technology, name='technology'),
    url(r'^authorlist/(?P<tid>[0-9]+)$',views.prepare_authorlist, name='authorlist'),
    url(r'^add_tech',views.add_tech, name='add_tech'),
    url(r'^update_tech',views.update_tech, name='update_tech'),
    url(r'^technology_query',views.technology_query, name='technology_query'),
    url(r'^user$', views.userpage, name='userpage'),
    url(r'^update_criteria$', views.update_criteria, name='update_criteria'),
    url(r'^docs/(?P<qid>[0-9]+)$', views.doclist, name='doclist'),
    url(r'^docs/(?P<qid>[0-9]+)/(?P<q2id>[0-9]+)/(?P<sbsid>[0-9]+)$', views.doclist, name='doclist'),
    url(r'^docssbs/(?P<sbsid>[0-9]+)$', views.doclistsbs, name='doclistsbs'),
    url(r'^docrellist/(?P<sbsid>[0-9]+)/(?P<qid>[0-9]+)/(?P<q2id>[0-9]+)/(?P<q3id>[0-9]+)$', views.docrellist, name='docrellist'),
    url(r'^sort_docs$', views.sortdocs, name='sortdocs'),
    url(r'^cycle_score$', views.cycle_score, name='cycle_score'),
    url(r'^activate_user$', views.activate_user, name='activate_user'),
    url(r'^assign_docs$', views.assign_docs, name='assign_docs'),
    url(r'^remove_assignments$', views.remove_assignments, name='remove_assignments'),
    #### Individual docs
    url(r'^screen/(?P<qid>[0-9]+)/(?P<tid>[0-9]+)/(?P<ctype>[0-9]+)/(?P<d>[-0-9]+)$', views.screen, name='screen'),
    url(r'^do_review$', views.do_review, name='do_review'),
    url(r'^add_note', views.add_note, name='add_note'),
    url(r'^doc_tech', views.doc_tech, name='doc_tech'),
    url(r'^download/(?P<qid>[0-9]+)', views.download, name='download'),
    url(r'^delete/(?P<thing>[a-zA-Z]+)/(?P<thingid>[0-9]+)$', views.delete, name='delete'),
    url(r'^manual_add/(?P<qid>[0-9]+)$', views.add_doc_form, name='add_doc_form'),
    url(r'^manual_add/$', views.add_doc_form, name='add_doc_form'),
    url(r'^external_add/(?P<authtoken>[0-9a-f-]+)$', views.add_doc_form, name='add_doc_form'),
    url(r'^do_add_doc/$', views.do_add_doc, name='do_add_doc'),

]
