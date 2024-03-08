#!/usr/bin/python3
"""Module of the test class of Amenity"""

import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """Test class of Amenity"""

    def setUp(self):
        """Set up instance for the tests"""
        self.instance = Amenity()

    def test_instance_of_Amenity(self):
        """Test if the object is a instance of Amenity"""
        self.assertIsInstance(self.instance, Amenity)

    def test_name_is_string(self):
        """Test is name is a string"""
        self.assertIsInstance(self.instance.name, str)
