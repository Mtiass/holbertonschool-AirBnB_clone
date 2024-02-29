#!/usr/bin/python3
"""
This module defines Amenity as a class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class inherits from BaseModel.

    Attributes:
        name: this a public class attribute.
    """
    name = ""
