#!/usr/bin/python3
"""
This module defines State as a class.
"""
import models
from models.base_model import BaseModel


class State(BaseModel):
    """
    This is a class that inherits from BaseModel.

    Attributes:
        name: is a public class attribute.
    """

    name = ""
