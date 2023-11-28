#!/usr/bin/python3
"""Unittest module for Review"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review unitttests"""

    def test_attribute(self):
        """Test the attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
