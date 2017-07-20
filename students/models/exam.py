# -*- coding: utf-8 -*-

from django.db import models


class Exam(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Название")

    leader = models.OneToOneField('Student',
        verbose_name=u"Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Доп заметки")

    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name,
                 self.leader.last_name)
        else:
            return u"%s" % (self.title,)
