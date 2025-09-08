from binance import Client
from binance.exceptions import BinanceAPIException
import logging

# Setup logging
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        if testnet:
            # Force futures testnet base URL
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi/v1/'
        logging.info("Initialized BasicBot (Testnet=%s)", testnet)

    def place_order(self, order_type, side, symbol, quantity, price=None):
        """Place a market or limit order"""
        try:
            if order_type.lower() == "market":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="MARKET",
                    quantity=quantity
                )
            elif order_type.lower() == "limit":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side.upper(),
                    type="LIMIT",
                    timeInForce="GTC", 
                    quantity=quantity,
                    price=price
                )
            else:
                logging.warning("Invalid order type: %s", order_type)
                return {"error": "Invalid order type! Use 'market' or 'limit'."}

            logging.info(" %s order placed successfully: %s", order_type.upper(), order)
            return order
        except BinanceAPIException as e:
            logging.error(" Error placing %s order: %s", order_type.upper(), e)
            return {"error": str(e)}

    def check_order_status(self, symbol, order_id):
        """Check order status"""
        try:
            order = self.client.futures_get_order(
                symbol=symbol,
                orderId=order_id
            )
            logging.info(" Checked order status: %s", order)
            return order
        except Exception as e:
            logging.error(" Error checking order status: %s", e)
            return {"error": str(e)}
