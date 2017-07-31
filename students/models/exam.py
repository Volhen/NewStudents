# -*- coding: utf-8 -*-

from django.db import models


class Exam(models.Model):
    """Exam Models"""

    class Meta(object):
        verbose_name = u'Экзамен'
        verbose_name_plural = u'Экзамены'

    object_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Название предмета')
    
    date_time =models.DateTimeField(
        blank=False,
        verbose_name=u'Дата и время проведения экзамена',
        null=True)

    professor_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'ФИО преподавателя')
    
    groups_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u'Группа на экзамене')
    
    def __unicode__(self):
        return u"%s %s" % (self.object_name, self.professor_name)