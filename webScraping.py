import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        req = urllib.request.urlopen(self.site)
        html = req.read()
        fr = open("html.txt", "w")
        fr.write(str(html))
        fr.close()

sb1 = Scraper("https://pypi.org/project/beautifulsoup4/")
sb1.scrape()
