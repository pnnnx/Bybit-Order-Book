# 📊 BTC/USDT Real-Time Orderbook Monitor 🚀

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pybit](https://img.shields.io/badge/Pybit-3.1.0+-green?logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow)

> 🌟 Real-time BTC/USDT orderbook monitoring with color visualization directly in terminal

## ✨ Features

- 🚀 **10 updates per second** (configurable)
- 🌈 **Color-coded orders**:
  - 🔴 `Ask` - Sell orders
  - 🟢 `Bid` - Buy orders
  - 🔵 Large orders (>1 BTC)
- 📊 **Automatic spread calculation** between best prices
- 🧹 **Self-clearing display** (optional)
- ⚙️ Supports both Bybit mainnet and testnet

💰 Price: 42500.50 | 🔄 Spread: 2.50 USDT
==============================
🔼 ASK (Sell)        🔽 BID (Buy)
------------------------------
| 42503.00         1.25      🔴
| 42502.50         0.75      🔴
==============================
| 42500.50         2.10      🟢
| 42499.00         1.85      🟢

## 🛠 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/yourusername/btc-orderbook-monitor.git
cd btc-orderbook-monitor

# 2. Install dependencies
pip install -r requirements.txt  # or just 'pip install pybit'

# 3. Run
python main.py
