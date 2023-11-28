#!/usr/bin/python3
"""FileStorage test module"""


import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test__file_path(self):
        """Test __file_path attribute"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test__objects(self):
        """Test __objects attribute"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        """Test all method"""
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        """Test new method"""
        base = BaseModel()
        storage.new(base)
        self.assertIn("BaseModel." + base.id, storage.all().keys())
        self.assertIn(base, storage.all().values())

    def test_save(self):
        """Test save method"""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        """Test reload method"""
        with self.assertRaises(TypeError):
            storage.reload(None)
