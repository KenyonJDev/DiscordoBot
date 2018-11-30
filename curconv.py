import urllib.request
import json

amount = input("amount? ")
from_currency = input("from? ")
to_currency = input("to? ")
print(amount + '' + from_currency + '' + to_currency)

class CurrencyConverter:

	rates = {}

	def __init__(self, url):
		req = urllib.request.Request(url, headers={'User-Agent': 'howCode Currency Bot'})
		data = urllib.request.urlopen(req).read()
		data = json.loads(data.decode('utf-8'))
		self.rates = data["rates"]

	def convert(self, amount, from_currency, to_currency):
		initial_amount = amount
		if from_currency != "EUR":
			amount = amount / self.rates[from_currency]
		if to_currency == "EUR":
		 	return initial_amount, from_currency, '=', amount, to_currency
		else:
			return initial_amount, from_currency, '=', amount * self.rates[to_currency], to_currency

    def getAnswer(userInput):
        amount = userInput.lower().replace("convert ", '')




converter = CurrencyConverter("http://data.fixer.io/api/latest?access_key=0930e8e17d8bbe942a4bec2cc9feab58") #api key from fixer


#Testing cases
#print(converter.convert(1.0, "EUR", "USD"))
#print(converter.convert(1.0, "GBP", "USD"))
#print(converter.convert(1.0, "CAD", "GBP"))
#print(converter.convert(1.0, "CAD", "EUR"))
#print(converter.convert(1.0, "GBP", "USD"))