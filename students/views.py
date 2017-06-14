# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
        {'id': 1,
        'first_name': u'Виталий',
        'last_name': u'Подоба',
        'ticket': 235,
        'image': 'img/invisible-man.jpg'},
        {'id': 2,
        'first_name': u'Андрей',
        'last_name': u'Корост',
        'ticket': 2123,
        'image': 'img/profilepic.gif'},
        {'id': 3,
        'first_name': u'Виктор',
        'last_name': u'Потребенко',
        'ticket': 254,
        'image': 'img/stranger.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return render(request, 'students/students_add.html', {})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

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

# Views for Groups
def journal_list(request):
    return render(request, 'students/journal_list.html', {})