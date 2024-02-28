# main.py

import signal
import sys
import time

from scraper import Cleaner
from scraper import Scraper
from linkGetter import LinkGetter
from loadToDB import Load

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
        
    # iterate through team numbers and scrape team stat pages
    for teamNumber in teamNumbers:
        
        # append team number to url
        teamURL = "https://www.nba.com/stats/team/" + teamNumber + "?Season=2022-23"
        
        playerStats = Scraper.extractNBATeamStats(teamURL)
        
        playersLoaded = 0
        staffLoaded = 0
        
        for rawStat in playerStats:
            cleaned = Cleaner.cleanNBAStat(rawStat)
            
            if (Cleaner.isCoach(rawStat)):
                # TODO: load coach stats to DB
                staffLoaded += 1
            
            if (not Cleaner.isCoach(rawStat)):
                # TODO: load player stats to DB
                playersLoaded += 1
                
        print("Loaded " + str(playersLoaded) + " players and " + str(staffLoaded) + " staff")


    
    try: 
        while True:
            print("Running...")
            time.sleep(5)
    except KeyboardInterrupt:
        pass # Ctrl+C pressed

if __name__ == "__main__":
    main()