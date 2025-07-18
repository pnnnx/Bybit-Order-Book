import sys
import time
import os

from pybit.unified_trading import HTTP

session = HTTP(testnet=False)

def clear_console():
    os.system('clear')

try:
    while True:
        
        ticker = session.get_tickers(category="linear", symbol="BTCUSDT")
        last_price = float(ticker['result']['list'][0]['lastPrice'])
        orderbook = session.get_orderbook(category="linear", symbol="BTCUSDT", limit=20)
        clear_console()
        
        bid = float(ticker['result']['list'][0]['bid1Price'])
        ask = float(ticker['result']['list'][0]['ask1Price'])
        spread = ask - bid
        spread = str(spread)[0:6]

        bid_ob = list(orderbook['result']['b'])
        ask_ob = list(orderbook['result']['a'])[::-1]


        print(f'price:\033[1m{last_price}\033[0m')
        print("==============================")
        print(f'spread:{spread}')
        print("==============================")
        width = 14
        for j in ask_ob:
            if float(j[1]) >= 1:
                print(f'|\033[31m{j[0]:<{width}}\033[0m\033[34m{j[1]:>{width}}\033[0m|')
            else:
                print(f'|\033[31m{j[0]:<{width}}{j[1]:>{width}}\033[0m|')
        print("==============================")
        for i in bid_ob:
            if float(i[1]) >= 1:
                print(f'|\033[32m{i[0]:<{width}}\033[0m\033[34m{i[1]:>{width}}\033[0m|')
            else:
                print(f'|\033[32m{i[0]:<{width}}{i[1]:>{width}}\033[0m|')
        time.sleep(1/10)
except KeyboardInterrupt:
    print("\nExit.")
    sys.exit(0)