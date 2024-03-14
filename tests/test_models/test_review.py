#!/usr/bin/python3
"""Module of the test class of Review"""

import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """Test class of Review"""

    def setUp(self):
        """Set up instance for the tests"""
        self.instance = Review()

    def test_instance(self):
        """Test for the creation of the instance"""
        self.assertIsInstance(self.instance, Review)

    def test_place_id_string(self):
        """Test for the place_id is string"""
        self.assertEqual(type(self.instance.place_id), str)

    def test_user_id_string(self):
        """Test for the user_id is string"""
        self.assertEqual(type(self.instance.user_id), str)

    def test_text_string(self):
        """Test for the text is string"""
        self.assertEqual(type(self.instance.text), str)