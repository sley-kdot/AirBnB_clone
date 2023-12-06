#!/usr/bin/python3
""" Module contains the base model for creating all
instances of the class
"""

from datetime import datetime
import uuid


class BaseModel:
    """ Class defines all common attributes/ methods for
    other classes

    Arguments:
        args (tuple): accepts non positional variable arguments
        kwargs (dict): accepts positional keyword arguments
    """

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns the readable string representation of an instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Method updates the public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Method returns key/values of the __dict__ of the
        instance
        """

        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
