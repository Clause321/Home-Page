from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wyfHP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^portfolio/$', 'portfolio.views.portfolio'),
    url(r'^portfolio/(?P<i>\d)/detail/$', 'portfolio.views.show'),
    url(r'^$', 'basic.views.home'),
    
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))