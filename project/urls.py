import time
from django.conf.urls import include, url
from django.views.decorators.cache import cache_page
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog

from webform.views import show_form, process_form, get_javascript

def get_version():
    return int(time.time())

urlpatterns = [
    url(r'^$', show_form),
    url(r'^javascript$', get_javascript),
    url(r'^jsi18n/$',
        # JavaScriptCatalog.as_view(),
        cache_page(86400, key_prefix='js18n-%s' % get_version())(JavaScriptCatalog.as_view(packages=['webform'])),
        name='javascript-catalog'),
    url(r'^admin/', include(admin.site.urls)),
]
