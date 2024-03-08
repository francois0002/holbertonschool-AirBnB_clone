#!/usr/bin/python3
"""Module Test of the class User"""

from models.user import User
import unittest


class Test_User(unittest.TestCase):
    """Test class of User"""

    def setUp(self):
        """Set up instance for the tests"""
        self.instance = User()

    def test_instance(self):
        """Test for the creation of the instance"""
        self.assertIsInstance(self.instance, User)

    def test_email_string(self):
        """Test for the email is string"""
        self.assertEqual(type(self.instance.email), str)

    def test_password_string(self):
        """Test for the password is string"""
        self.assertEqual(type(self.instance.password), str)

    def test_first_name_string(self):
        """Test for the first_name is string"""
        self.assertEqual(type(self.instance.first_name), str)

    def test_last_name_string(self):
        """Test for the last_name is string"""
        self.assertEqual(type(self.instance.last_name), str)
