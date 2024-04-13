from yahoo_fin import stock_info
import time

brands = input("enter the company: ")

while True:
    price = stock_info.get_live_price(brands)
    print(price)

    if price > 1500:
        print("Sell")

    elif price > 2700:
        print("Invest")

    elif price < 5000:
        print("profit")

    time.sleep(10)
