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
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is  None:
                continue
            if "html" in url:
                print("\n" + url)


sb1 = Scraper("https://news.google.com/")
sb1.scrape()
