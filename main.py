# main.py

import signal
import sys
import time

from scraper import Cleaner
from scraper import Scraper
from linkGetter import LinkGetter
from loadToDB.Load import load_player_to_db, load_coach_to_db
#from Load import load_player_to_db, load_coach_to_db

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
        
        teamName = Scraper.extractNBATeamName(teamURL)
        
        playersLoaded = 0
        staffLoaded = 0
        
        for rawStat in playerStats:
            cleaned = Cleaner.cleanNBAStat(rawStat)
            
            if Cleaner.isCoach(rawStat):
                coach_data = cleaned
                load_coach_to_db(coach_data, teamName)
                staffLoaded += 1

            if not Cleaner.isCoach(rawStat):
                player_data = cleaned
                load_player_to_db(player_data, teamName)
                playersLoaded += 1
            
        # print(f"From {teamName}: Loaded {playersLoaded} players and {staffLoaded} staff")

        print("From " + str(teamName) + ": Loaded " + str(playersLoaded) + " players and " + str(staffLoaded) + " staff")   
        
            
    try: 
        while True:
            print("Running...")
            time.sleep(5)
    except KeyboardInterrupt:
        pass # Ctrl+C pressed

if __name__ == "__main__":
    main()