
#!/usr/bin/python3
"""Test FileStorage"""


import unittest
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel
from models import storage 
import os


class TestFileStorage(unittest.TestCase):
    """TestCase FileStorage"""
    def test_fileStorage(self):
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_fileStore_save(self):
        """Test FileStore Save"""
        storage.new(base)
        storage.save()
        with open("file.json", "r", encoding='utf-8') as r:
            file_Json = r.read()
            self.assertTrue(f"BaseModel.{base.id}" in file_Json)
            file_json = r.read()
            self.assertTrue(f"BaseModel.{base.id}" in file_Json)

    def test_file(self):
        """test reload"""
        copy = obj.copy()
        models.storage.reload()
        copy2 = obj.copy()
        self.assertEqual(len(copy), len(copy2))
        storage.save()
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """ Test Reload"""
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(base.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Doc """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_none(self):
        """ Doc """
        self.assertEqual(storage.reload(), None)


storage = FileStorage()
obj = storage.all()
base = BaseModel()

if __name__ == '__main__':
    unittest.main()
