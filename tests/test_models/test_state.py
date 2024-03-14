#!/usr/bin/python3
"""Module Test of the class State"""

from models.state import State
import unittest


class Test_State(unittest.TestCase):
    """Test class of State"""

    def setUp(self):
        """Set up instance for the tests"""
        self.instance = State()

    def test_instance(self):
        """Test for the creation of the instance"""
        self.assertIsInstance(self.instance, State)

    def test_name_string(self):
        """Test for the name is string"""
        self.assertEqual(type(self.instance.name), str)
