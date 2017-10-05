# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout
from crispy_forms.bootstrap import FormActions

from ..models import Exam
from ..util import paginate, get_current_group

def exam_list(request):
    # check if we need to show only one group of exam
    current_group = get_current_group(request)

    if current_group:
        exam = Exam.objects.filter(groups_name=current_group)
    else:
    # otherwise show all students
        exam = Exam.objects.all()

    # apply pagination, 3 exam per page
    context = paginate(exam, 3, request, {},
        var_name='exam')

    return render(request,'students/exam_list.html',context)

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        #fields = ('object_name','date_time','professor_name','groups_name')
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)

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
            self.helper.form_action = reverse('exam_add')
        else:
            self.helper.form_action = reverse('exam_edit',
                kwargs={'pk': kwargs['instance'].id})

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-lg-2 control-label'
        self.helper.field_class = 'col-lg-10'

        # add buttons
        if add_form:
            submit = Submit('add_button', u'Добавить',
                css_class="btn btn-primary")
        else:
            submit = Submit('save_button', u'Сохранить',
                css_class="btn btn-primary")

        self.helper.layout = Layout(
            'object_name',
            'date_time',
            'professor_name',
            'groups_name',
            FormActions(submit,Submit('cancel_button', u'Отменить', css_class="btn btn-link"))
        )
class BaseExamFormView(object):
    
    def get_success_url(self):
        return u'%s?status_message=Изменения успешно сохранены!'% reverse('exam')

    def post(self, request, *args, **kwargs):
        # handle cancel button
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('exam') +
                u'?status_message=Изменения отменены.')
        else:
            return super(BaseExamFormView, self).post(
                request, *args, **kwargs)

class ExamAddView(BaseExamFormView,CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'students/exam_form.html'
    

class ExamUpdateView(BaseExamFormView,UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'students/exam_form.html'
    

class ExamDeleteView(BaseExamFormView,DeleteView):
    model = Exam
    template_name = 'students/exam_confirm_delete.html'
    def get_success_url(self):
        return u'%s?status_message=Студент успешно удален!'%reverse('exam')