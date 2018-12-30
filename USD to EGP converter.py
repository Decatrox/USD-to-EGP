import urllib.request
from decimal import Decimal

url = "https://markets.businessinsider.com/currencies/usd-egp"
r = urllib.request.urlopen(url)
text = r.read()
text = str(text)
pos = text.index("CurrentPrice")
#edit pos+19 according to how may decimal places there si on the webpage
pos2 = text[pos+14:].index(",")
pos3 = text[pos+14:].index(".")
dp = (pos2-pos3)
rate = text[pos+14:pos+14+pos2]
rate = Decimal(rate.replace('.',''))
#edit /100 according to the same thing
rate = rate/(10**(dp-1))
value_USD = input("Please enter the value in USD that you want to convert to EGP: ")

if "." in value_USD:
  dot = value_USD.index(".")
  length = len(value_USD)
  value_USD = (Decimal(value_USD.replace('.',''))) / (10**(length-dot-1))
else:
     value_USD = int(value_USD)

while 1==1:
   value_EGP = value_USD * rate
   print (value_EGP, " pounds")
   value_USD = input("Enter another value to convert or type 0 to exit: ")
   if value_USD == "0":
      break
   if "." in value_USD:
     dot = value_USD.index(".")
     length = len(value_USD)
     value_USD = (Decimal(value_USD.replace('.',''))) / (10**(length-dot-1))
   else:
        value_USD = int(value_USD)


