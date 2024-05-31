import requests

# URL od dodávateľa
url = 'https://vreckovynoz.sk/heureka'
response = requests.get(url)
with open('C:\\Users\\larso\\xml_project\\rosler_supplier.xml', 'wb') as file:
    file.write(response.content)
