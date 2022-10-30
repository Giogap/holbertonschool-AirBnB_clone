#!/usr/bin/python3
"""Test FileStorage"""

import unittest
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test FileStorage"""

    def setUp(self):
        
        self.instanceOne = BaseModel()
        self.instanceTwo = BaseModel()

    def test_BaseModel(self):
        """Test BaseModel"""
        firstUpdate = self.instanceOne.updated_at
        self.instanceOne.save()
        secondUpdate = self.instanceOne.updated_at
        self.assertNotEqual(firstUpdate, secondUpdate)

    def test_id(self):
        """Test Id"""
        self.assertNotEqual(self.instanceOne.id, self.instanceTwo.id)

    def test_dict(self):
        """Test Dict"""
        self.assertIn("id", self.instanceOne.to_dict())
        self.assertIn("__class__", self.instanceOne.to_dict())
        self.assertIn("created_at", self.instanceOne.to_dict())
        self.assertIn("updated_at", self.instanceOne.to_dict())

    def test_str(self):
        """Test str"""
        self.assertIsInstance(self.instanceOne.__str__(), str)
        self.assertIn(self.instanceOne.id, self.instanceOne.__str__())
        self.assertIn(type(self.instanceOne).__name__,
        self.instanceOne.__str__())
