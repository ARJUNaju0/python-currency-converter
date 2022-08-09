from forex_python.converter import CurrencyRates

c=CurrencyRates()
print("currency converter")

amount=int(input("Amount: "))
print()
print("currency code")
print("USD")
print("INR")
print("EUR")
print("AUD")

from_currency=input("From currency ").upper()
to_currency=input("To currency  ").upper()
print("from",from_currency, "to" ,to_currency)
result=c.convert(from_currency,to_currency,amount)
print(amount,from_currency,"equal to",result,to_currency)
print()
def liveExchangeRate():
    rate=c.convert(from_currency,to_currency,1)
    print("currency exchange rate 1",from_currency ,"to",to_currency,rate)

liveExchangeRate()