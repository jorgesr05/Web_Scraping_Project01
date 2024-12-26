from bs4 import BeautifulSoup
import requests

# You can put the web you want to analyze
url = requests.get(
    "https://www.aruma.pe/serum-effaclar-ultra-concentrado-30ml-la-roche-posay/p")

soup = BeautifulSoup(url.content, "html.parser")
result = soup.find("span", {
                   "class": "vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--summary"})
firstPrice_text = result.text
floatFirstPrice = float(firstPrice_text)
print(floatFirstPrice)
# prueba
