
#!/usr/bin/python3
"""Test FileStorage"""


import unittest
import models
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage


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


storage = FileStorage()
obj = storage.all()
base = BaseModel()
storage.reload()


if __name__ == '__main__':
    unittest.main()
