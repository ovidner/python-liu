Python-LiU
============
A collection of tools for communicating with APIs and services used at Linköping University.

Please note: you will need a KOBRA API key to use the KOBRA client. Contact [Kårservice](mailto:it@karservice.se) to
apply for this.

Usage examples
--------------

### KOBRA Client
    >>> from liu.kobra import KOBRAClient
    >>> client = KOBRAClient('<username>', '<api key>')

    # By LiU ID
    >>> student = client.get_student(liu_id='abcde123')

    # By email address
    >>> student = client.get_student(email='abcde123@student.liu.se')

    # By personal id number
    >>> student = client.get_student(personal_number='yymmdd-xxxx')

    # By RFID number
    >>> student = client.get_student(rfid_number='0000000000')

    # By barcode/magnet number
    >>> student = client.get_student(barcode_number='0000000000000')

    >>> student
    {u'first_name': u'FIRST', u'last_name': u'LAST', u'union': u'LinTek', u'barcode_number': u'0000000000000', u'liu_id': u'abcde123', u'personal_number': u'yymmdd-xxxx', u'rfid_number': u'0000000000', u'email': u'abcde123@student.liu.se', u'blocked': None}

License
-------
[MIT License](http://choosealicense.com/licenses/mit/)