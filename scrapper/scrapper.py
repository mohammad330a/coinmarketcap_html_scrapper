import requests


class Scrapper:
    def __init__(self, parser, web_url):
        self.result = None
        self.parser = parser
        self.web_url = web_url

        self.read_config()
        self.boot()

    def read_config(self):
        return

    def boot(self):
        return

    def scrap(self):
        html_scrap = requests.get(self.web_url).text
        self.parser.feed(html_scrap)
        self.result = {
            "top_gainers": self.parser.top_gainers,
            "top_losers": self.parser.top_losers
        }
