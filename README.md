# Automated Financial Data Scraper & Analysis System

## Project Description
This project utilises SQL databases and Python modules to create an automated financial analysis system that extracts stock market data, perform technical analysis (Relating to the "Golden Cross Strategy"), and generates a summarized investment report of your desired stocks in Word format.


## Tech Stack
- **Language:** Python 3.x
- **Database:** pgAdmin4 using PostgreSQL (SQLAlchemy)
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Report Generation:** python-docx, python-dotenv


## Key Features
These are the key features of my project:

**ETL** 
1. Extracton of Data: Utilisation of yfinance module to extract real-time market data from Yahoo Finance. 

2. Loading of Data: The raw data is loaded into a PostgreSQL (pgadmin4) database ensuring data integrity for further analysis. (Refer to "scraping.py")

**Quantitative Analysis Engine:** 
1. Data Processing: Leveraged **Pandas** to digest the data from pgadmin4 and derive key quantitative finance indicators through high-performance manipulation such as **SMA50, SMA200, Volatility Percentage, Overnight Gap.** 

2. Algorithmic Logic: Developed a custom analysis engine that generates "Buy/Hold/Sell" recommendations through a decision matrix that references Confluence Trading Strategies and the "Golden Cross Strategy". (Refer to "analysis.py")

3. Strategic Documentation: For a detailed breakdown of the indicator thresholds used as well a visual of the decision matrix used, please refer to the documentation below:

    [Confluence trading indicators and decision matrix (PDF)] (Confluence trading indicators and decision matrix.pdf)


3. Data Visualisation: Integrated **Matplotlib** to generate trend charts from processed DataFrames.

**Dynamic Reporting:** 
1. Modularisation: Programme operates through a centralised exeuction script that bridges the ETL and analysis script. (Refer to "masterscript.py")

2. Document Synthesis: Utilises **python-docx** to programmatically generate reports, embed visuals such as charts and insert analysis from the Quantitative Analysis Engine into a final Word report.


## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file based on the `.env.example` template.
4. Run `python scripts/masterscript.py` to generate reports.


## Project Motivation and Background
This project is my first full-stack integration of Python and SQL. As an incoming Business Analytics Student with a focus on finance, I developed this project to bridge the gap between:
     ** 1. My theoretical knowledge of both languages.** I had attained certifications for both languages separately through practicing and applying my theoretical knowledge to sample/engineered data/problems.

     ** 2. Practical application of my knowledge.** I realised I should put apply my theoretical knowledge for a purpose. I had always wanted to learn more about metrics/logic for stock analysis which I felt would be a useful application of Python analytical modules and SQL databases.

## Key Takeaways
    ** 1. Full-Stack Architecture:** This project alllowed me to apply my knowledge to something tangible and applicable whilie successfully achieving a level of full-stack development through bridging Python Logic with PostgreSQL database using **SQLAlchemy**.

    ** 2. Dynamic Data Engineering:** I scaled my use of **Pandas** and **Matplotlib** from small, "clean" datasets to live, high-volume market data. This was also where I applied my finance research on confluence trading to produce a simple analysis logic from the data for actionable insights.

    ** 3. Document Automation:** I expanded the project scope to include automated reporting using **python-docx**. Through automating the reports, I have learnt the modality of automation modules as well as their methods of implementation.

    ** 4. Version Control and Repository Management:** This was my first project that I uploaded to **GitHub** and was able to learn and understand the Git Workflow (Stage, Commit, Push) which also allowed me to review back prior versions of code. I also learnt to use **.gitignore** and **.env** to protect sensitive environment veriables while allowing for public collaboration on Github

## Improvements
I have several improvements to this project that I intend to implement down the road as I further upskill myself:

    **1. Improving the Analysis Formula:** The ones used in the current version are basic indicators as I am still experimenting with the formula and script logic. I look to adding other indicators such as "Relative Strength Index" and "Days since Cross".

    **2. Improving Report Automation:** I want to take it a step further by automating that process, setting a daily timestamp for which the code will automatically run and generate the report.

    **3. Web Dashboard:** While I intend to develop a more robust front-end such as a Dashboard to provide a more comprehensive analysis of the data.
