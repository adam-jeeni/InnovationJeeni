from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'InnovationJeeni.views.web', name='web'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'InnovationJeeni.views.index', name='home_page'),
    url(r'^innovation/?$', 'InnovationJeeni.views.innovation', name='innovation_page'),
    url(r'^close-the-gap/?$', 'InnovationJeeni.views.closethegap', name='closethegap_page'),
    
    url(r'^execute-your-business/?$', 'InnovationJeeni.views.executeyourbusiness', name='executeyourbusiness_page'),
    url(r'^high-performance-teams/?$', 'InnovationJeeni.views.highperformanceteams', name='highperformanceteams_page'),
    url(r'^fast-software-development/?$', 'InnovationJeeni.views.fastsoftwaredelivery', name='fastsoftwaredelivery_page'),
    url(r'^websites-that-kill/?$', 'InnovationJeeni.views.websitesthatkill', name='websitesthatkill_page'),
    url(r'^case-studies/?$', 'InnovationJeeni.views.casestudies', name='casestudies_page'),
    
    url(r'^admin/', include(admin.site.urls)),
)
