#!/usr/bin/python3
""" Class BaseModel"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ Class BaseModel """
    def __init__(self, *args, **kwargs):
        """ Public instance attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key == "create_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "update_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        clssN = self.__class__.__name__
        return "[{}] ({}) {}".format(clssN, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary of __dict__ """
        nDict = self.__dict__.copy()
        for key in nDict.keys():
            if key == "updated_at":
                nDict[key] = nDict[key].isoformat()
            if key == "created_at":
                nDict[key] = nDict[key].isoformat()
            nDict["__calss__"] = self.__class__.__name__
        return nDict
