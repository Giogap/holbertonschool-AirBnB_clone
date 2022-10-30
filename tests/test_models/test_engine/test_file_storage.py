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
