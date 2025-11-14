"""
Comprehensive fix for SMA calculation in the KLSE notebook
Handles cases where pandas_ta returns Series, DataFrame, or None
"""
import json

# Read the notebook
with open('projects/klse-stock-screener/klse_stock_screener.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the add_technical_indicators function cell
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = cell.get('source', '')
        if isinstance(source, str) and 'def add_technical_indicators' in source:
            # Replace with fixed version
            new_source = """# Create a reusable function to add all technical indicators
def add_technical_indicators(df):
    \"\"\"
    Add comprehensive technical indicators to price data.

    Parameters:
    -----------
    df : pd.DataFrame
        Historical price data with OHLCV columns

    Returns:
    --------
    pd.DataFrame
        DataFrame with added technical indicators
    \"\"\"
    df = df.copy()

    # Helper function to safely extract Series from pandas_ta results
    def safe_add_indicator(result):
        if result is None:
            return None
        elif isinstance(result, pd.Series):
            return result
        elif isinstance(result, pd.DataFrame):
            # If DataFrame returned, take the first column
            return result.iloc[:, 0] if len(result.columns) > 0 else None
        return result

    # Moving Averages with safe extraction
    df['SMA_20'] = safe_add_indicator(df.ta.sma(length=20))
    df['SMA_50'] = safe_add_indicator(df.ta.sma(length=50))
    df['SMA_200'] = safe_add_indicator(df.ta.sma(length=200))
    df['EMA_20'] = safe_add_indicator(df.ta.ema(length=20))

    # RSI
    df['RSI'] = safe_add_indicator(df.ta.rsi(length=14))

    # MACD
    macd = df.ta.macd()
    if macd is not None:
        df = pd.concat([df, macd], axis=1)

    # Bollinger Bands
    bbands = df.ta.bbands(length=20, std=2)
    if bbands is not None:
        df = pd.concat([df, bbands], axis=1)

    # ATR (Average True Range) - Volatility
    df['ATR'] = safe_add_indicator(df.ta.atr(length=14))

    # Volume SMA
    df['Volume_SMA'] = df['Volume'].rolling(window=20).mean()

    return df

print("✅ add_technical_indicators() function created!")
print("\\nThis function adds:")
print("  • Simple Moving Averages (20, 50, 200)")
print("  • Exponential Moving Average (20)")
print("  • RSI (14-day)")
print("  • MACD with signal line")
print("  • Bollinger Bands")
print("  • ATR (Average True Range)")
print("  • Volume Moving Average")"""

            cell['source'] = new_source
            print(f"Fixed add_technical_indicators function in cell {i}")
            break

# Write the fixed notebook
with open('projects/klse-stock-screener/klse_stock_screener.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook fixed successfully with comprehensive SMA handling!")
