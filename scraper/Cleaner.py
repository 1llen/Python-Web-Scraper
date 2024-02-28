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
        list: A list of cleaned team stats
    """
    
    print(teamURL)
    teamHTML = Scraper.scrapeDynamicPage(teamURL, 'table') # return html of team stats
    
    # scrape each <tr> to </tr> tag using regex
    pattern = r'<tr>(.*?)</tr>'
    teamStats = re.findall(pattern, teamHTML, re.DOTALL) # find all matches and store in list
    
    return teamStats
    
    
    
    
    