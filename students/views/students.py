# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.images import ImageFile

from django.forms import ModelForm
from django.views.generic import UpdateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Student, Group


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

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('students_edit',
            kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Сохранить', css_class="btn btn-primary"),
            Submit('cancel_button', u'Откланить', css_class="btn btn-link"),
        )

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Студента успешно сохранено!' \
            % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редактирование студента отменено!' %
                reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
