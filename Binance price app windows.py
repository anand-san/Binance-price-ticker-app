from tkinter import *
import json
import requests
def coinval(event):
	inp=entry.get()
	inp=inp.upper()
	if inp!="BTC":
		binance=requests.get("https://api.binance.com/api/v1/ticker/24hr?symbol="+inp+"BTC")
		data=binance.json()
		try:
			finex=requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
			btc=finex.json()
			usdprice=float((btc["last_price"]))
			btcprice=float((data["lastPrice"]))
			usdval=str(usdprice*btcprice)
			usdvald=str(("Value USD : "+usdval+" USD"))
			lastprice=str(("Value BTC : "+data["lastPrice"]+" BTC"))
			change=str(("24Hr Change : "+data["priceChange"]+" BTC"))
			high=str(("24hr High : "+data["highPrice"]+" BTC"))
			low=str(("24hr Low : "+data["lowPrice"]+" BTC"))
			res.configure(text = "Here are your results for "+ inp +"\n"+ usdvald+"\n"+lastprice+"\n"+change+"\n"+high+"\n"+low)
		except:
			err=str((inp+" is an invalid symbol"))
			res.configure(text = err)
	else:
		finex=requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
		btc=finex.json()
		lastprice=str(("Value : "+btc["last_price"]+" USD"))
		low=str(("24hr Low : "+btc["low"]+" USD"))
		high=str(("24hr High : "+btc["high"]+" USD"))
		volume=str(("Volume 24hr: "+btc["volume"]+" BTC"))	
		err=str((inp+" is an invalid symbol"))
		try:
			res.configure(text = "Here are your results for "+ inp +"\n"+lastprice+"\n"+volume+"\n"+high+"\n"+low)
		except:
			res.configure(text = err)
	return
w = Tk()
lab = Label(w, text='Check Coin Prices')
lab.pack()
Label(w, text="Enter Coin Symbol (press Enter)").pack()
entry = Entry(w)
entry.bind("<Return>", coinval)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()

		

