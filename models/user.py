#!/usr/bin/python3
"""
This module defines User as a class.
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a class that inherits from BaseModel.

    Attributes:
        email: public class attribute
        password: public class attribute
        first_name: public class attribute
        last_name: public class attribute
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
