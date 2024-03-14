#!/usr/bin/python3
"""Module of the test class of Place"""

import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """Test class of Place"""

    def setUp(self):
        """Set up instance for the tests"""
        self.instance = Place()

    def test_instance_of_Place(self):
        """instance is a object of Place"""
        self.assertIsInstance(self.instance, Place)

    def test_city_id_is_string(self):
        """Test if city_id is a string"""
        self.assertIsInstance(self.instance.city_id, str)

    def test_user_id_is_string(self):
        """Test if user_id is a string"""
        self.assertIsInstance(self.instance.user_id, str)

    def test_name_is_string(self):
        """Test if name is a string"""
        self.assertIsInstance(self.instance.name, str)

    def test_description_is_string(self):
        """Test if description is a string"""
        self.assertIsInstance(self.instance.description, str)

    def test_number_rooms_is_integer(self):
        """Test if number_rooms is a integer"""
        self.assertIsInstance(self.instance.number_rooms, int)

    def test_number_bathrooms_is_integer(self):
        """Test if number_bathrooms is a integer"""
        self.assertIsInstance(self.instance.number_bathrooms, int)

    def test_max_guest_is_integer(self):
        """Test if max_guest is a integer"""
        self.assertIsInstance(self.instance.max_guest, int)

    def test_price_by_night_is_integer(self):
        """Test if price_by_night is integer"""
        self.assertIsInstance(self.instance.price_by_night, int)

    def test_latitude_is_float(self):
        """Test if latitude is a float"""
        self.assertIsInstance(self.instance.latitude, float)

    def test_longitude_is_float(self):
        """Test if longitude is a float"""
        self.assertIsInstance(self.instance.longitude, float)

    def test_amenity_ids_is_string(self):
        """Test  if amenity_ids is a string"""
        self.assertIsInstance(self.instance.amenity_ids, str)
