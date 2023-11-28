#!/usr/bin/python3
"""Unittest module for User"""


import unittest
from datetime import datetime

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Unittest for the User class"""

    def test_attributes(self):
        user = User()
        user.email = ""
        user.first_name = ""
        user.last_name = ""
        user.password = ""

        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.password, "")

    def test_attributes_types(self):
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))
        self.assertEqual(str, type(User.password))

    def test_subclass(self):
        self.assertTrue(issubclass(User, BaseModel))


    if __name__ == '__main__':
        unittest.main()
