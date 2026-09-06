import requests
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    filename="currency.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s => %(name)s | %(levelname)s | %(message)s",
    datefmt="%d %B %Y ; %H:%M:%S"
)
My_logger=logging.getLogger(__name__)
# تحميل المتغيرات من ملف .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
My_logger.info(f"Verefication if main.py file is related and connected with .env file => {API_KEY[:5]}") #just 5 first letters of API_KEY
#The API key here is only visible in the secret file (currency.log) located in .gitignore
if not API_KEY:
    raise ValueError("API_KEY doesn't exist in .env file")
while True:
    try:
        currency = input("Enter the currency code (example: EUR, SAR, DZD): ").upper()
        #يجب اضافه شرط ليظهر الخطا لانه هنا حتى لو ادخلت عددا يعتبره نصا (تدخل 12 => يعتبره '12')
        # تحقق يدوي: إذا كان الإدخال يحتوي على أرقام أو ليس بطول 3 أحرف
        if not currency.isalpha() or len(currency) != 3:
            raise ValueError("Invalid currency format")
            
        break # اخرج من الحلقة إذا كان الإدخال صحيحاً

    except ValueError:
        print("You entered an incorrect code! Please enter the right currency code (example: EUR, SAR, DZD).")
        My_logger.warning(f"User entered an incorrect code: {currency}")  #to know the error of user and what he entered 


url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
try:
    response = requests.get(url,timeout=(5,10))
    data = response.json()
    My_logger.debug(data)  ##just to see the form of data to can build the rest code parts
except requests.exceptions.Timeout:
    print("Server response delay — please try again")
    My_logger.error("Server response delay or server data transmission delay (exceeding the specified timeframe)")
except requests.exceptions.ConnectionError:
    print("Internet outage or server not available")
    My_logger.critical("Internet outage or server not available")

else: 
    if response.status_code == 200 :
        rate = data["conversion_rates"].get(currency)
        if rate :
            My_logger.info(f"1 USD = {rate} {currency}")
            print(f"1 USD = {rate} {currency}")
        else: 
            print("The currency does not exist. Check the currency code.")
            My_logger.warning("The currency does not exist. Check the currency code.")
    else : 
        print(f"Connection error : {response.status_code}")
        My_logger.error(f"Connection error : {response.status_code}")


