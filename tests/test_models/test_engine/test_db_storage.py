#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
import MySQLdb
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db',
                     "Do test this only if storage is db")
    def setUp(self):
        """set up for test"""
        if os.getenv("HBNB_TYPE_STORAGE") == 'db':
            self.db = MySQLdb.connect(os.getenv("HBNB_MYSQL_HOST"),
                                      os.getenv("HBNB_MYSQL_USER"),
                                      os.getenv("HBNB_MYSQL_PWD"),
                                      os.getenv("HBNB_MYSQL_DB"))
            self.cursor = self.db.cursor()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db',
                     "Do test this only if storage is db")
    def tearDown(self):
        """at the end of the test this will tear it down"""
        if os.getenv("HBNB_TYPE_STORAGE") == 'db':
            self.db.close()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db',
                     "Do test this only if storage is db")
    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db',
                     "Do test this only if storage is db")
    def test_attributes_DBStorage(self):
        """Test DBStorage attributes methods"""
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))


if __name__ == "__main__":
    unittest.main()
