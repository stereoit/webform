from django.conf.urls import include, url
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog

from webform.views import show_form, process_form, get_javascript

urlpatterns = [
    url(r'^$', show_form),
    url(r'^javascript$', get_javascript),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['webform']), name='javascript-catalog'),
    # url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^admin/', include(admin.site.urls)),
]
