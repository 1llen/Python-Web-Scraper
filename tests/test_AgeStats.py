import unittest
from io import StringIO
from unittest.mock import patch

import os
import sys
currentDirectory = os.path.dirname(os.path.realpath(__file__))
parentDirectory = os.path.dirname(currentDirectory)
sys.path.append(parentDirectory)
from display.AgeStats import ageStatistics

class TestAgeStatistics(unittest.TestCase):

    def test_average_age_output(self):
        expected_output_start = "The average age out of"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            ageStatistics()
            output = fake_out.getvalue().strip()
            # Check that the output starts with the expected output
            self.assertTrue(output.startswith(expected_output_start))
            # Check that the output does not contain a sole 0 for any number
            self.assertNotIn(" 0 ", output)

if __name__ == '__main__':
    unittest.main()