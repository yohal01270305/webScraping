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
        url_list = []
        for tag in sp.find_all("a"):
            print(tag)
            url = tag.get("href")
            if url is  None:
                continue
            if "html" in url:
                url_list.append(url)

        print("--------------------------------------------------")
        for l in url_list:
            print(l)

sUrl = "https://www.yahoo.co.jp/"
sb1 = Scraper(sUrl)
sb1.scrape()
