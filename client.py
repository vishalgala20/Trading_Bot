import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:

    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None):

        try:

            if order_type == "MARKET":

                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )

            elif order_type == "STOP_LIMIT":

                 order = self.client.futures_create_order(
                 symbol=symbol,
                 side=side,
                 type="STOP",
                 quantity=quantity,
                 price=price,
                 stopPrice=price,
                 timeInForce="GTC"
             )

            return order

        except Exception as e:
            return {"error": str(e)}