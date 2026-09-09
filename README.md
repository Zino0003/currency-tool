# Currency Exchange Tool
A system that asks the user to enter the currency whose exchange rate he wants to know, and how much it's worth compared to 1 dollar (the reference currency).
![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Demo](assets/demo.png)
___
## ✨ Features :
- It supports more than 160 currencies worldwide
- A clean and user-friendly system
- Automatic input validation
- Complete handling of communication errors
- Professional logging in a separate file (currency.log)
- Protecting the API Key with a ".env" file
___
## ✨ Prerequisites :
- **Python +3.8**
- **Git**
- **Free API Key** from [ExchangeRate-API](https://www.exchangerate-api.com/)
___
## ✨ Installation :
1. Clone the project :
```bash
git clone https://github.com/Zino0003/currency-tool.git
cd currency-tool
```
2. Creating the virtual environment (v_env) and activate it :
```bash
python -m venv v_env
```
- Activate on Windows (Git Bash) :
```bash
source v_env/Scripts/activate
```
- Activate on Windows (CMD / PowerShell) :
```bash
v_env\Scripts\activate
```
- Activate on macOS / Linux :
```bash
source v_env/bin/activate
```
3. Install the libraries :
```bash
pip install -r requirements.txt
```
4. Copy `.env.example` to create your local `.env` file: 
- On Windows :
```bash
copy .env.example .env
```
- On macOS / Linux :
```bash
cp .env.example .env
```
=> **Note:** The `.env` file is included in `.gitignore` to prevent sensitive credentials from being committed.
___
## ✨ Configuration :
1. Get your free API key from [ExchangeRate-API](https://www.exchangerate-api.com)
2. Open the `.env` file in your text editor.
3. Paste your key inside the '.env' file as follow:
```env
API_KEY=your_api_key_here
```
___
## ✨ Usage : 
- Run the code :
```bash
python main_project_code.py
```
=> Success :
```
Enter the currency code: JPY
1 USD = 154.4091 JPY
```
=> Invalid currency :
```
Enter the currency code: ABC
The currency does not exist. Check the currency code.
```
___
## ✨ Project Structure :
```text
currency-tool/
├── assets/               # Project screenshots and media
├── .env.example          # Environment variables template
├── .gitignore            # Git exclusion rules
├── LICENSE               # MIT License
├── main_project_code.py  # Main CLI application script
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
```
___
## ✨ Built With :
- [Python](https://www.python.org/) - Programming Language
- [Requests](https://requests.readthedocs.io/) - HTTP library for making API requests
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Reads key-value pairs from `.env` files
- [Logging](https://docs.python.org/3/library/logging.html) - Built-in Python module for event logging
- [ExchangeRate-API](https://www.exchangerate-api.com/) - REST API used for fetching real-time exchange rates
___
## ✨ License :
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
___
## ✨ Contact :
**Mr; Zine elabidine ABDELOUAHAB** 
- **LinkedIn Profile:** [Click here](https://www.linkedin.com/in/zine-abdelouahab) 
- **Email:** abdelouahabzineelabidine@gmail.com

Project Link: [GitHub Repository](https://github.com/Zino0003/currency-tool)