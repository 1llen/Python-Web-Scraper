import unittest
from unittest.mock import patch, MagicMock
import pymongo
import matplotlib.pyplot as plt
import heapq
from io import StringIO

import os
import sys
currentDirectory = os.path.dirname(os.path.realpath(__file__))
parentDirectory = os.path.dirname(currentDirectory)
sys.path.append(parentDirectory)
from display.HeightStats import heightStatistics

class TestHeightStatistics(unittest.TestCase):

    def test_average_height_output(self):
        # Expected tallest player
        expected_output_start = "['Boban Marjanovic',"
        
        # Run the heightStatistics function and capture the output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            heightStatistics()
            
            # Get the output from the fake output stream
            output = fake_out.getvalue().strip()
            
            # Check that the output starts with the expected output
            self.assertTrue(output.startswith(expected_output_start))
            
if __name__ == '__main__':
    unittest.main()
            
        
