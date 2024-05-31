import requests

# URL od dodávateľa Opinel
url = 'http://feed.pottenpannen.sk:28000/input/8504'
# Užívateľské meno a heslo
username = 'feedppsk'
password = 'ham'

response = requests.get(url, auth=(username, password))
with open('C:\\Users\\larso\\xml_project\\opinel_supplier.xml', 'wb') as file:
    file.write(response.content)

