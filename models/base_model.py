#!/usr/bin/python3
"""This module creates a BaseModel class """

import uuid
from datetime import datetime


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model

        Args:
            args: tuples of arguments
            kwargs: dictionary of arguments
            id : Define unique id randomly generate with uuid
            created_at : Date time of creation
            updated_at : Date time of last update
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.now())
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Return the string representation of object instance."""
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """return a dictionary containing all keys/values of class instances"""
        class_name = type(self).__name__
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = class_name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
