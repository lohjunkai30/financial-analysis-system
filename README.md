# Automated Financial Data Scraper & Analysis System

## Project Description
This project utilises SQL databases and Python modules to create an automated financial analysis system that extracts stock market data, perform technical analysis (Relating to the "Golden Cross Strategy"), and generates a summarized investment report of your desired stocks in Word format.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Database:** pgAdmin4 using PostgreSQL (SQLAlchemy)
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Report Generation:** python-docx, python-dotenv

## 🚀 Key Features
1. **Scraping:** Utilisation of yfinance module to scrape stock data off Yahoo Finance to be stored in pgAdmin4 SQL database ("scraping.py")
2. **Financial Analysis System:** Extracts the stock data from database to derive key indicators on stock performances via Pandas (Eg: SMA50, SMA200, Volatility Percentage, Overnight Gap). This includes a simple formula that mimics confluence trading by taking into consideration all the key indictors calculated to come to a conclusion of the best course of action for that stock. Lastly, to further supplement the analysis, graphs are generated from the Pandas dataframe using MatPlotLib. ("analysis.py")
3. **Automated Reporting:** Generates a `.docx` report that includes all the key indicators and analysis from the system as well as the plotted graphs. ("masterscript.py")
4. **Secure Data Handling:** Uses `.env` variables to manage database credentials securely.


## ⚙️ Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file based on the `.env.example` template.
4. Run `python scripts/masterscript.py` to generate reports.