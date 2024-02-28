# main.py

import signal
import sys
import time

from scraper import Scraper
from linkGetter import LinkGetter

def shutdownHandler(signum, frame):
    print("Shutting down...")
    
    # TODO: clean up here
    
    sys.exit(0)

def main():
    # Register the shutdown handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, shutdownHandler)
    
    # pageHtml = Scraper.scrapePage("https://www.nba.com/stats/history")
    
    teamNumbers = LinkGetter.getNBATeams("https://www.nba.com/teams")
    
    print(teamNumbers)
    
    try: 
        while True:
            print("Running...")
            time.sleep(5)
    except KeyboardInterrupt:
        pass # Ctrl+C pressed

if __name__ == "__main__":
    main()