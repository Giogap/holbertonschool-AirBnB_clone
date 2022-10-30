#!/usr/bin/python3
"""Test FileStorage"""

import unittest
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """TestCase FileStorage"""
    def test_fileStorage(self):
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    
    def test_file_path(self):
        """ Test FilePath"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"), False)

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

if __name__ == '__main__':
    unittest.main()
