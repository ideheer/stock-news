import requests
import os


ALPHA_API_KEY = os.environ["Alpha_Key"]
NEWS_API_KEY = os.environ["News_Key"]

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_stock_data():
    parameters = {
        "apikey": ALPHA_API_KEY,
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
    }
    url = 'https://www.alphavantage.co/query'
    response = requests.get(url, params=parameters)
    stock_data = response.json()
    first_two = dict(list((stock_data["Time Series (Daily)"]).items())[0: 2])
    result = []
    for k in first_two:
        result.append(first_two[k]['4. close'])
    difference = abs(float(result[0]) - float(result[1]))
    five_percent = float(result[0])*.05
    if difference > five_percent:
        print("Get News")


def get_news():
    parameters = {
        "apiKey": NEWS_API_KEY,
        "q": "+Tesla",
    }
    url = 'https://newsapi.org/v2/everything'
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    news_data = response.json
    print(type(news_data))
get_news()
# https://newsapi.org/v2/everything?q=+Tesla&apiKey=4d2f04456d6a404fbcba899bf7d3255a&searchIn=title&from=08-02-2023&language=en
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

