# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot that places **MARKET** and **LIMIT** orders on **Binance Futures Testnet (USDT-M)**.
The application is designed with a **modular structure**, separating the API client layer and CLI layer, with proper **logging and error handling**.

---

## Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Supports both **BUY** and **SELL**
* Command-line interface using **argparse**
* **Logging** of API requests, responses, and errors
* **Exception handling** for API errors and invalid inputs
* Modular code structure for maintainability

---

## Tech Stack

* Python 3.x
* python-binance
* argparse
* logging
* python-dotenv

---

## Project Structure

```
trading-bot/
│
├── client.py          # Binance Futures API client wrapper
├── cli.py             # CLI argument parsing
├── main.py            # Main application logic
├── logger.py          # Logging configuration
├── trading_bot.log    # Log file with API requests/responses
├── requirements.txt   # Python dependencies
└── README.md
```

---

## Setup Instructions

### 1. Clone or Download the Repository

```
git clone <repository_url>
cd trading-bot
```

or download the zip and extract it.

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Create Environment File

Create a `.env` file in the project root and add your **Binance Futures Testnet API credentials**.

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

You can generate API keys from:

https://testnet.binancefuture.com

---

## Running the Application

### MARKET Order Example

```
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

Example Output

```
Order Request Summary
---------------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

Order Response
--------------
Order Placed Successfully
Order ID: 12345678
Status: FILLED
Executed Qty: 0.002
Avg Price: 64000
```

---

### LIMIT Order Example

```
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 80000
```

Example Output

```
Order Request Summary
---------------------
Symbol: BTCUSDT
Side: SELL
Type: LIMIT
Quantity: 0.002
Price: 80000

Order Response
--------------
Order Placed Successfully
Order ID: 12345679
Status: NEW
Executed Qty: 0
Avg Price: None
```

---

## Logging

All API requests, responses, and errors are logged to:

```
trading_bot.log
```

Example log entry:

```
2026-03-14 21:05:11 | INFO | Starting trading bot
2026-03-14 21:05:12 | INFO | Placing BUY MARKET order for BTCUSDT
2026-03-14 21:05:13 | INFO | Order placed successfully
```

Logs for both **MARKET** and **LIMIT** orders are included.

---

## Error Handling

The application includes error handling for:

* Invalid CLI inputs
* Binance API errors
* Network/API failures
* Missing environment variables

Errors are displayed in the console and recorded in the log file.

---

## Assumptions

* The bot interacts with **Binance Futures Testnet (USDT-M)** only.
* Minimum order notional on testnet is **$100**, so order quantity must meet that requirement.
* `.env` file containing API credentials is **not included in the repository for security reasons**.

---

## Possible Improvements (Future Work)

* Support additional order types (Stop-Limit / OCO)
* Interactive CLI menu
* Web-based UI dashboard
* Automated trading strategies

---

## Author

Vishal Gala
