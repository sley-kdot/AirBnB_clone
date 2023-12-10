#!/usr/bin/python3
"""Module contains the User class and it's properties"""

from models.base_model import BaseModel


class User(BaseModel):
    """a class that inherits from the BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
