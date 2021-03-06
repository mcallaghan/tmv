from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from tmv_app.views import *
from django.contrib.auth.decorators import login_required

app_name = 'tmv_app'

urlpatterns = [
    url(r'^$', login_required(runs), name='index'),
    path('network/<int:run_id>', login_required(network), name='network'),
    path('network/<int:run_id>/<str:csvtype>', login_required(network), name='network'),
    url(r'^network_wg/(?P<run_id>\d+)$', login_required(network_wg), name='network_wg'),
    url(r'^network_wg/(?P<run_id>\d+)/(?P<t>\d+)/(?P<f>\d+)/(?P<top>.+)$', login_required(network_wg), name='network_wg'),
    url(r'^return_corrs$', login_required(return_corrs), name='return_corrs'),
    url(r'^growth/(?P<run_id>\d+)$', login_required(growth_heatmap), name='growth_heatmap'),
    url(r'^growth_json/(?P<run_id>\d+)/(?P<v>.+)/$', login_required(growth_json), name='growth_json'),

    # topic page and topic doc loader
    url(r'^topic/(?P<topic_id>\d+)/$', login_required(topic_detail), name="topic_detail"),
    url(r'^topic/(?P<topic_id>\d+)/(?P<run_id>\d+)/$', login_required(topic_detail), name="topic_detail"),
    url(r'^get_topic_docs/(?P<topic_id>\d+)/$', login_required(get_topic_docs), name="get_topic_docs"),
    path('get_topicterms/<int:topic_id>', login_required(get_topicterms), name="get_topicterms"),
    url(r'^multi_topic/$', login_required(multi_topic), name="multi_topic"),

    url(r'^highlight_dtm_w$', login_required(highlight_dtm_w), name="highlight_dtm_w"),
    url(r'^dynamic_topic/(?P<topic_id>\d+)/$', login_required(dynamic_topic_detail), name="dynamic_topic_detail"),

    url(r'^term/(?P<run_id>\d+)/(?P<term_id>\d+)/$', login_required(term_detail), name="term_detail"),
    url(r'^doc/random/(?P<run_id>\d+)$', login_required(doc_random), name="random_doc"),
    url(r'^doc/(?P<doc_id>.+)/(?P<run_id>\d+)$', login_required(doc_detail), name="doc_detail"),
    url(r'^author/(?P<author_name>.+)/(?P<run_id>\d+)$', login_required(author_detail), name="author_detail"),
    url(r'^institution/(?P<run_id>\d+)/(?P<institution_name>.+)/$', login_required(institution_detail)),
    # Home page
    url(r'^topic_presence/(?P<run_id>\d+)$', login_required(topic_presence_detail),name="topics"),

    url(r'^topics_time/(?P<run_id>\d+)/(?P<stype>\d+)$', login_required(topics_time),name="topics_time"),
    url(r'^topics_time_csv/(?P<run_id>\d+)/$', login_required(get_yt_csv),name="topics_time_csv"),
    url(r'^stats/(?P<run_id>\d+)$', login_required(stats), name="stats"),

    url(r'^runs$', login_required(runs), name='runs'),
    url(r'^runs/(?P<pid>\d+)/$', login_required(runs), name='runs'),

    url(r'^adjust_threshold/(?P<run_id>\d+)/(?P<what>.+)$', login_required(adjust_threshold), name='adjust_threshold'),

    url(r'^update/(?P<run_id>\d+)$', login_required(update_run), name='update'),
    url(r'^runs/delete/(?P<new_run_id>\d+)$', login_required(delete_run), name='delete_run'),

    url(r'^topic/random$', login_required(topic_random)),
    url(r'^term/random$', login_required(term_random)),
    url(r'^print_table/(?P<run_id>\d+)$', login_required(print_table), name="print_table"),

    url(r'^compare/(?P<a>\d+)/(?P<z>\d+)$', login_required(compare_runs), name="compare_runs")

    ]


    # Example:
    # (r'^BasicBrowser/', include('BasicBrowser.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),



#onyl serve static content for development
#urlpatterns += static(settings.STATIC_URL,document_root='static')
