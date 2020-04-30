import requests


r = requests.get("https://bitcoinadvice.io/")
print(r.status_code)
print(r.ok)
