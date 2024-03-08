#!/usr/bin/python3
"""Module Test of the class FileStorage"""

import unittest
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """Test class of FileStorage"""

    def setUp(self):
        """Set up instance for the tests"""
        self.instance = FileStorage()

    def test_instance(self):
        """Test for the creation of the instance"""
        self.assertIsInstance(self.instance, FileStorage)
