import re
import sys

sys.path.append("..")
from scraper import Scraper

def isCoach(rawStat):
    """isCoach
    Checks if the record is a coach

    Args:
        rawStat (str): The unformatted player stat

    Returns:
        bool: True if the record is a coach, False otherwise
    """
    return "Head Coach" in rawStat or "Assistant Coach" in rawStat or "Trainer" in rawStat

def cleanNBAPlayerStat(playerStatRaw):
    """cleanNBAPlayerStats
    Cleans a dictionary of a players stats from an entry in the list returned from extractNBATeamStats(). 

    Args:
        playerStatRaw (str): The unformatted player stat

    Returns:
        formatted_record (dict): A dictionary of cleaned player stats
    """
    cleaned = re.sub(r'<[^>]+>', '', playerStatRaw) # remove html tags and classes
    
    components = cleaned.split()
    
    if len(components) >= 10:
        formatted_record = {
        "First Name": components[0],
        "Last Name": components[1],
        "Number": components[2],
        "Position": components[3],
        "Height": components[4],
        "Weight": components[5],
        "Date of Birth": components[7:9],
        "Age": components[10],
        "Experience": components[11],        
        }
        print("Success: " + formatted_record)
        return formatted_record      
    
    print("Error: " + playerStatRaw)
    return None  
    
def cleanNBACoachStat(coachStatRaw):
    """cleanNBACoachStat
    Returns a dictionary of cleaned coach stats from an entry in the list returned from extractNBATeamStats() that is confirmed to be a coach

    Args:
        coachStatRaw (str): The unformatted coach stat

    Returns:
        formatted_record (dict): A dictionary of cleaned coach stats
    """
    
    
    
    
    
    
    