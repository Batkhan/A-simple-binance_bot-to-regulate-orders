Simplified Binance Futures Trading Bot (Testnet)

A simplified Python trading bot built for the Binance Futures Testnet (USDT-M).
This project demonstrates basic automated trading features such as placing market and limit orders, order tracking, and logging — designed as part of a coding challenge / job application.

✨ Features

1. Place Market and Limit orders

2. Support for BUY and SELL sides

3. Built on the Binance Futures Testnet (https://testnet.binancefuture.com)

4. Reusable bot class (BasicBot) for easy extension

5. Command-line interface (CLI) with input validation

6. Readable console output instead of raw JSON

7. Logging of all API calls, responses, and errors (bot.log)

8. Order status check after placement

📂 Project Structure
binance_bot.py   # Core trading bot logic (API wrapper class)
bot_exec.py      # CLI interface to interact with the bot
bot.log          # Log file (auto-generated when you run the bot)

🔧 Setup Instructions
1. Clone the repository
git clone https://github.com/<your-username>/binance-futures-bot.git
cd binance-futures-bot

2. Install dependencies
pip install python-binance

3. Add your Binance Testnet API keys

Edit bot_exec.py and replace:

API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"


⚠️ Keys must be generated from the Binance Futures Testnet dashboard.

▶️ Running the Bot

Run the CLI interface:

python bot_exec.py


Example run:

!!! Trading Bot Binance !!!
Enter order type (market/limit): market
Enter side (BUY/SELL): BUY
Enter symbol (e.g. BTCUSDT): BTCUSDT
Enter quantity: 0.01


Example output:

- Order Summary
   Order ID    : 123456789
   Symbol      : BTCUSDT
   Side        : BUY
   Type        : MARKET
   Status      : FILLED
   Quantity    : 0.01
   Executed    : 0.01
   Price       : 0
   Avg. Price  : 61250.00


Logs are written to bot.log:

2025-09-08 16:05:12,345 - INFO -  MARKET order placed successfully: {...}
2025-09-08 16:05:12,678 - INFO -  Checked order status: {...}

- Requirements

Python 3.8+

python-binance