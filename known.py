
import requests

# URL del endpoint (reemplazá por el que necesites)
url = "https://knownonline.vtexcommercestable.com.br/api/oms/pvt/orders"

# Cabeceras requeridas por VTEX
headers = {
    "X-VTEX-API-AppKey": "vtexappkey-knownonline-IPWBFW",
    "X-VTEX-API-AppToken": "CVBSREIACFNEEBYQWRZZEGPEJJMYKTFKZUBGQDIAZICUEGRPXZZYKLWVFWJHSKQJZCFJASASIZAVEUACSWAKTGAOYGATUBIPSTVCBHPFZHPLKBRKWGOVJFPSBQLTRGXH",
    "Accept": "application/json"
}

# Si es un GET
response = requests.get(url, headers=headers)

# Si es un POST, sería:
# response = requests.post(url, headers=headers, json={"param":"value"})

print("Status:", response.status_code)
data = response.json()

products = data.get("list", [])
if products:
    first_product = products[0]
    print(first_product)
