import requests
import dotenv
import os
dotenv.load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alpha_vantage_api_key}'
r = requests.get(url)
data = r.json()
data = list(data['Time Series (Daily)'].items())[:2]
yesterday_close_stock_price = float(data[0][1]['4. close'])
day_before_yesterday_close_stock_price = float(data[1][1]['4. close'])

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_api_key = os.getenv("NEWS_API_KEY")
if abs(yesterday_close_stock_price - day_before_yesterday_close_stock_price) / day_before_yesterday_close_stock_price > 0.05:
    print("Get News")


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

