KOBRA Client
============
A simple client for the KOBRA API.

Please note: you will need a KOBRA API key to use this.

Usage
-----
    from kobra import KOBRAClient
    client = KOBRAClient('user', 'key')
    student = client.get_student(liu_id='abcde123')