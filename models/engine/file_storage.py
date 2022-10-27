#!/usr/bin/python3
""" class FileStorage """



import json
import os


class FileStorage:
    """ serializes and deserializes instances to a JSON"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{} {}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects """
        with open(FileStorage.__file_path, "w+") as f:
            nDict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(nDict, f)

    def reload(self):
        """ Deserializes the JSON file """
        from models.base_model import BaseModel
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                l_dict = json.load(f)

            for key, value in l_dict.items:
                obj = eval(value["class"])(**value)
                FileStorage.__objects[key] = obj
        except Exception:
            pass


