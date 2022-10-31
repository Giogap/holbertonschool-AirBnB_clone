#!/usr/bin/python3
"""Test user"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """class Test from user"""

    def test_city(self):
        """Test User"""
        c = City()
        self.assertTrue(issubclass(u.__class__, BaseModel))
        self.assertTrue(hasattr(c, "id"))
        self.assertTrue(hasattr(c, "created_at"))
        self.assertTrue(hasattr(c, "updated_at"))
        self.assertTrue(hasattr(c, "first_name"))
        self.assertTrue(hasattr(c, "last_name"))
        self.assertTrue(hasattr(c, "email"))
        self.assertTrue(hasattr(c, "password"))
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")

        c.state_id = "89"
        c.name = "My First Model"
        s = f"[{c.__class__.__name__}] ({c.id}) {c.__dict__}"
        self.assertEqual(s, str(c))


if __name__ == '__main__':
    unittest.main()
