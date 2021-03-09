from Binance_API_Connector import *
from CoinMarketCap_API_Connector import *



if __name__ == '__main__':
	asset_values = get_asset_list()
	asset_prices = get_value_of_assets(asset_values, "EUR")

	print(asset_values)
	print(asset_prices)

	total_value_of_assets = 0
	for coin in asset_values:
		total_value_of_assets += float(asset_prices[coin]) * float(asset_values[coin])

	print(total_value_of_assets)