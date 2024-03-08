#!/usr/bin/python3
"""Module of the test class of City"""

import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """Test class of City"""

    def setUp(self):
        """Set up instance for the tests"""
        self.instance = City()

    def test_instance_of_City(self):
        """Test if the object is a instance of City"""
        self.assertIsInstance(self.instance, City)

    def test_state_id_is_string(self):
        """Test if state_id is a string"""
        self.assertIsInstance(self.instance.state_id, str)

    def test_name_is_string(self):
        """Test is name is a string"""
        self.assertIsInstance(self.instance.name, str)
