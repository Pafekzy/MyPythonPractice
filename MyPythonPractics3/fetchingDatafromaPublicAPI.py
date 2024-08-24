import requests

url = input("Enter the URL of the public API: ")
response = requests.get(url)
data = response.json()
print(data)

#Fetching Data from a Public API