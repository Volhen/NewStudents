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

from ..models import Group
from ..util import paginate, get_current_group


def groups_list(request):
    # check if we need to show only one group of students
    current_group = get_current_group(request)
    
    if current_group:
        groups = Group.objects.filter(title=current_group)
    else:
    # otherwise show all students
        groups = Group.objects.all()
     # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title',):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # apply pagination, 3 groups per page
    context = paginate(groups, 3, request, {}, var_name='groups')

    return render(request, 'students/groups_list.html', context)


class GroupForm(ModelForm):
    class Meta:
        model = Group
    def __init__(self, *args, **kwargs):
        super(GroupForm,self).__init__(*args,**kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        
        #add form or edit form
        if kwargs['instance'] is None:
            add_form = True
        else:
            add_form = False
        
        #set form tag attributes
        if add_form:
            self.helper.form_action = reverse('groups_add')
        else:
            self.helper.form_action = reverse('groups_edit',
                kwargs={'pk': kwargs['instance'].id})

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-8'

         # add buttons
        if add_form:
            submit = Submit('add_button', u'Добавить',
                css_class="btn btn-primary")
        else:
            submit = Submit('save_button', u'Сохранить',
                css_class="btn btn-primary")
        self.helper.layout = Layout(
            'title',
            'leader',
            'notes',
            FormActions(submit,Submit('cancel_button', u'Отменить', css_class="btn btn-link"))
        )

class BaseGroupFormView(object):
    
    def get_success_url(self):
        return u'%s?status_message=Изменения успешно сохранены!'% reverse('groups')

    def post(self, request, *args, **kwargs):
        # handle cancel button
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('groups') +
                u'?status_message=Изменения отменены.')
        else:
            return super(BaseGroupFormView, self).post(
                request, *args, **kwargs)

class GroupAddView(BaseGroupFormView, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'students/groups_form.html'

class GroupUpdateView(BaseGroupFormView, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'students/groups_form.html'

class GroupDeleteView(BaseGroupFormView, DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'
    def get_success_url(self):
        return u'%s?status_message=Группа успешно удалена!'%reverse('groups')
