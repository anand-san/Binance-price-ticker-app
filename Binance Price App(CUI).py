# Author : https://github.com/seanjin17

import json
import requests
def get_data():
	finex=requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
	btc=finex.json()
	inp=input("Input Symbol : ")
	inp=inp.upper()
	if inp=="BTC":
		lastprice=str(("Value : "+btc["last_price"]+" USD"))
		low=str(("24hr Low : "+btc["low"]+" USD"))
		high=str(("24hr High : "+btc["high"]+" USD"))
		volume=str(("Volume 24hr: "+btc["volume"]+" BTC"))	
		print ("Here are your results for "+ inp +"\n"+lastprice+"\n"+volume+"\n"+high+"\n"+low)
		get_data()
	else:
		m=requests.get("https://api.binance.com/api/v1/ticker/24hr?symbol="+inp+"BTC")
		data=m.json()
		try:		
			usdprice=float((btc["last_price"]))
			btcprice=float((data["lastPrice"]))
			usdval=str(usdprice*btcprice)
			usdvald=str(("Value USD : "+usdval+" USD"))
			lastprice=str(("Value BTC : "+data["lastPrice"]+" BTC"))
			change=str(("24Hr Change : "+data["priceChange"]+" BTC"))
			high=str(("24hr High : "+data["highPrice"]+" BTC"))
			low=str(("24hr Low : "+data["lowPrice"]+" BTC"))
			print ("Here are your results for "+ inp +"\n"+ usdvald+"\n"+lastprice+"\n"+change+"\n"+high+"\n"+low)
			get_data()
		except:
			print(inp+" is an invalid symbol or it is not yet listed on binance")
			get_data()
get_data()
