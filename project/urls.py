from django.conf.urls import include, url
from django.contrib import admin

from webform.views import show_form, process_form

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', show_form),
    # url(r'^process-form$', process_form),
    # url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
]
