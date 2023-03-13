#!/usr/bin/python3
# Task: Defines the BaseModel class."""
"""Importing all files for the Class File"""

<<<<<<< HEAD
=======
import models

>>>>>>> 97de90edc4e584062b5693fb642e9e89b0a93f65
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
<<<<<<< HEAD
        if len(kwargs) != 0:
            del kwargs['__class__']
=======

        if kwargs:
>>>>>>> 97de90edc4e584062b5693fb642e9e89b0a93f65
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
<<<<<<< HEAD
=======
        '''Save the instance to the file_storage.'''
        self.storage.save()
>>>>>>> 97de90edc4e584062b5693fb642e9e89b0a93f65

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
<<<<<<< HEAD
        return f"[{clname}] ({self.id}) {self.__dict__}".format(clname, self.id, self.__dict__)

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
=======
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

>>>>>>> 97de90edc4e584062b5693fb642e9e89b0a93f65
