#!/usr/bin/python3
"""
This module defines City as a class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This is a class that inherits from BaseModel.

    Attributes:
        state_id: public class attribute.
        name: public class attribute.
    """

    state_id = ""
    name = ""
