import csv
import requests
import logging

STOOQ_API_URL = "https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv"
STOOQ_QUOTE_INDEX = "Close"

logger = logging.getLogger(__name__)


class CommandError(Exception):
    pass

class StockQuoteHandler:
    def handle(self, command):
        if not command:
            raise CommandError("Invalid command: {}".format(command))

        stock_quote = self.get_stock_quote(command)
        if not stock_quote or stock_quote == "N/A":
            raise CommandError(f"Stock quote not found: {command}")

        return f"{command} quote is {stock_quote} per share."

    def get_stock_quote(self, stock_code):
        api_url = STOOQ_API_URL.format(stock_code=stock_code)
        response = requests.get(api_url)
        formatted_result = self.handle_csv_stock_data(response.iter_lines())
        logger.info(formatted_result)
        return formatted_result.get(STOOQ_QUOTE_INDEX)

    def handle_csv_stock_data(self, csv_iterator):
        decoded_content = [content.decode("utf-8") for content in csv_iterator]
        try:
            header, data = decoded_content[0].split(","), decoded_content[1].split(",")
        except IndexError as index_error:
            logger.error("Cannot decode csv content. Reason: %s", index_error)
            return {}
        else:
            return dict(zip(header, data))
