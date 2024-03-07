#!/usr/bin/python3
"""Module of the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Creation of the class Review an inherited class of BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor of Review

        Args:
            args: tuple of arguments
            kwargs: dictionary of arguments
        """
        super().__init__(*args, **kwargs)
