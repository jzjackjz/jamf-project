import requests

response = requests.get("https://mcxlmpfy3k.execute-api.us-east-1.amazonaws.com/dev/animals")
response2 = requests.get("https://mcxlmpfy3k.execute-api.us-east-1.amazonaws.com/dev/animals?animal=dog")
dog = response2.json()

print(dog["animal"])