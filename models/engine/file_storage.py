#!/usr/bin/python3
""" class FileStorage """


from models.base_model import BaseModel
import json


class FileStorage:
    """ serializes and deserializes instances to a JSON"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj].__class__.__name__.id = obj

    def save(self):
        """ Serializes __objects """
        nDict = {}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(nDict, f)

    def reload(self):
        """ Deserializes the JSON file """
        try:
            with open(self.file_path, "r") as f:
                nDict = f.read()
                self.__objects = json.load(f, nDict)
        except FileNotFoundError:
            pass


