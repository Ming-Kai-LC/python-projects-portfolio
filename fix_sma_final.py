"""
Final fix for SMA calculation in the KLSE notebook
Handles the fact that notebook source is a list of strings
"""
import json

# Read the notebook
with open('projects/klse-stock-screener/klse_stock_screener.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the add_technical_indicators function cell (cell 16)
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = cell.get('source', [])

        # Join list to check content
        source_text = ''.join(source) if isinstance(source, list) else source

        if 'def add_technical_indicators' in source_text:
            # Replace with fixed version
            new_source = [
                "# Create a reusable function to add all technical indicators\n",
                "def add_technical_indicators(df):\n",
                "    \"\"\"\n",
                "    Add comprehensive technical indicators to price data.\n",
                "    \n",
                "    Parameters:\n",
                "    -----------\n",
                "    df : pd.DataFrame\n",
                "        Historical price data with OHLCV columns\n",
                "    \n",
                "    Returns:\n",
                "    --------\n",
                "    pd.DataFrame\n",
                "        DataFrame with added technical indicators\n",
                "    \"\"\"\n",
                "    df = df.copy()\n",
                "    \n",
                "    # Helper function to safely extract Series from pandas_ta results\n",
                "    def safe_add_indicator(result):\n",
                "        if result is None:\n",
                "            return None\n",
                "        elif isinstance(result, pd.Series):\n",
                "            return result\n",
                "        elif isinstance(result, pd.DataFrame):\n",
                "            # If DataFrame returned, take the first column\n",
                "            return result.iloc[:, 0] if len(result.columns) > 0 else None\n",
                "        return result\n",
                "    \n",
                "    # Moving Averages with safe extraction\n",
                "    df['SMA_20'] = safe_add_indicator(df.ta.sma(length=20))\n",
                "    df['SMA_50'] = safe_add_indicator(df.ta.sma(length=50))\n",
                "    df['SMA_200'] = safe_add_indicator(df.ta.sma(length=200))\n",
                "    df['EMA_20'] = safe_add_indicator(df.ta.ema(length=20))\n",
                "    \n",
                "    # RSI\n",
                "    df['RSI'] = safe_add_indicator(df.ta.rsi(length=14))\n",
                "    \n",
                "    # MACD\n",
                "    macd = df.ta.macd()\n",
                "    if macd is not None:\n",
                "        df = pd.concat([df, macd], axis=1)\n",
                "    \n",
                "    # Bollinger Bands\n",
                "    bbands = df.ta.bbands(length=20, std=2)\n",
                "    if bbands is not None:\n",
                "        df = pd.concat([df, bbands], axis=1)\n",
                "    \n",
                "    # ATR (Average True Range) - Volatility\n",
                "    df['ATR'] = safe_add_indicator(df.ta.atr(length=14))\n",
                "    \n",
                "    # Volume SMA\n",
                "    df['Volume_SMA'] = df['Volume'].rolling(window=20).mean()\n",
                "    \n",
                "    return df\n",
                "\n",
                "print(\"✅ add_technical_indicators() function created!\")\n",
                "print(\"\\nThis function adds:\")\n",
                "print(\"  • Simple Moving Averages (20, 50, 200)\")\n",
                "print(\"  • Exponential Moving Average (20)\")\n",
                "print(\"  • RSI (14-day)\")\n",
                "print(\"  • MACD with signal line\")\n",
                "print(\"  • Bollinger Bands\")\n",
                "print(\"  • ATR (Average True Range)\")\n",
                "print(\"  • Volume Moving Average\")"
            ]

            cell['source'] = new_source
            print(f"Fixed add_technical_indicators function in cell {i}")
            break

# Write the fixed notebook
with open('projects/klse-stock-screener/klse_stock_screener.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook fixed successfully with comprehensive SMA handling!")
