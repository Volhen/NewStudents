# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.images import ImageFile

from ..models import Student, Group
from datetime import datetime

# Views for Students

def students_list(request):
    students = Student.objects.all()

    students = students.order_by('last_name')
    #try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name','first_name','ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    
    #paginate students
    paginator = Paginator(students,3)
    page = request.GET.get('page')
    try:
        students=paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}

            # data for student object
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Имя обязательно"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Фамилия обязательно"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата рождения обязатель"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введите корректно формат даты (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Номер билета обязателен"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Выберите группу студенту"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Выберите корректную группу"
                else:
                    data['student_group'] = groups[0]


            #проверка по фото!!!
            if request.FILES.get('photo'):
                photo = request.FILES.get('photo')
                MAX_SIZE = 2097152 #2 mb in b
                photo_name = photo.name
                format_photo = photo_name[-3:]

                if format_photo in ('peg','jpg','png','gif'):
                    if photo.size > MAX_SIZE:
                        errors['photo'] = u"Розмер фото очень большой"
                    else:
                        data['photo'] = photo
                else:
                    errors['photo'] = u"Формат файла не соответствует"
                
            # save student
            if not errors:
                student = Student(**data)
                student.save()

                # redirect to students list
                return HttpResponseRedirect(
                    u'%s?status_message=Студент успешно добавлен %s !'% 
                    (reverse('home'),first_name))
            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                    {'groups': Group.objects.all().order_by('title'),
                     'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=Добавление студента отмененно!'% 
                reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
            {'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
