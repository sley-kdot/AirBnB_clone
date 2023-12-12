#!/usr/bin/python3
""" Test file for file_storage module """

import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Tests for the FileStorage class """

    def setUp(self):
        """ Creates an instance of FileStorage """
        self.my_storage = FileStorage()

    def tearDown(self):
        """ Test clean up method """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_types(self):
        """ Test the attribute type """
        self.assertEqual(type(self.my_storage.all()), dict)

    def test_when_a_new_instance_is_created(self):
        """ Test_when_a_new_instance_is_created """
        obj = BaseModel()
        self.my_storage.new(obj)
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(obj_key, self.my_storage.all())

    def test_save_and_reload(self):
        """ Test save and reload method """
        obj = BaseModel()
        self.my_storage.new(obj)
        obj.save()
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.my_storage.reload()
        self.assertIn(obj_key, objects)

    def test_storage_instance(self):
        """ Test_storage_instance """
        self.assertIsInstance(models.storage, FileStorage)
