"""
This script fetches, processes, and visualizes historical stock price data for Apple Inc. (AAPL)
using the Polygon.io API.

Modules Used:
- requests: For making HTTP requests to the Polygon.io API.
- pandas: For data manipulation and analysis.
- matplotlib.pyplot: For data visualization.

Functionality:
1. Fetch historical stock data for AAPL.
2. Process the data into a pandas DataFrame.
3. Analyze and summarize the data.
4. Plot the closing price trend over time.

API Endpoint:
- URL: 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-06-30/2024-06-01'
- Parameters: 
  - adjusted=true
  - sort=asc
  - apiKey=[Your_API_Key]

Note:
- Replace [Your_API_Key] with your actual Polygon.io API key.

Usage:
- Run the script to fetch data, generate a summary, and display a plot of AAPL stock prices.
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import sys

API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-06-30/2024-06-01'

def get_stock_data(api_key, base_url):
    """
    Fetches stock price data from the Polygon.io API.

    Args:
    - api_key (str): The API key for authenticating with Polygon.io.
    - base_url (str): The base URL for the API endpoint.

    Returns:
    - dict: The JSON response from the API.
    """
    url = f"{base_url}?adjusted=true&sort=asc&apiKey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        if 'results' not in data:
            raise ValueError("Unexpected response format or missing data")
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

def process_data(data):
    """
    Converts JSON data to a pandas DataFrame and processes it.

    Args:
    - data (dict): The JSON data from the API.

    Returns:
    - pd.DataFrame: Processed data as a pandas DataFrame.
    """
    df = pd.DataFrame(data['results'])
    df['t'] = pd.to_datetime(df['t'], unit='ms')
    return df

def summarize_data(df):
    """
    Generates summary statistics of the stock price data.

    Args:
    - df (pd.DataFrame): The DataFrame containing stock price data.

    Returns:
    - dict: Summary statistics including start date, end date, average price,
            highest price, and lowest price.
    """
    summary = {
        'start_date': df['t'].min(),
        'end_date': df['t'].max(),
        'average_price': df['c'].mean(),
        'highest_price': df['h'].max(),
        'lowest_price': df['l'].min()
    }
    return summary

def plot_data(df):
    """
    Plots the closing price of AAPL stock over time.

    Args:
    - df (pd.DataFrame): The DataFrame containing stock price data.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df['t'], df['c'], label='Closing Price')
    plt.title('AAPL Stock Price (2021-2024)')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """
    Main function to orchestrate the fetching, processing, and visualization of stock data.
    """
    data = get_stock_data(API_KEY, BASE_URL)
    df = process_data(data)
    
    summary = summarize_data(df)
    print(summary)
    
    plot_data(df)

if __name__ == "__main__":
    main()
