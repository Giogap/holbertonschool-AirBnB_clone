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
        myModel = BaseModel()
        d1 = myModel.updated_at
        d1.save()
        myModel2 = d1.update_at
        self.assertNotEqual(myModel, myModel2)


