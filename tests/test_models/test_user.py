#!/usr/bin/python3
""" Test User """

import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Test class User"""
    def user(self):
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        self.assertEqual(my_user.first_name, "Betty")
        self.assertEqual(my_user.last_name, "Bar")
        self.assertEqual(my_user.email, "airbnb@mail.com")
        self.assertEqual(my_user.fpassword, "root")
