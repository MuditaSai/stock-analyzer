from dotenv import load_dotenv
import os
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time

load_dotenv()  # Load variables from .env file
api_key = os.getenv("API_KEY")

endpoint = "time_series"
 
url = f"https://api.finazon.io/latest/finazon/us_stocks_essential/{endpoint}"
 
querystring = {"ticker": "AAPL", "interval": "4mo", "start_at": 32585600, "end_at": int(time.time()), "page_size": 1000}
 
headers = {"Authorization": f"apikey {api_key}"}
 
response = requests.get(url, headers=headers, params=querystring).json()
data = response["data"]

timestamp = int(time.time())
date_time = datetime.utcfromtimestamp(timestamp)
# Convert Unix timestamps to datetime objects and extract high prices
timestamps = [datetime.utcfromtimestamp(entry["t"]) for entry in data]
high_prices = [entry["h"] for entry in data]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 4))  # Adjust width and height
ax.plot(timestamps, high_prices, marker='o', linestyle='-', linewidth=1.5, markersize=4)  # Set line thickness

# Format the x-axis to show dates clearly
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('High Price')
ax.set_title(f'High Prices Over Time for {querystring["ticker"]}')

# Display the plot
plt.show()

