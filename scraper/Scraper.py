from urllib.request import urlopen

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

