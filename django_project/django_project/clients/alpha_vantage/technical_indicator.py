from alpha_vantage.techindicators import TechIndicators
import json

from django_project.clients.alpha_vantage import constants

class TechIndicatorClient(object):

    def __init__(self, index=None):
        self.ti = TechIndicators(constants.ALPHA_VANTAGE_API_KEY)
        self.index = index

    def get_full_code(self, stock_code):
        if self.index:
            return stock_code + "." + self.index
        else:
            return stock_code

    def get_macd(self, stock_code):
        stock_code = self.get_full_code(stock_code)
        score = self.ti.get_macd(stock_code, interval=constants.INTERVAL_60MIN,
                                         series_type=constants.SERIES_TYPE_CLOSE)

        return score

    def get_rsi(self, stock_code):
        stock_code = self.get_full_code(stock_code)
        score = self.ti.get_rsi(stock_code, interval=constants.INTERVAL_60MIN,
                                        series_type=constants.SERIES_TYPE_CLOSE)

        return score

    def get_stoch(self, stock_code):
        stock_code = self.get_full_code(stock_code)
        score = self.ti.get_stoch(stock_code, interval=constants.INTERVAL_60MIN)

        return score

    def get_stochrsi(self, stock_code):
        stock_code = self.get_full_code(stock_code)
        score = self.ti.get_stochrsi(stock_code, interval=constants.INTERVAL_60MIN)

        return score

    def get_last_value(self, indicator_score):
        last_key = list(indicator_score[0].keys())[0]
        last_score = indicator_score[0][last_key]

        return json.dumps(last_score)