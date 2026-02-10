import sys
import os
import argparse
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from client import setup_client
from binance.client import Client
from binance.exceptions import BinanceAPIException

if __name__ == "__main__":
  
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    log_path = os.path.join(project_root, 'bot.log')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler(log_path, mode='a'), logging.StreamHandler()])

    parser = argparse.ArgumentParser(description='Place a STOP-LIMIT order on Binance Futures.')
    parser.add_argument('symbol', type=str, help='Trading symbol')
    parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order side')
    parser.add_argument('quantity', type=float, help='Order quantity')
    parser.add_argument('price', type=float, help='The price of the limit order once triggered')
    parser.add_argument('stop_price', type=float, help='The price that triggers the limit order')
    args = parser.parse_args()

    client = setup_client()
    if client:
        try:
            logging.info(f"Attempting to place STOP-LIMIT {args.side} order for {args.quantity} {args.symbol} with stop {args.stop_price} and price {args.price}...")
            order = client.futures_create_order(
                symbol=args.symbol,
                side=args.side.upper(),
                type='STOP',
                timeInForce='GTC',
                quantity=args.quantity,
                price=str(args.price),
                stopPrice=str(args.stop_price)
            )
            logging.info(f"Successfully placed STOP-LIMIT order. Response: {order}")
            print("\n--- Order Execution Successful ---")
            print(order)
            print("---------------------------------")
        except BinanceAPIException as e:
            logging.error(f"Binance API Error placing stop-limit order: {e}")
            print(f"\n--- Order Execution Failed: {e} ---")

