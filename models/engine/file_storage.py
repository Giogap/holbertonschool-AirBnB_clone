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
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj].__class__.__name__.id = obj

    def save(self):
        """ Serializes __objects """
        nDict = {}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(nDict, f)

    def reload(self):
        """ Deserializes the JSON file """
        try:
<<<<<<< HEAD
            with open(self.file_path, "r") as f:
                nDict = f.read()
                self.__objects = json.load(f, nDict)
=======
            with open(self.file_path, "r", encoding="utf-8") as f:
                result = f.read()
                self.__objects = json.load(result)
>>>>>>> 64d77850526b0664a25bb160b279fc7aa6f80c90
        except FileNotFoundError:
            pass


