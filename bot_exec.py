from binance_bot import BasicBot
import logging

# Paste your keys here
API_KEY = "e017a1788b2c03577f15e6db96619ec536d0d714ff6aa6c96ebf7d1058fd9aeb"
API_SECRET = "4cec931e108a47cc432f1204e6dbd86e1ce1b0f6817f2535983143a4ecb97d0a"

bot = BasicBot(API_KEY, API_SECRET, testnet=True)

def format_order(order):
    """Format order details for console output"""
    if not order or "error" in order:
        return f"❌ Error: {order.get('error', 'Unknown error')}"
    
    return (
        f"\n📌 Order Summary\n"
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

# --- Input validation ---
order_type = input("Enter order type (market/limit): ").strip().lower()
if order_type not in ["market", "limit"]:
    print("❌ Invalid order type. Choose 'market' or 'limit'.")
    logging.warning("User entered invalid order type: %s", order_type)
    exit()

side = input("Enter side (BUY/SELL): ").strip().upper()
if side not in ["BUY", "SELL"]:
    print("❌ Invalid side. Choose 'BUY' or 'SELL'.")
    logging.warning("User entered invalid side: %s", side)
    exit()

symbol = input("Enter symbol (e.g. BTCUSDT): ").strip().upper()
try:
    quantity = float(input("Enter quantity: ").strip())
    if quantity <= 0:
        raise ValueError
except ValueError:
    print("❌ Invalid quantity. Must be a positive number.")
    logging.warning("User entered invalid quantity")
    exit()

price = None
if order_type == "limit":
    try:
        price = float(input("Enter price: ").strip())
        if price <= 0:
            raise ValueError
    except ValueError:
        print("❌ Invalid price. Must be a positive number.")
        logging.warning("User entered invalid price")
        exit()

# --- Place order ---
result = bot.place_order(order_type, side, symbol, quantity, price)
print(format_order(result))

# --- Order status check ---
if isinstance(result, dict) and "orderId" in result:
    status = bot.check_order_status(symbol, result["orderId"])
    print("\n📊 Order Status Update:")
    print(format_order(status))
