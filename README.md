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

## Background
Hello guys! This is my first holistic project utilising my skillsets in SQL and Python. As an incoming Business Analytics Student that is interested in finance as well, I felt that this project allowed me to kill two birds in one stone:
    **1**. Consolidate my respective knowledge in Python and SQL and learn how to link them together (such as through SQLAlchemy)
    **2.** Learn more about trading stocks and the key indicators used as a yardstick for the stock performance.

Upon reflection, through this project, I learnt how to link all the different aspects of Python and SQL together. I had proficiency in both languages separately but none in using them together for full-stack development. Furthermore, I was able to experiment more with the powerful modules such as Pandas and Matplotlib. Lastly, I had learnt much about the finance world through researching for this project and I finally understood how key terms that defined the bedrock of trading tied in together. 

However, this is not the end of the project. I have several improvements to this project that I intend to implement down the road as I further upskill myself. Below are several improvements:

    1. __Improving the Analysis Formula__. In confluence trading, there are numerous esssential key indicators that paint a clear picture on the stock performance. The ones used in the current version are basic indicators as I am still experimenting with the formula and script logic. I look to adding other indicators such as "Relative Strength Index" and "Days since Cross".

    2. __Improving Report Automation__. Right now, while running the code will generate the report, I want to take it a step further by automating that process, setting a daily timestamp for which the code will automatically run and generate the report.
