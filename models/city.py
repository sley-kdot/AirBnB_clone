#!/usr/bin/python3
"""Module contains the City class and its properties"""

from models.base_model import BaseModel


class City(BaseModel):
    """a class City that inherits from the BaseModel"""
    state_id = ""
    name = ""
