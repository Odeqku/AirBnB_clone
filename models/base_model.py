#!/usr/bin/python3
# Task: Defines the BaseModel class."""
"""Importing all files for the Class File
models: to import all packages 
uuid: module for generating a unique user id
datatime: Module for keeping track of time and date"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or k == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            pass

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        

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
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
