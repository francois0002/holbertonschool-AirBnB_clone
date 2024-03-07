#!/usr/bin/python3
"""Module of the class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Creation of the class Place an inherited class of BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """Constructor of the class Place

        Args:
            args: tuple of arguments
            kwargs: dictionary of arguments
        """
        super().__init__(*args, **kwargs)
