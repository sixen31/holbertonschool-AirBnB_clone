#!/usr/bin/python3
"""Unittest module for State"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """State unittests"""

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")
