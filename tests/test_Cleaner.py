import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup
from unittest.mock import MagicMock

import os
import sys
currentDirectory = os.path.dirname(os.path.realpath(__file__))
parentDirectory = os.path.dirname(currentDirectory)
sys.path.append(parentDirectory)

from scraper.Cleaner import cleanNBAPlayerStat
from scraper.Cleaner import cleanNBAPlayerAverageStats
from scraper.Cleaner import cleanNBACoachStat
from scraper.Cleaner import cleanNBAStat

class TestCleaner(unittest.TestCase):
    
    def test_cleanNBAPlayerStat(self):
        # Simulate the raw player stat HTML
        playerStatRaw = "<div>Player Name</div><div>Number</div><div>Position</div><div>Height</div><div>Weight</div><div>Date of Birth</div><div>Age</div><div>Experience</div><div>School</div>"
        # Expected cleaned player stat
        expected_result = {
            "Name": "Player Name",
            "Number": "Number",
            "Position": "Position",
            "Height": "Height",
            "Weight": "Weight",
            "Date of Birth": "Date of Birth",
            "Age": "Age",
            "Experience": "Experience",
            "School": "School"
        }
        # Call the cleanNBAPlayerStat function and assert that the result is as expected
        self.assertEqual(cleanNBAPlayerStat(playerStatRaw), expected_result)

    def test_cleanNBAPlayerAverageStats(self):
        # Simulate the raw player stat HTML
        playerStatsRaw = "<div>Player Average Stats</div>"
        # Expected cleaned player stat
        expected_result = ["Player Average Stats"]
        # Call the cleanNBAPlayerStat function and assert that the result is as expected
        self.assertEqual(cleanNBAPlayerAverageStats(playerStatsRaw), expected_result)

    def test_cleanNBACoachStat(self):
        # Simulate the raw coach stat HTML
        coachStatRaw = "<div>Coach Name</div>"
        # Expected cleaned coach stat
        expected_result = {
            "First Name": "Coach",
            "Last Name": "Name",
            "Role": ""
        }
        # Call the cleanNBACoachStat function and assert that the result is as expected
        self.assertEqual(cleanNBACoachStat(coachStatRaw), expected_result)

    def test_cleanNBAStat_for_player(self):
        # set isCoach to False
        isCoach = MagicMock(return_value=False)
        # Simulate the raw player stat HTML
        playerOrCoachStatRaw = "<div>Player Name</div><div>Number</div><div>Position</div><div>Height</div><div>Weight</div><div>Date of Birth</div><div>Age</div><div>Experience</div><div>School</div>"
        # Expected cleaned player stat
        expected_result = {
            "Name": "Player Name",
            "Number": "Number",
            "Position": "Position",
            "Height": "Height",
            "Weight": "Weight",
            "Date of Birth": "Date of Birth",
            "Age": "Age",
            "Experience": "Experience",
            "School": "School"
        }
        # Call the cleanNBAStat function and assert that the result is as expected
        self.assertEqual(cleanNBAStat(playerOrCoachStatRaw), expected_result)
        

if __name__ == '__main__':
    unittest.main()