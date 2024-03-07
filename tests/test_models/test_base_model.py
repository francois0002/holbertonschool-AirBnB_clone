#!/usr/bin/python3
"""Module of the test class of BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """Test class of BaseModel"""

    def setUp(self):
        """Set up instance for the tests"""
        self.instance = BaseModel()

    def test_instance_of_BaseModel(self):
        """Test if the object is a instance of BaseModel"""
        self.assertIsInstance(self.instance, BaseModel)

    def test_id_string(self):
        """Test if id is a type of string"""
        self.assertIsInstance(self.instance.id, str)

    def test_created_at_datetime(self):
        """Test if created_at use the module datetime"""
        self.assertIsInstance(self.instance.created_at, datetime)

    def test_updated_at_datetime(self):
        """Test if updated_at use the module datetime"""
        self.assertIsInstance(self.instance.updated_at, datetime)
