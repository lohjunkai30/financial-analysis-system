import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os



# 1. Connecting the database to current python script using SQLAlchemy
#DB_URL = "postgresql://postgres:Password335C@localhost:5432 python_finance_project"
load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)

def fetch_and_save_stock(ticker, start_date, end_date):
    print(f"Fetching data for {ticker}...")
    
    # 2. Download data via yfinance
    df = yf.download(ticker, start=start_date, end=end_date)

    # reformat the multi-indexed table
    df.columns = df.columns.get_level_values(0)
    
    # Flatten the MultiIndex (yfinance often returns nested columns)
    df = df.reset_index()
    
    # 3. Rename columns to match your SQL table exactly
    # Map: 'Date' -> 'action_date', 'Close' -> 'close_price', etc.
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    df = df.rename(columns={
        'Date': 'action_date',
        'Open': 'open_price',
        'High': 'high_price',
        'Low': 'low_price',
        'Close': 'close_price',
        'Volume': 'volume'
    })
    
    # Add the 'symbol' column which the API doesn't provide in the rows
    df['symbol'] = ticker

    # 4. Filter for only the columns we created in SQL
    cols = ['symbol', 'action_date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']
    df = df[cols]

    #Connect and Delete existing entries for the current ticker to prevent double counting in the event that the script runs twice on the same day
    with engine.connect() as connection:
        query = text(f"DELETE FROM stock_data WHERE symbol = '{ticker}'")
        connection.execute(query)
        connection.commit()

    # 5. Push to SQL
    try:
        df.to_sql(f'stock_data', engine, if_exists='append', index=False)
        print(f"Successfully saved {len(df)} rows to the database!")
    except Exception as e:
        print(f"Error: {e}")

