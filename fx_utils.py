import pandas as pd


DATA_DIR = "data/raw"

def load_data():
    """read data from 3 files and return them"""
    clients = pd.read_csv(f"{DATA_DIR}/clients.csv", parse_dates=["join_date"])
    trades = pd.read_csv(f"{DATA_DIR}/trades.csv", parse_dates=["date"])
    fx_daily = pd.read_csv(f"{DATA_DIR}/fx_daily.csv", parse_dates=["date"])
    return clients, trades, fx_daily

    
def add_indicators(df, window=20):
    """Insert 3 columns ret / ma / vol into a table"""
    df = df.copy()
    df["ret"]   = df["close"].pct_change()
    df["ma"]  = df["close"].rolling(window).mean()
    df["vol"] = df["ret"].rolling(window).std()
    return df


def data_quality_report(df):
    """Checking missing and unique data"""
    a = df.isna().sum()
    b = df.nunique()
    table = pd.DataFrame({
        "Total NaN": a,
        "Unique": b,
    })
    return table