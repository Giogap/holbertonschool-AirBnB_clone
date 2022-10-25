#!/usr/bin/python3
""" Doc """


from models.base_model import BaseModel
import json


class FileStorage:
    """"""

    def __init__(self, file_path, objects):
        self.__file_path = file_path
        self.__objects = objects


    def all(self):
        return self.__objects


    def new(self, obj):
        self.__objects[obj].__class__.__name__.id = obj


    def save(self):
        nDict = {}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(nDict, f)

    def reload(self):
        pass