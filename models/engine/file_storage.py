#!/usr/bin/python3
"""Module containing the class FileStorage"""

import json
import os


class FileStorage:
    """
    a class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return (dict): a dictionary of the private attribute objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            data = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """
        Method desirializes the JSON file to __objects

        Raises:
           FileNotFoundError: If the json file is not found
        """
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    dict_obj = json.load(f)
                    for key, value in dict_obj.items():
                        class_name = value["__class__"]
                        class_obj = eval(class_name)
                        obj = class_obj(**value)
                        FileStorage.__objects[key] = obj
            except FileNotFoundError:
                pass
