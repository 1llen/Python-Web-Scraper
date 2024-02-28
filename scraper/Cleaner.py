import re
import sys

sys.path.append("..")
from scraper import Scraper

def cleanNBATeamStats(teamURL):
    
    print(teamURL)
    teamHTML = Scraper.scrapeDynamicPage(teamURL, 'table') # return html of team stats
    
    # write html to txt file
    # with open('teamHTML.txt', 'w') as f:
    #     f.write(teamHTML)
    #     f.close()
    
    print(teamHTML)
    
    # scrape each <tr> to </tr> tag using regex
    pattern = r'<tr>(.*?)</tr>'
    teamStats = re.findall(pattern, teamHTML, re.DOTALL)    
    
    print(teamStats)
    
    return teamStats
    
    
    
    
    