#!/usr/bin/python3
"""Module of the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """Creation of the class User an inherited class of BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
