# Binance Futures Trading Bot

This project contains a set of CLI-based Python scripts for placing orders on the Binance USDT-M Futures Testnet, as per the assignment requirements.

It supports Market, Limit, and Stop-Limit orders, with all actions and errors logged to `bot.log`.

## Project Structure

```
/
├── src/
│   ├── client.py               # Shared API connection and logging setup
│   ├── market_orders.py        # Script for placing Market orders
│   ├── limit_orders.py         # Script for placing Limit orders
│   └── advanced/
│       └── stop_limit_orders.py 
├── .env                        # Stores API credentials 
├── bot.log                     # Log file (auto-generated)
├── report.md                   
└── README.md                   
```

## Setup and Installation

### Prerequisites

- Python 3.8+
- A Binance Futures Testnet account and API Keys.

### Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/AvinashK47/binance-trading-bot
   cd binance-trading-bot
   ```

2. **Set up a Virtual Environment (Recommended):**

   ```sh
   # For Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```sh
   pip install python-binance python-dotenv
   ```

4. **Configure API Credentials:**
   Create a file named `.env` in the root directory of the project. Add your Binance Testnet API key and secret to this file:
   ```
   BINANCE_API_KEY=your_testnet_api_key_here
   BINANCE_API_SECRET=your_testnet_api_secret_here
   ```

## Usage

All commands are run from the root of the project directory.

### To Place a Market Order

**Syntax:** `python src/market_orders.py <SYMBOL> <SIDE> <QUANTITY>`

**Example:**

```sh
python src/market_orders.py BTCUSDT BUY 0.001
```

### To Place a Limit Order

**Syntax:** `python src/limit_orders.py <SYMBOL> <SIDE> <QUANTITY> <PRICE>`

**Example:**

```sh
python src/limit_orders.py ETHUSDT SELL 0.1 3000
```

### To Place a Stop-Limit Order

**Syntax:** `python src/advanced/stop_limit_orders.py <SYMBOL> <SIDE> <QUANTITY> <PRICE> <STOP_PRICE>`

**Example:**

```sh
python src/advanced/stop_limit_orders.py BTCUSDT SELL 0.001 59950 60000
```
