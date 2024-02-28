import re
import sys
sys.path.append("..")
from scraper import Scraper

url = "https://www.nba.com/teams"

def getNBATeams(url): 
    page = Scraper.scrapePage(url)
    
    pattern = r'href="/stats/team/(\d+)"'
        
    teams = re.findall(pattern, page)    
    
    return teams

getNBATeams(url)