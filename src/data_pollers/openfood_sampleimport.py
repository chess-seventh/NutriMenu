import requests

BASE_URL='https://www.openfood.ch/api/v2'
API_KEY='7bae318b548c33fb739bf02ce2636072'

url = BASE_URL + '/products'

query = {
  "page[number]": "2",
  "size[size]": "5"
}

headers = {
  'Authorization': "Token token={}".format(API_KEY),
  'Accept': 'application/vnd.api+json',
  'Content-Type': 'application/vnd.api+json'
}

r = requests.get(url, params=query, headers=headers)
print(r.status_code)
print(r.json())