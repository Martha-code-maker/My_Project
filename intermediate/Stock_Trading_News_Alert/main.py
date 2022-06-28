from twilio.rest import Client
import requests
import datetime as dt
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ.get("ST_API_KEY")
NEWS_API_KEY = os.eviron.get("NEW_API_KEY")
TWILIO_SID = os.environ.get("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday = dt.date.today() - dt.timedelta(1)
before_yesterday = yesterday - dt.timedelta(1)

stock_parms = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
}
r = requests.get(STOCK_ENDPOINT, params=stock_parms)
data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data['4. close']

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_diff = float(yesterday_closing_price)-float(before_yesterday_closing_price)
up_down = None
if price_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((price_diff/float(yesterday_closing_price))*100)
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5:
    print("Get News")

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey" : NEWS_API_KEY
    }
    news_r = requests.get(NEWS_ENDPOINT, params=news_params)
    n_data = news_r.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = n_data[:3]
    print(three_articles)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']} " for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body= article,
            from_='+18643054926',
            to='phone_number'
        )


