from urllib.request import urlopen # for static web scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrapePage(url):
    """scrapePage
    returns entire html of page at url

    Args:
        url (str): The url of the page to scrape

    Returns:
        str: The html of the page
    """
    page = urlopen(url)
    
    htmlPage = page.read()
    htmlDecoded = htmlPage.decode("utf-8")
    
    return htmlDecoded

def scrapeDynamicPage(url, waitTag):
    """scrapeDynamicPage
    returns html of page at url after waiting for "waitTag" to load. Used for pages with client side javascript. Uses selenium webdriver to emulate browser.

    Args:
        url (str): The url of the page to scrape
        waitTag (str): The html tag to wait for to load before scraping

    Returns:
        str: The html of the page
    """
    
    # TODO: "quietly" open the browser
    
    driver = webdriver.Chrome()
    driver.get(url)
    
    tag = "//" + waitTag
    
    try: 
        # wait for </table> tag to load
        tr_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, tag))
        )
        
        # DEBUG
        print(tr_element.text)
        
        return driver.page_source
        
    except Exception as e:
        print("Error: " + str(e))
        
    finally:
        driver.quit()
        

