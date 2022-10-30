#!/usr/bin/python3
"""Test FileStorage"""

from ast import Store
import unittest
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """TestCase FileStorage"""

    def test_fileStorage(self):
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_fileStore_save(self):
        """Test FileStore Save"""
        storage = FileStorage()
        base = BaseModel()
        storage.new(base)
        storage.save()
        with open("file.json", "r", encoding='utf-8') as r:
            file_Json = r.read()
            self.assertTrue(f"BaseModel.{base.id}" in file_Json)
            file_json = r.read()
            self.assertTrue(f"BaseModel.{base.id}" in file_Json)

    def test_file(self):
        """test reload"""
        storage = FileStorage()
        obj = storage.all()
        copy = obj.copy()
        models.storage.reload()
        copy2 = obj.copy()
        self.assertEqual(len(copy), len(copy2))
        storage.save()
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """ >Test Reload """
        Storage = FileStorage()
        Storage.reload()
        self.assertIsNotNone(Storage.all())
        self.assertIs(Storage.all(), Storage.all())

    def test_save_reload(self):
        """ checking save and reload method """
        storage = FileStorage()
        base = BaseModel()
        base.name = "Betty"
        bid = base.id
        storage.new(base)
        storage.save()
        storage.reload()
        self.assertIsNotNone(
            storage.all()[base.__class__.__name__ + "." + bid])


if __name__ == '__main__':
    unittest.main()
