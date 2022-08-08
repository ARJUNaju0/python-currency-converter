from forex_python.converter import CurrencyRates

c=CurrencyRates()
amount=int(input("Amount: "))

print("USD")
print("INR")
print("EUR")
print("AUD")

from_currency=input("enter the 1st country code ").upper()
to_currency=input("enter the 2nd country code  ").upper()
print(amount,from_currency, "to" ,to_currency)
result=c.convert(from_currency,to_currency,amount)
print(result)

def liveExchangeRate():
    rate=c.convert(from_currency,to_currency,1)
    print("live exchange rate ",from_currency ,"to",to_currency,rate)

liveExchangeRate()