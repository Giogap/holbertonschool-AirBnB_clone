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
        self.my_model = BaseModel()
        self.my_model.save()
        self.assertIsNotNone(BaseModel.save)
