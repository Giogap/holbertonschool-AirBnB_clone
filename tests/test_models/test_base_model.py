#!/usr/bin/python3
"""
Test BaseModel
"""


from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestsBaseModel(unittest.TestCase):
    """ Test BaseModel """
    def testBaseMdlSave(self):
        save = datetime.now()
        self.assertEqual(save, datetime.now())
