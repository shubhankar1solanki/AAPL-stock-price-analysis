# AAPL Stock Price Analysis

This project fetches, processes, and visualizes historical stock price data for Apple Inc. (AAPL) using the Polygon.io API. The script retrieves data for the period from June 30, 2021, to June 1, 2024, calculates summary statistics, and plots the closing price trend over time.

## Idea of the Script

The script performs the following tasks:
1. Fetches historical stock data for AAPL from the Polygon.io API.
2. Processes the data into a pandas DataFrame.
3. Calculates summary statistics including start date, end date, average price, highest price, and lowest price.
4. Plots the closing price trend over the specified period.

## Installation

To install the required packages, run the following command:

```
pip install -r requirements.txt
```

To run the script, use below command:

```
python aapl_stock_analysis.py
```

## Project Structure

- **Script File**: `aapl_stock_analysis.py` - This file contains code to gather data from the Polygon.io API, prepare a summary, and generate a chart.
- **Output File**: `output.png` - This image file displays the generated chart.
- **Requirements File**: `requirements.txt` - This file lists the packages used in the script.