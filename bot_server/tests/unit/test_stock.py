from unittest import TestCase
from bot_server.stock import StockQuoteHandler


class TestStock(TestCase):

    def setUp(self):
        self.handler = StockQuoteHandler()

    def test_handle_stock_csv_data(self):
        csv_data = (
            b'Symbol,Date,Time,Open,High,Low,Close,Volume',
            b'AAPL.US,2021-01-11,22:00:04,129.19,130.17,128.5,128.98,100620880'
        )
        result = self.handler.handle_csv_stock_data(csv_data)
        self.assertEqual(result, {
            "Symbol": "AAPL.US",
            "Date": "2021-01-11",
            "Time": "22:00:04",
            "Open": "129.19",
            "High": "130.17",
            "Low": "128.5",
            "Close": "128.98",
            "Volume": "100620880"
        })
