import json, requests


API_key = ""

base_url = "https://pro-api.coinmarketcap.com"
price_of_coins_endpoint = "/v1/cryptocurrency/quotes/latest"



header = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_key,
}



def get_value_of_assets(assets, currency):
	symbols = ""
	prices_of_assets = {}


	for coin in assets:
		symbols = symbols + coin + ","


	symbols = symbols[:-1]

	parameters = {
  		'convert': currency,
  		'symbol': symbols
	}

	response = requests.get(base_url + price_of_coins_endpoint, params=parameters, headers=header)
	data = json.loads(response.text)['data']

	

	for coin in data:
		prices_of_assets[str(data[coin]["symbol"])] = str(data[coin]['quote'][currency]['price'])

	return prices_of_assets





