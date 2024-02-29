#!/usr/bin/python3
"""
This module defines Review as a class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is a class that inherits from BaseModel.

    Attributes:
        place_id: public class attributes
        user_id: public class attributes
        text: public class attributes.
    """

    place_id = ""
    user_id = ""
    text = ""
