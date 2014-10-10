# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from django_auth_ldap.backend import LDAPBackend
from .settings import LiUStudentLDAPSettings, LiUEmployeeLDAPSettings
from .models import LiUID


class _LiUBackend(LDAPBackend):
    """
    DON'T USE THIS AS YOUR AUTH BACKEND! Use the LiUStudentBackend and/or LiUEmployeeBackend instead.
    """

    def _get_settings(self):
        """
        Overridden since the _settings are always set in our subclasses.
        """

        return self._settings


class LiUStudentBackend(_LiUBackend):
    """
    An authentication backend for LiU students. Also works with the KOBRA API to fetch some more info about students.
    """

    settings_prefix = 'LIU_STUDENT_LDAP_'
    _settings = LiUStudentLDAPSettings(settings_prefix)

    def populate_liu_id(self, user):
        if not hasattr(user, 'liu_id'):
            user.liu_id = LiUID.objects.create(liu_id=user.username)
            user.save()

        user.liu_id.fetch()

        return user.liu_id

    def get_or_create_user(self, *args, **kwargs):
        user = super(LiUStudentBackend, self).get_or_create_user(*args, **kwargs)

        # get_or_create_user returns a tuple as ordinary get_or_create methods, we're only interested in the first item
        # (the actual object)
        self.populate_liu_id(user[0])

        return user


class LiUEmployeeBackend(_LiUBackend):
    """
    An authentication backend for LiU employees.
    """

    settings_prefix = 'LIU_EMPLOYEE_LDAP_'
    _settings = LiUEmployeeLDAPSettings(settings_prefix)