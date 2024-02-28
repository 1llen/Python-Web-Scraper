from urllib.request import urlopen

def scrapePage(url):
    page = urlopen(url)
    
    htmlPage = page.read()
    htmlDecoded = htmlPage.decode("utf-8")
    
    return htmlDecoded

