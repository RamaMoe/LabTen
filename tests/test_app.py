import unittest
from app import greet
import os
import sys

# Add the project root (folder that contains app.py) to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class TestApp(unittest.TestCase):


    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
