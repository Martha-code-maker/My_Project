import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

account_sid = "#ACCOUNT_SID"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 37.16,
    "lon": 127.02,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

will_rain = False

for i in hourly_data:
    condition_code = i["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella?",
        from_='#twilio number',
        to='#your phone number'
    )

    print(message.status)
