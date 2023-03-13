#!/usr/bin/python3
# Task: Defines the BaseModel class."""
"""Importing all files for the Class File"""

import models

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel Instance with:
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            del kwargs['__class__']

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif not key == '__class__':
                    self.__dict__[key] = value

            if not self.__dict__ in FileStorage.__objects:
                models.storage.new(self)

        else:
            pass


    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

        '''Save the instance to the file_storage.'''
        self.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        cp_dict = self.__dict__.copy()
        cp_dict["created_at"] = self.created_at.isoformat()
        cp_dict["updated_at"] = self.updated_at.isoformat()
        cp_dict["__class__"] = self.__class__.__name__
        return cp_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return f"[{clname}] ({self.id}) {self.__dict__}"


#Test Case

