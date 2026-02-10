import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv

def setup_client():
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dotenv_path = os.path.join(project_root, '.env')
    load_dotenv(dotenv_path=dotenv_path)
    
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    if not api_key or not api_secret:
        logging.error("CRITICAL: BINANCE_API_KEY and BINANCE_API_SECRET must be set in the .env file.")
        return None

    try:
        client = Client(api_key, api_secret, testnet=True)
        
        client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        
        client.futures_account()
        logging.info("Successfully connected to Binance Futures Testnet.")
        return client
    except (BinanceAPIException, BinanceRequestException) as e:
        logging.error(f"API Connection Error: {e}")
        return None