# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings

from liu.kobra import KOBRAClient


@python_2_unicode_compatible
class StudentUnion(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('name'))

    def __str__(self):
        return self.name


class LiUIDQuerySet(models.QuerySet):
    def fetch(self):
        for i in self:
            i.fetch()


@python_2_unicode_compatible
class LiUID(models.Model):
    """
    Stores a LiU ID. Fetches information from KOBRA with the fetch() method.

    liu_id is the only mandatory field.
    """
    liu_id = models.CharField(max_length=10, primary_key=True, verbose_name=_('LiU ID'))

    first_name = models.CharField(max_length=256, blank=True, verbose_name=_('first name'))
    last_name = models.CharField(max_length=256, blank=True, verbose_name=_('last name'))

    id_number = models.CharField(max_length=11, blank=True, verbose_name=_('national identification number'))

    barcode_number = models.CharField(max_length=32, blank=True, verbose_name=_('magnet/barcode card number'))
    rfid_number = models.CharField(max_length=32, blank=True, verbose_name=_('RFID card number'))

    student_union = models.ForeignKey('StudentUnion', related_name='members', blank=True, null=True,
                                      verbose_name=_('student union'))

    blocked = models.NullBooleanField(verbose_name=_('blocked'))

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='liu_id', blank=True, null=True,
                                verbose_name=_('user'))

    objects = LiUIDQuerySet.as_manager()

    class Meta:
        verbose_name = _('LiU ID')
        verbose_name_plural = _('LiU IDs')

    def __str__(self):
        return self.liu_id

    def fetch(self):
        """
        Updates the fields using KOBRA. Uses LiU ID to find user.
        """
        client = KOBRAClient(settings.LIU_KOBRA_USER, settings.LIU_KOBRA_API_KEY)
        # We don't catch any exceptions here. You might want to catch them in your own applications instead.
        data = client.get_student(liu_id=self.liu_id)

        if data:
            self.first_name = data['first_name']
            self.last_name = data['last_name']

            self.id_number = data['personal_number']

            self.barcode_number = data['barcode_number']
            self.rfid_number = data['rfid_number']

            self.student_union = StudentUnion.objects.get_or_create(name=data['union'])[0]

            self.blocked = data['blocked']

            self.save()