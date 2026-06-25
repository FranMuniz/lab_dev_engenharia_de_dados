import requests

url = 'https://api.adviceslip.com/advice'

response = requests.get(url)

print(response.json())