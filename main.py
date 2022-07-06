from scrapper.HTMLHandler import CoinMarketCapHTMLParser
from scrapper.scrapper import Scrapper

if __name__ == '__main__':
    # get_page_rows("https://coinmarketcap.com/gainers-losers/")
    parser = CoinMarketCapHTMLParser()
    scrapper = Scrapper(parser, 'https://coinmarketcap.com/gainers-losers/')
    scrapper.scrap()
    print(scrapper.result)
