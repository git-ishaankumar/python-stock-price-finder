import yfinance as yf
from pprint import pprint
import os
import sys


def search():
    input_ticker = input(
        "\nInput a ticker from any company on the stock market.\n\n"
    ).upper()
    ticker = yf.Ticker(input_ticker)
    info = ticker.info
    if not info or 'symbol' not in info:
        print("\nTicker doesn't exist")
        return search()
    company_info = {
        "Ticker Symbol": input_ticker,
        "Company Name": info.get("longName", "N/A"),
        "Market Price": info.get("regularMarketPrice", "N/A"),
        "Market Capitalization": info.get("marketCap", "N/A"),
        "Sector": info.get("sector", "N/A"),
        "Industry": info.get("industry", "N/A"),
        "Previous Close": info.get("previousClose", "N/A"),
        "Open": info.get("open", "N/A"),
        "52-Week High": info.get("fiftyTwoWeekHigh", "N/A"),
        "52-Week Low": info.get("fiftyTwoWeekLow", "N/A"),
        "Volume": info.get("volume", "N/A"),
        "Dividend Yield": info.get("dividendYield", "N/A"),
        "Earnings Date": info.get("earningsDate", "N/A"),
        "PE Ratio": info.get("trailingPE", "N/A"),
        "Beta": info.get("beta", "N/A"),
    }
    print("\n*********************************")
    for key, value in company_info.items():
        print(f"{key}: {value}")

    print("\n*********************************")

    return choose()


def recommendation():
    input_ticker = input(
        "\nInput a ticker from any company on the stock market.\n\n"
    ).upper()
    ticker = yf.Ticker(input_ticker)
    info = ticker.info
    if not info or 'symbol' not in info:
        print("Ticker doesn't exist")
        return search()
    recommendations = ticker.recommendations
    print("\n*********************************")
    print(f"Ratings given by analysts for {info.get("longName", "N/A"),}")
    print(recommendations.tail())

    print("\n*********************************")

    return choose()

def download():
    input_ticker = input(
        "\nInput a ticker from any company on the stock market.\n\n"
    ).upper()
    ticker = yf.Ticker(input_ticker)
    info = ticker.info
    if not info or 'symbol' not in info:
        print("Ticker doesn't exist")
        return search()
    filename = f"{input_ticker}.txt"
    file_exists = os.path.isfile(filename)
    company_info = {
        "Ticker Symbol": input_ticker,
        "Company Name": info.get("longName", "N/A"),
        "Market Price": info.get("regularMarketPrice", "N/A"),
        "Market Capitalization": info.get("marketCap", "N/A"),
        "Sector": info.get("sector", "N/A"),
        "Industry": info.get("industry", "N/A"),
        "Previous Close": info.get("previousClose", "N/A"),
        "Open": info.get("open", "N/A"),
        "52-Week High": info.get("fiftyTwoWeekHigh", "N/A"),
        "52-Week Low": info.get("fiftyTwoWeekLow", "N/A"),
        "Volume": info.get("volume", "N/A"),
        "Dividend Yield": info.get("dividendYield", "N/A"),
        "Earnings Date": info.get("earningsDate", "N/A"),
        "PE Ratio": info.get("trailingPE", "N/A"),
        "Beta": info.get("beta", "N/A"),
    }
    with open(filename, "w") as file:
        for key, value in company_info.items():
            file.write(f"{key}: {value}\n")
    
    if file_exists:
        print(f"Updated company information saved to {filename}.")
    else:
        print(f"New file {filename} created and company information saved.")


def choose():
    print("\n💵 Stock Market Info 💵")
    choice = input(
        "1️⃣ Recommendations\n2️⃣ Search by Ticker\n3️⃣ Download Company Info\n4️⃣ Quit\n\n"
    )
    if choice not in ["1", "2", "3", "4"]:
        return choose()
    elif choice == "1":
        recommendation()
    elif choice == "2":
        search()
    elif choice == "3":
        download()
    elif choice == "4":
        sys.exit("\nThanks for using Stock Market Price Finder! 👋")



choose()
