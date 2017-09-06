from django.conf.urls import patterns, include, url
from django.contrib import admin

from students.views.students import StudentUpdateView, StudentDeleteView, StudentsAddView
from students.views.contact_admin import ContactView
from students.views.groups import GroupAddView, GroupUpdateView, GroupDeleteView
from .settings import MEDIA_ROOT, DEBUG


urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/(?P<pk>\d+)/edit/$',
        StudentUpdateView.as_view(),
        name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$',
        StudentDeleteView.as_view(),
        name='students_delete'),
    url(r'^students/add/$',
        StudentsAddView.as_view(),
        name='students_add'),

    # Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', GroupAddView.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(),
         name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(),
         name='groups_delete'),
    # Journal urls
    url(r'^journal/$', 'students.views.journal.journal_list', name='journal'),

    # Exam urls
    url(r'^exam/$', 'students.views.exam.exam_list', name='exam'),

    #Contact admin Form
    #url(r'^contact-admin/$','students.views.contact_admin.contact_admin', name='contact_admin'),
    url(r'^contact-admin/$',ContactView.as_view(),name='contact_admin'),
    url(r'^admin/', include(admin.site.urls)),

    #Students edit
    url(r'^students/(?P<pk>\d+)/edit/$',StudentUpdateView.as_view(),name='students_edit'),
    
)
if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))