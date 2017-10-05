# -*- coding: utf-8 -*-
#from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core.files.images import ImageFile

from django.forms import ModelForm
from django.views.generic import UpdateView, CreateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout
from crispy_forms.bootstrap import FormActions

from ..models import Student, Group
from ..util import paginate, get_current_group


# Views for Students

def students_list(request):
    # check if we need to show only one group of students
    current_group = get_current_group(request)
    
    if current_group:
        students = Student.objects.filter(student_group=current_group)
    else:
    # otherwise show all students
        students = Student.objects.all()
     # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # apply pagination, 3 students per page
    context = paginate(students, 3, request, {},
        var_name='students')

    return render(request, 'students/students_list.html', context)


#def students_add(request):
    # was form posted?
#    if request.method == "POST":
#        # was form add button clicked?
#        if request.POST.get('add_button') is not None:
            # errors collection
#            errors = {}

            # data for student object
#            data = {'middle_name': request.POST.get('middle_name'),
#                    'notes': request.POST.get('notes')}

            # validate user input
#            first_name = request.POST.get('first_name', '').strip()
#            if not first_name:
#                errors['first_name'] = u"Имя обязательно"
#            else:
#                data['first_name'] = first_name

#            last_name = request.POST.get('last_name', '').strip()
#            if not last_name:
#                errors['last_name'] = u"Фамилия обязательно"
#            else:
#                data['last_name'] = last_name

#            birthday = request.POST.get('birthday', '').strip()
#            if not birthday:
#                errors['birthday'] = u"Дата рождения обязатель"
#            else:
#                try:
#                    datetime.strptime(birthday, '%Y-%m-%d')
#                except Exception:
#                    errors['birthday'] = u"Введите корректно формат даты (напр. 1984-12-30)"
#                else:
#                    data['birthday'] = birthday

#            ticket = request.POST.get('ticket', '').strip()
#            if not ticket:
#                errors['ticket'] = u"Номер билета обязателен"
#            else:
#                data['ticket'] = ticket

 #           student_group = request.POST.get('student_group', '').strip()
 #           if not student_group:
 #               errors['student_group'] = u"Выберите группу студенту"
 #           else:
 #               groups = Group.objects.filter(pk=student_group)
 #               if len(groups) != 1:
 #                   errors['student_group'] = u"Выберите корректную группу"
 #               else:
 #                   data['student_group'] = groups[0]


            #проверка по фото!!!
#            if request.FILES.get('photo'):
#                photo = request.FILES.get('photo')
#                MAX_SIZE = 2097152 #2 mb in b
#                photo_name = photo.name
#                format_photo = photo_name[-3:]

#                if format_photo in ('peg','jpg','png','gif'):
#                    if photo.size > MAX_SIZE:
#                        errors['photo'] = u"Розмер фото очень большой"
#                    else:
#                        data['photo'] = photo
#                else:
#                    errors['photo'] = u"Формат файла не соответствует"
                
            # save student
#            if not errors:
#                student = Student(**data)
#                student.save()

                # redirect to students list
#                return HttpResponseRedirect(
#                    u'%s?status_message=Студент успешно добавлен %s !'% 
#                    (reverse('home'),first_name))
 #           else:
                # render form with errors and previous user input
#                return render(request, 'students/students_add.html',
#                    {'groups': Group.objects.all().order_by('title'),
#                     'errors': errors})

#        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
#            return HttpResponseRedirect(
#                u'%s?status_message=Добавление студента отмененно!'% 
#                reverse('home'))
#    else:
        # initial form render
#        return render(request, 'students/students_add.html',
#            {'groups': Group.objects.all().order_by('title')})

class StudentForm(ModelForm):
    class Meta:
        model = Student

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        #add form or edit form
        if kwargs['instance'] is None:
            add_form = True
        else:
            add_form = False
            
        # set form tag attributes
        if add_form:
            self.helper.form_action = reverse('students_add')
        else:
            self.helper.form_action = reverse('students_edit',
                kwargs={'pk': kwargs['instance'].id})

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        if add_form:
            submit = Submit('add_button', u'Добавить',
                css_class="btn btn-primary")
        else:
            submit = Submit('save_button', u'Сохранить',
                css_class="btn btn-primary")
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'middle_name',
            'birthday',
            'photo',
            'ticket',
            'student_group',
            'notes',
            FormActions(submit,Submit('cancel_button', u'Отменить', css_class="btn btn-link"))
        )

class BaseStudentsFormView(object):
    
    def get_success_url(self):
        return u'%s?status_message=Изменения успешно сохранены!'% reverse('home')

    def post(self, request, *args, **kwargs):
        # handle cancel button
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('home') +
                u'?status_message=Изменения отменены.')
        else:
            return super(BaseStudentsFormView, self).post(
                request, *args, **kwargs)

class StudentsAddView(BaseStudentsFormView,CreateView):
    model =Student
    template_name = 'students/students_form.html'
    form_class = StudentForm

class StudentUpdateView(BaseStudentsFormView,UpdateView):
    model = Student
    template_name = 'students/students_form.html'
    form_class = StudentForm

class StudentDeleteView(BaseStudentsFormView,DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'
    def get_success_url(self):
        return u'%s?status_message=Студент успешно удален!'%reverse('home')
