import unittest
from unittest.mock import patch, MagicMock

import os
import sys
currentDirectory = os.path.dirname(os.path.realpath(__file__))
parentDirectory = os.path.dirname(currentDirectory)
sys.path.append(parentDirectory)
from loadToDB.Load import connect_to_db

class TestConnectToDb(unittest.TestCase):

    @patch('loadToDB.Load.MongoClient')
    def test_connect_to_db_success(self, mock_mongo_client):
        # Mock the return value of MongoClient
        mock_client = MagicMock()
        mock_mongo_client.return_value = mock_client

        # Call the function
        result = connect_to_db()

        # Assert that the function returns the expected values
        self.assertEqual(result, (mock_client, mock_client['NBA']))

    # Need failure test
        
if __name__ == '__main__':
    unittest.main()