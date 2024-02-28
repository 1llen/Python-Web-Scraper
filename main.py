# main.py

import signal
import sys
import time

from scraper import Cleaner
from linkGetter import LinkGetter

def shutdownHandler(signum, frame):
    print("Shutting down...")
    
    # TODO: clean up here
    
    sys.exit(0)

def main():
    # Register the shutdown handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, shutdownHandler)
    
    print("Starting...")
    print("Press Ctrl+C to quit...")
    
    teamNumbers = LinkGetter.getNBATeams("https://www.nba.com/teams")
    print(teamNumbers)
    
    # iterate through team numbers and scrape team stat pages
    for teamNumber in teamNumbers:
        
        # append team number to url
        teamURL = "https://www.nba.com/stats/team/" + teamNumber
        
        playerStats = Cleaner.cleanNBATeamStats(teamURL)
        
        # TODO: add function to Cleaner.py for cleaning string into dictionary for uploading to DB
        
        # TODO: add function to Load.py for loading player stats to DB

        
        
    
    
    
    try: 
        while True:
            print("Running...")
            time.sleep(5)
    except KeyboardInterrupt:
        pass # Ctrl+C pressed

if __name__ == "__main__":
    main()