#!/usr/bin/python3
"""class User"""


from models.base_model import BaseModel

<<<<<<< HEAD
class User:
    """"""
=======

class User(BaseModel):
    """class User that inherits from BaseModel"""
>>>>>>> 06881f103fb1d9017cc72e0c6493ce590c213c89
    email = ""
    password = ""
    first_name = ""
    last_name = ""
