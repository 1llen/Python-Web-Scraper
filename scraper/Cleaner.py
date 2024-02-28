import re
# from bs4 import BeautifulSoup
import sys

sys.path.append("..")
from scraper import Scraper

def cleanNBATeamStats(teamURL):
    
    print(teamURL)
    teamHTML = Scraper.scrapePage(teamURL) # return html of team stats
    
    # write html to txt file
    with open('teamHTML.txt', 'w') as f:
        f.write(teamHTML)
        f.close()
    
    print(teamHTML)
    
    # scrape each <tr> to </tr> tag using regex
    pattern = r'<tr>(.*?)</tr>'
    teamStats = re.findall(pattern, teamHTML, re.DOTALL)
    
    # soup = BeautifulSoup(teamHTML, 'html.parser')
    # teamStats = soup.find_all('tr')
    
    
    print(teamStats)
    
    return teamStats
    
    
    
    
    