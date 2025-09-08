from binance_bot import BasicBot
import logging
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

bot = BasicBot(API_KEY, API_SECRET, testnet=True)

def format_order(order):
    """Format order details for console output"""
    if not order or "error" in order:
        return f" Error: {order.get('error', 'Unknown error')}"
    
    return (
        f"\n Order Summary\n"
        f"   Order ID    : {order.get('orderId')}\n"
        f"   Symbol      : {order.get('symbol')}\n"
        f"   Side        : {order.get('side')}\n"
        f"   Type        : {order.get('type')}\n"
        f"   Status      : {order.get('status')}\n"
        f"   Quantity    : {order.get('origQty')}\n"
        f"   Executed    : {order.get('executedQty')}\n"
        f"   Price       : {order.get('price')}\n"
        f"   Avg. Price  : {order.get('avgPrice', 'N/A')}\n"
    )

print("!!! Trading Bot Binance !!!")

order_type = input("Enter order type (market/limit): ").strip().lower()
if order_type not in ["market", "limit"]:
    print(" Invalid order type. Choose 'market' or 'limit'.")
    logging.warning("User entered invalid order type: %s", order_type)
    exit()

side = input("Enter side (BUY/SELL): ").strip().upper()
if side not in ["BUY", "SELL"]:
    print(" Invalid side. Choose 'BUY' or 'SELL'.")
    logging.warning("User entered invalid side: %s", side)
    exit()

symbol = input("Enter symbol (e.g. BTCUSDT): ").strip().upper()
try:
    quantity = float(input("Enter quantity: ").strip())
    if quantity <= 0:
        raise ValueError
except ValueError:
    print(" Invalid quantity. Must be a positive number.")
    logging.warning("User entered invalid quantity")
    exit()

price = None
if order_type == "limit":
    try:
        price = float(input("Enter price: ").strip())
        if price <= 0:
            raise ValueError
    except ValueError:
        print(" Invalid price. Must be a positive number.")
        logging.warning("User entered invalid price")
        exit()

result = bot.place_order(order_type, side, symbol, quantity, price)
print(format_order(result))

if isinstance(result, dict) and "orderId" in result:
    status = bot.check_order_status(symbol, result["orderId"])
    print("\n Order Status Update:")
    print(format_order(status))
