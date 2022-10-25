#!/usr/bin/python3
"""
Test BaseModel
"""


from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestsBaseModel(unittest.TestCase):
    """ Test BaseModel """
    def testBaseMdlId(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(my_model.my_number, 89)

