#!/usr/bin/python3
"""Module containing the class FileStorage"""

import json


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
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            data = {key: value.to_dict() 
                    for key, value in self.__objects.items()}
            json.dump(data, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:

            pass
