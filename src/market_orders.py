import argparse
import logging
import os
from client import setup_client
from binance.client import Client
from binance.exceptions import BinanceAPIException

if __name__ == "__main__":
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_path = os.path.join(project_root, 'bot.log')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler(log_path, mode='a'), logging.StreamHandler()])

    parser = argparse.ArgumentParser(description='Place a MARKET order on Binance Futures.')
    parser.add_argument('symbol', type=str, help='Trading symbol (e.g., BTCUSDT)')
    parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('quantity', type=float, help='Order quantity')
    args = parser.parse_args()

    client = setup_client()
    if client:
        try:
            logging.info(f"Attempting to place MARKET {args.side} order for {args.quantity} {args.symbol}...")
            order = client.futures_create_order(
                symbol=args.symbol,
                side=args.side.upper(),
                type=Client.ORDER_TYPE_MARKET,
                quantity=args.quantity
            )
            logging.info(f"Successfully placed MARKET order. Response: {order}")
            print("\n--- Order Execution Successful ---")
            print(order)
            print("---------------------------------")
        except BinanceAPIException as e:
            logging.error(f"Binance API Error placing market order: {e}")
            print(f"\n--- Order Execution Failed: {e} ---")