# main.py

import signal
import sys
import time

from scraper import Cleaner
from scraper import Scraper
from linkGetter import LinkGetter
from loadToDB.Load import load_player_to_db, load_coach_to_db, load_URL_to_db, check_URL_in_db
from display import AgeStats
from display import HeightStats
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
            
    # Main Menu
    while True:
        print("Temporary CLI Main Menu:")
        option = input("Select an option: \n1. Scraper \n2. Viewer \n3. Exit\n")
        if option == "1":
            scraperOption = input("Select a scraper: \n1. NBA \n2. LinkedIn [TO DO]\n3. Back to main menu\n")
            if scraperOption == "1":
                typeOption = input("Select a type: \n1. Player data \n2. Player Stats \n3. Back to main menu\n")
                if typeOption == "1":
                    NBAScraper()
                elif typeOption == "2":
                    NBAPlayerStats()
            elif scraperOption == "2":
                print("TODO: LinkedIn Scraper")
                pass
            elif scraperOption == "3":
                pass
            else:
                print("Invalid option. Please try again.") 
            
        elif option == "2":
            viewOption = input("Select a analysis: \n1. Player age \n2. Player height (TODO) \n3. Back to main menu\n")
            if viewOption == "1":
                AgeStats.ageStatistics()
            elif viewOption == "2":
                HeightStats.heightStatistics()
            elif viewOption == "3":
                pass
            else:
                print("Invalid")
        elif option == "3":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid option. Please try again.") 
    
    try: 
        while True:
            print("Running...")
            time.sleep(5)
    except KeyboardInterrupt:
        pass # Ctrl+C pressed
    
def NBAScraper(year="2023"):
    """
    Scrape NBA player and coach data for the specified year.
    TODO: Move to seperate file

    Args:
        year (str, optional): _description_. Defaults to "2023".
    """
    teamNumbers = LinkGetter.getNBATeams("https://www.nba.com/teams")
        
    # Modify year 
    startYear = str(int(year) - 1)
    endYear = year[-2:]
    
    # iterate through team numbers and scrape team stat pages
    for teamNumber in teamNumbers:
        
        # append team number and year to url
        teamURL = "https://www.nba.com/stats/team/" + teamNumber + "?Season=" + startYear + "-" + endYear
        
        # Check if URL has already been loaded for memoization; returns true if it exists in DB already
        if (check_URL_in_db(teamURL)):
            # go to next team
            continue
        
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

        # load url to db
        load_URL_to_db(teamURL)

        # Console logging
        print("From " + str(teamName) + ": Loaded " + str(playersLoaded) + " players and " + str(staffLoaded) + " staff \n")   
        
def NBAPlayerStats(year="2023", seasonType = "Regular+Season", seasonSegment = "All"):
    """
    Scrape NBA player and coach data for the specified year.
    TODO: Move to seperate file

    Args:
        year (str, optional): _description_. Defaults to "2023".
        seasonType (str, optional): _description_. Defaults to "Regular+Season".
        seasonSegment (str, optional): _description_. Defaults to "All".
    """
    teamNumbers = LinkGetter.getNBATeams("https://www.nba.com/teams")
        
    # Modify year 
    startYear = str(int(year) - 1)
    endYear = year[-2:]
    
    # Modify season segment
    if seasonSegment == "All":
        seasonSegment = ""
    # TODO: Implement other season segments and types
    
    for teamNumber in teamNumbers:
        teamURL = "https://www.nba.com/stats/team/" + teamNumber + "/players-traditional?Season=" + startYear + "-" + endYear + "&SeasonType=" + seasonType
        
        if seasonSegment != "":
            teamURL = teamURL + "&SeasonSegment=" + seasonSegment

        # Console logging
        print(teamURL)

        # Check if URL has already been loaded for memoization; returns true if it exists in DB already
        if (check_URL_in_db(teamURL)):
            # go to next team in for loop
            continue

        # Extract team stat pages
        playerStats = Scraper.extractNBAPlayerStats(teamURL)
        
        for rawStat in playerStats:
            cleaned = Cleaner.cleanNBAPlayerAverageStats(rawStat)
            
            # TODO: Insert into MongoDB (WITH YEAR)
            
            # Console logging
            print("Loaded player: " + str(cleaned["player"]) + " with " + str(cleaned["gp"]) + " games played and " + str(cleaned["pts"]) + " points")
            
        
            
        
    
    
        
def NBAViewer():
    # TODO:
    # Call DB function for selecting teams
    # Client should be able to select a team
    # Call DB function for selecting players for that team
    
    pass

if __name__ == "__main__":
    main()