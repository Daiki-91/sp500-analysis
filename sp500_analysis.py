import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# S&P500のデータを取得
symbol = "^GSPC"
data = yf.download(symbol, start="2020-01-01", end="2025-01-01")

# 移動平均線の追加 (50日、200日)
data['50ma'] = data['Close'].rolling(window=50).mean()
data['200ma'] = data['Close'].rolling(window=200).mean()

# 日次リターン計算
data['Return'] = data['Close'].pct_change() * 100  # パーセンテージで計算

# グラフを描画
plt.figure(figsize=(14,7))

# 株価と移動平均線をプロット
plt.subplot(2, 1, 1)  # 1つ目のプロット
plt.plot(data['Close'], label="S&P500 Close")
plt.plot(data['50ma'], label="50-Day Moving Average", linestyle='--')
plt.plot(data['200ma'], label="200-Day Moving Average", linestyle='--')
plt.title('S&P500 and Moving Averages')
plt.legend()

# リターンをプロット
plt.subplot(2, 1, 2)  # 2つ目のプロット
plt.plot(data['Return'], label="Daily Return", color='orange')
plt.title('Daily Return of S&P500')
plt.legend()

plt.tight_layout()
plt.show()
