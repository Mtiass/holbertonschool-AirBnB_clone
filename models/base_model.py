#!/usr/bin/python3
"""
This module defines BaseModel as a class.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    This is a class that defines all common attributes/methods
    for other classes.

    Attributes:
        id: is a public instance attribute.
        created_at: is a public instance attribute.
        updated_at: is a public instance attribute.
    """

    def __init__(self, *args, **kwargs):
        """
        This is the initializer method.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """
        This is a public instance method that updates updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This is a public instance method that returns a dictionary
        containing all keys/values of __dict__ of the instance.
        """
        ins_dic = self.__dict__.copy()
        ins_dic['__class__'] = self.__class__.__name__
        ins_dic['created_at'] = self.created_at.isoformat()
        ins_dic['updated_at'] = self.updated_at.isoformat()

        return (ins_dic)

    def __str__(self):
        """
        This is a method that returns a human-readable string,
        that is a representation of the object.
        """
        return ("[{}] ({}) {}".format(
           self.__class__.__name__, self.id, self.__dict__))
