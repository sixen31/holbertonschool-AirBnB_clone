#!/usr/bin/python3
"""Unittest module for Amenity"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Amenity unittests"""

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
