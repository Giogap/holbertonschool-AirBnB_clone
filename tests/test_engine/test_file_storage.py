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
        self.assertEqual(storage._FileStorage__file_path, 'file.json')
        self.assertDictEqual(storage._FileStorage__objects, {})