import re
import sys

sys.path.append("..")
from scraper import Scraper

def cleanNBATeamStats(teamURL):
    """cleanNBATeamStats
    Returns a list of cleaned team stats from the NBA team stats page

    Args:
        teamURL (str): The url of the NBA team stats page

    Returns:
        list: A list of cleaned team stats. Formatted as `<First Name> <Last Name> "#"<Number>, <Position>, <Height> <Weight in lbs> "lbs" <Date of birth as 'MMM DD, YYYY'> <Age> <Experience> <School> <How Aquired>`
    """
    
    print(teamURL)
    teamHTML = Scraper.scrapeDynamicPage(teamURL, 'table') # return html of team stats
    
    # scrape each <tr> to </tr> tag using regex
    pattern = r'<tr>(.*?)</tr>'
    teamStats = re.findall(pattern, teamHTML, re.DOTALL) # find all matches and store in list
    
    # DEBUG: write to file
    with open("teamStats.txt", "w") as file:
        file.write(str(teamStats))
    
    return teamStats

def cleanNBAPlayerStats(playerStatList):
    """cleanNBAPlayerStats
    Cleans a list of player stats from cleanNBATeamStats(). 

    Args:
        playerStatList (list): The list of player stats to clean

    Returns:
        list: A list of dictionaries of cleaned player stats 
    """
    
    
    
    
    