# -*- coding: utf-8 -*-
import requests
from requests.exceptions import HTTPError


class StudentNotFound(Exception):
    pass


class Unauthorized(Exception):
    pass


class KOBRAClient(object):
    """
    A dead simple API client to KOBRA.
    """
    url = 'https://kobra.ks.liu.se/students/api.json'
    accepted_params = [
        'liu_id',
        'email',
        'personal_number',
        'rfid_number',
        'barcode_number'
    ]

    def __init__(self, user, key):
        self.user = user
        self.key = key

    def get_student(self, **kwargs):
        """
        Calls the API and gets a student by **one** (1) of these parameters at a time:
        :param liu_id: LiU-ID (e.g. johec890)
        :param email: Email address (e.g. johec890@student.liu.se)
        :param personal_number: Personal identification number (e.g. 860421-0000)
        :param rfid_number: LiU card number (NFC/RFID, e.g. 3479871166)
        :param barcode_number: LiU card number (barcode/magnet, e.g. 975226854847805)
        :return: A dictionary with student data.
        """
        if len(kwargs) != 1 or not any(i in self.accepted_params for i in kwargs.keys()):
            # Raises a TypeError if called with other than exactly 1 argument or with other parameter than the ones
            # accepted.
            raise TypeError('Called with invalid argument(s) and/or wrong number of arguments.')

        response = requests.post(self.url, kwargs, auth=(self.user, self.key))

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise Unauthorized('Invalid credentials.')
        elif response.status_code == 404:
            raise StudentNotFound
        else:
            raise HTTPError(('HTTP %s error.' % response.status_code), response=response)