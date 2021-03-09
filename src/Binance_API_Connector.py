import requests, json, hashlib, hmac

API_key = ""
secret_key = ""

base_url = "https://api.binance.com"

#Currently just for debugging purposes
system_status_endpoint = "/wapi/v3/systemStatus.html"
account_status = "/wapi/v3/accountStatus.html"
account_API_trading_status = "/wapi/v3/apiTradingStatus.html"
test_connectivity = "/api/v3/ping"

check_server_time = "/api/v3/time"
symbol_price_ticker = "/api/v3/ticker/price"
account_information = "/api/v3/account"


def get_account_information():
	servertime = get_server_time()

	payload = {	"timestamp":  str(servertime) }

	signature = create_signature(dict_to_string(payload))
	payload["signature"] = signature

	header = {"X-MBX-APIKEY" : API_key}

	return requests.get(base_url + account_information, params=payload, headers=header).text


def get_server_time():
	return json.loads(requests.get(base_url + check_server_time).text)['serverTime']


def create_signature(query_string):
	return hmac.new(secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()


def dict_to_string(dictionary):
	string = ""
	for key in dictionary.keys():
		string = string + key + "=" + dictionary.get(key) +"&"

	return string[:-1]


def get_asset_list():
	account_info = json.loads(get_account_information())
	balances = account_info["balances"]
	assets = {}

	for coin in balances:
		total_value_of_asset = float(coin["free"]) + float(coin["locked"])
		if (total_value_of_asset > 0):
			assets[coin["asset"]] = total_value_of_asset
			
	return assets



