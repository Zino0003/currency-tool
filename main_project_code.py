import requests
import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
#print(API_KEY) for verefication of if main.py file is related and connected with .env file
if not API_KEY:
    raise ValueError("API_KEY doesn't exist in .env file")

currency=input("Enter the currency code (example: EUR, SAR, DZD): ").upper()
url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
response = requests.get(url)
data = response.json()
#print(data) just to see the form of data to can build the rest code parts
if response.status_code == 200 :
    rate = data["conversion_rates"].get(currency)
    if rate :
    print(f"1 USD = {rate} {currency}")
    else: 
        print("The currency does not exist. Check the currency code.")
else : 
    print(f"Connection error : {response.status_code}")

    