#!/usr/bin/python3
""" Class BaseModel"""

from multiprocessing.sharedctypes import Value
from unittest.mock import create_autospec
from uuid import uuid4
from datetime import datetime
from venv import create

class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                pass
        self.id = str(uuid4())
        self.create_at = datetime.now()
        self.update_at = datetime.now()


    def __str__(self):
        clssN = self.__class__.__name__
        return "[{}] ({}) {}".format(clssN ,self.id, self.__dict__)

    
    def save(self):
        """ """
        self.update_at = datetime.now()

    def to_dict(self):
        nDict = self.__dict__
        nDict["__class__"] = __class__.__name__
        nDict["created_at"] = self.create_at.isoformat()
        nDict["update_at"] = self.update_at.isoformat()
        return self.__dict__
