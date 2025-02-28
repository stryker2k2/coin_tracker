from coinbase.rest import RESTClient
import json
import uuid
import os

client = RESTClient(key_file="./keys/cdp_api_key.json")

# Get Accounts
def get_accts():
    accounts = client.get_accounts()
    os.makedirs("output/accounts", exist_ok=True)
    filepath = "./output/accounts/accounts.json"
    with open(filepath, "w") as f:
        json.dump(accounts.to_dict(), f, indent=4)
    print(f"\nJSON Output: {filepath}")

# Get Account Amount
def get_assets():
    accounts = client.get_accounts()
    print("\nWallet")
    for acct in accounts.accounts:
        if float(acct.available_balance['value']) > 0:
            if acct.currency == "USDC":
                print(f"{acct.currency}: {float(acct.available_balance['value']):.2f}")
            else:
                product = client.get_product(f"{acct.currency}-USDC")
                print(f"{acct.currency}: {float(acct.available_balance['value']):.2f} (${(float(product.price) * float(acct.available_balance['value'])):.2f})")

# Get Product & Print Price
def get_stock_price():
    my_products = ["TRUMP-USDC", "BTC-USDC", "XRP-USDC", "MORPHO-USDC", "ETH-USDC"]
    product = client.get_product(my_products[4])
    print("\nMarket")
    print(f"{product.product_id}: ${product.price} / coin")
    os.makedirs("output/products", exist_ok=True)
    with open(f"./output/products/{product.product_id}.json", "w") as f:
        json.dump(product.to_dict(), f, indent=4)

# Buy Coin(s)
def buy_coins():
    order_id = str(uuid.uuid4())
    response = input("\nDo you want to make a purchase (y/n)? ")
    if response != "y":
        print("\nPurchase canceled\n")
        return
    product = input("\nWhat stock do you want to purchase (ex: BTC-USDC)? ")
    response = input(f"\nHow many {product} do you want to buy (in Dollars)? ")
    order_size = str(response)
    response = input(f"\nDo you want to buy ${order_size} of {product} coins (y/n)? ")
    if response == "y":
        order = client.market_order_buy(client_order_id=order_id, product_id=product, quote_size=order_size)
        os.makedirs("output/orders", exist_ok=True)
        filepath = f"./output/orders/{product}-{order_id}.json"
        with open(filepath, "w") as f:
            json.dump(order.to_dict(), f, indent=4)
        if order.success:
            print(f"\nJSON Output: {filepath}\n")
        else:
            print("\n[!] Purchase Failed\n")
    else:
        print("\nPurchase canceled\n")

# get_accts()
# get_stock_price()
get_assets()
buy_coins()
print("\n")
