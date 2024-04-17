import unittest
from unittest.mock import patch

import os
import sys
currentDirectory = os.path.dirname(os.path.realpath(__file__))
parentDirectory = os.path.dirname(currentDirectory)
sys.path.append(parentDirectory)
from linkGetter.LinkGetter import getNBATeams

class TestGetNBATeams(unittest.TestCase):

    @patch('linkGetter.LinkGetter.Scraper.scrapePage')
    def test_valid_url(self, mock_scrapePage):
        """
        Test that a valid url returns a list of team IDs.

        Args:
            mock_scrapePage (MagicMock): Mock function for the scrapePage method of the Scraper class.
        """
        mock_scrapePage.return_value = '<a href="/stats/team/1">Team 1</a><a href="/stats/team/2">Team 2</a>'
        result = getNBATeams("https://example.com")
        self.assertEqual(result, ['1', '2'],
                         "The list of team IDs should match the IDs in the links on the page.")

    @patch('linkGetter.LinkGetter.Scraper.scrapePage')
    def test_invalid_url(self, mock_scrapePage):
        """
        Test that an invalid url returns an empty list of team IDs.

        Args:
            mock_scrapePage (MagicMock): Mock function for the scrapePage method of the Scraper class.
        """
        mock_scrapePage.return_value = ''
        result = getNBATeams("invalid_url")
        self.assertEqual(result, [],
                         "An empty list of team IDs should be returned for an invalid URL.")
        self.assertEqual(result, [])

    @patch('linkGetter.LinkGetter.Scraper.scrapePage')
    def test_no_team_links(self, mock_scrapePage):
        """
        Test that a page with no links to NBA team pages returns an empty list of team IDs.

        Args:
            mock_scrapePage (MagicMock): Mock function for the scrapePage method of the Scraper class.
        """
        mock_scrapePage.return_value = '<a href="/other/link">Other Link</a>'
        result = getNBATeams("https://example.com")
        self.assertEqual(result, [],
                         "An empty list of team IDs should be returned if no links to team pages are found on the page.")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()