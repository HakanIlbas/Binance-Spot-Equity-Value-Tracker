from Binance_API_Connector import *
from CoinMarketCap_API_Connector import *
import time


if __name__ == '__main__':
	print("Binance Spot Equity Value Tracker")
	CMC_API_key = input("Please enter your CoinmarketCap API key: ")
	Binance_API_key = input("Please enter your Binance API key: ")
	Binance_secret_key = input("Please enter your Binance Secret key: ")
	currency = input("Please input the currency you would like to see your balance in (i.e. EUR or USD): ")

	while(True):
		asset_values = get_asset_list(Binance_API_key, Binance_secret_key)
		asset_prices = get_value_of_assets(asset_values, currency, CMC_API_key)

		total_value_of_assets = 0
		for coin in asset_values:
			total_value_of_assets += float(asset_prices[coin]) * float(asset_values[coin])

		print("Total value of assets is " + str(total_value_of_assets) + " " + currency)
		time.sleep(5 * 60)