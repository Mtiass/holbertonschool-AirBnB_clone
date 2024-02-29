#!/usr/bin/python3
"""
Unittest for Place class.
"""
import unittest
from models.place import Place


class Place_Test(unittest.TestCase):
    """
    Tests for Place class
    """
    def setUp(self):
        """This is the set up function."""
        self.place = Place()

    def test_attributes_existence(self):
        """This function tests for attributes_existence"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_is_string(self):
        """This function tests if id is a string"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)

    def test_is_integer(self):
        """This function tests if is integer."""
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)

    def test_is_float(self):
        """This function tests if is float."""
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)

    def test_is_list(self):
        """Function to test if is list."""
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
