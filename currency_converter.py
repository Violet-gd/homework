def currency_converter(amount,from_currency,to_currency):
    conversion_rate = { 
    'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06}, 
    'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81}, 
    'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45}, 
    'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    if amount<0:
        return 0.0
    else:
        return round(conversion_rate[from_currency][to_currency]*amount,2) 
a=int(input("amount"))
b=input("from_currency")
c=input("to_currency")
print(currency_converter(a,b,c))