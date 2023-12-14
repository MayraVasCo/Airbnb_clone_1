import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        # Test the initialization of the BaseModel instance
        bm = BaseModel()

        # Check if id is a string
        self.assertIsInstance(bm.id, str)

        # Check if created_at and updated_at are datetime objects
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

        # Check if created_at and updated_at are roughly the same initially
        self.assertAlmostEqual(bm.created_at.timestamp(), bm.updated_at.timestamp(), delta=0.01)

    def test_save_method(self):
        # Test the save method updates the updated_at attribute
        bm = BaseModel()
        initial_updated_at = bm.updated_at

        # Wait for a short time to ensure a change in the updated_at attribute
        import time
        time.sleep(0.1)

        bm.save()

        # Check if updated_at is updated after calling save
        self.assertNotAlmostEqual(bm.updated_at.timestamp(), initial_updated_at.timestamp(), delta=0.01)

    def test_to_dict_method(self):
        # Test the to_dict method returns a dictionary with the expected keys and values
        bm = BaseModel()
        bm_dict = bm.to_dict()

        # Check if the dictionary has the expected keys
        self.assertIn('id', bm_dict)
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)
        self.assertIn('__class__', bm_dict)

        # Check if the values are of the expected types
        self.assertIsInstance(bm_dict['id'], str)
        self.assertIsInstance(bm_dict['created_at'], str)
        self.assertIsInstance(bm_dict['updated_at'], str)
        self.assertIsInstance(bm_dict['__class__'], str)

if __name__ == '__main__':
    unittest.main()

