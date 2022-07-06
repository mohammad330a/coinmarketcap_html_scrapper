from html.parser import HTMLParser


class CoinMarketCapHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()

        self.cur_coin = dict()
        self.top_gainers = list()
        self.top_losers = list()
        self.result = list()

        self.is_section = False
        self.is_header = False
        self.is_losers = False
        self.is_winners = False
        self.is_coin = False
        self.is_data = False
        self.data_num = 0

    def handle_starttag(self, tag, attrs):
        # print("start", tag, attrs)

        if ('class', 'uikit-col-md-8 uikit-col-sm-16') in attrs:
            self.is_section = True
        if self.is_section and tag.strip() == 'tr':
            self.is_coin = True
        if self.is_coin and tag.strip() == 'td':
            self.is_data = True
        if self.is_section and tag.strip() == 'thead':
            self.is_header = True

    def handle_endtag(self, tag):
        # print("end: ", tag)

        if self.is_section and tag.strip() == 'tr':
            self.is_coin = False
            if self.is_header:
                pass
            elif self.is_winners:
                self.top_gainers.append(self.cur_coin)
            elif self.is_losers:
                self.top_losers.append(self.cur_coin)
            self.cur_coin = dict()
            self.data_num = 0

        if tag.strip() == 'table':
            self.is_section = False
            self.is_winners = False
            self.is_losers = False

        if self.is_coin and tag.strip() == 'td':
            self.is_data = False

        if self.is_section and tag.strip() == 'thead':
            self.is_header = False

    def handle_data(self, data):
        if self.is_data:
            self.data_num += 1
            if self.data_num == 1:
                self.cur_coin['id'] = data.strip()
            if self.data_num == 2:
                self.cur_coin['name'] = data.strip()
            if self.data_num == 4:
                self.cur_coin['code'] = data.strip()
            if self.data_num == 5:
                self.cur_coin['price'] = data.strip()
            if self.data_num == 6:
                self.cur_coin['24h'] = data.strip()
            if self.data_num == 8:
                self.cur_coin['volume'] = data.strip()

        if self.is_section and data.strip() == 'Top Gainers':
            self.is_winners = True

        if self.is_section and data.strip() == 'Top Losers':
            self.is_losers = True
