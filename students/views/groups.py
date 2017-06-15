# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups

def groups_list(request):
    students_groups = (
        {'id': 1,
        'groups_name': u'МтМ-21',
        'ST_name': u'Ячменев Олег'},
        {'id': 2,
        'groups_name': u'МтМ-22',
        'ST_name': u'Иванов Иван'},
        {'id': 3,
        'groups_name': u'МтМ-23',
        'ST_name': u'Потребенко Виктор'},
    )
    return render(request, 'students/groups_list.html', {'students_groups': students_groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
