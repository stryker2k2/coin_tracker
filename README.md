# Coin Tracker
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Using Coinbase Advanced API Python SDK which can be found at:\
https://github.com/coinbase/coinbase-advanced-py \
https://docs.cdp.coinbase.com/advanced-trade/docs/welcome/

## Linting
``` markdown
# https://pypi.org/project/ruff/
ruff check . --fix
```

## Installing
``` markdown
# Windows
python3 -m pip install virtualenv
python3 -m virtualenv venv
.\venv\Scripts\activate
(venv) pip install -r requirements.txt

# Linux
python3 -m pip install virtualenv
python3 -m virtualenv venv
source ./venv/bin/activate
(venv) pip install -r requirements.txt
```

## Running
Make a 'keys' folder and place your Coinbase API JSON Key (cdp_api_key.json) inside. The output will show in your terminal (stdout) and inside the 'output' folder.
``` markdown
# Windows
(venv) python app.py
```

## Output
``` markdown
JSON Output: ./output/accounts/accounts.json

Market
ETH-USDC: $2196.2 / coin

Wallet
USDC: 750.01
XRP: 8209.60 ($17016.04)
ETH: 2.28 ($5005.89)
BTC: 0.26 ($21377.96)

Do you want to make a purchase (y/n)? y

What stock do you want to purchase (ex: BTC-USDC)? ETH-USDC

How many ETH-USDC do you want to buy (in Dollars)? 250

Do you want to buy $250 of ETH-USDC coins (y/n)? n

Purchase canceled
```
