#!/usr/bin/python3
"""Test FileStorage"""

import unittest
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """TestCase FileStorage"""
    def test_fileStorage(self):
        test = FileStorage.all(self)
        self.assertIsInstance(test, dict)
        self.assertEqual(len(test), 0)
        instanceBase = BaseModel()
        self.assertGreater(len(test), 0)
