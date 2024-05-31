import requests

# URL od dodávateľa
url = 'https://knifestock.sk/export/google-merchant-sk.xml'
response = requests.get(url)
with open('supplier.xml', 'wb') as file:
    file.write(response.content)
