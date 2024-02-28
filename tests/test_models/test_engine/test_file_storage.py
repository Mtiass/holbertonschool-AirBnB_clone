#!/usr/bin/python3
"""
Unittest for FileStorage class.
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class FileStorage_Test(unittest.TestCase):
    """
    Tests for FileStorage class
    """
    def setUp(self):
        """This is the set up function."""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """This is the tearDown function."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_file_path_attribute(self):
        """This function tests __file_path attribute"""
        self.assertEqual(
            self.storage._FileStorage__file_path, "test_file.json")

    def test_working_save(self):
        """Test to validate save works."""
        fs = FileStorage()
        fs.new(BaseModel())
        fs.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_objects_attribute(self):
        """This function tests __objects attribute"""
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all_method(self):
        """This function tests all method"""
        self.assertEqual(self.storage.all(), {})

    def test_all_return_type(self):
        """Test to validate all() returns an object."""
        self.assertEqual(type(self.storage.all()), dict)

    def test_new_method(self):
        """This function tests new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], obj)

    def test_save_method(self):
        """This function tests save method"""
        obj = BaseModel()
        key = "BaseModel.{}".format(obj.id)
        self.storage._FileStorage__objects[key] = obj
        self.storage.save()
        # Check if the file has been created and contains the serialized data
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            self.assertIn(key, data)
            self.assertEqual(data[key], obj.to_dict())

    def test_reload_method(self):
        """This function tests reload method"""
        obj = BaseModel()
        key = "BaseModel.{}".format(obj.id)
        self.storage._FileStorage__objects[key] = obj
        self.storage.save()
        # Clear objects and reload from the file
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(key, self.storage._FileStorage__objects)
        reloaded_obj = self.storage._FileStorage__objects[key]
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.to_dict(), obj.to_dict())


if __name__ == '__main__':
    unittest.main()
