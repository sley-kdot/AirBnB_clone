#!/usr/bin/python3
from models.base_model import BaseModel
import json

class FileStorage(BaseModel):
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{self.__class__.__name__}.{self.id}"
        self.__objects[key] = obj
