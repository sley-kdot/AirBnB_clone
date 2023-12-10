#!/usr/bin/python3
"""Module contains the Review class and its properties"""

from models.base_model import BaseModel


class Review(BaseModel):
    """a class review that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
