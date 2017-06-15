# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups
def journal_list(request):
    return render(request, 'students/journal_list.html', {})