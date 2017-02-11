"""
Sample Python 2.7 code for a call against the OpenFood API products listing, with paging
Replace [API_KEY] with your API Key
curl -X POST --header "Content-Type: application/vnd.api+json" --header "Accept: application/json" --header "Authorization: Token token=5ca3831de0a81aefce3e3f0b4f774a4a" -d "{
  \"query\": {
    \"wildcard\": {
      \"name_translations.en\" : \"toblerone*\"
    }
  }
}" "https://www.openfood.ch/api/v2/products/_search"
USAGE:
$ python product_search.py
"""

import requests

BASE_URL='https://www.openfood.ch/api/v2'
API_KEY='7bae318b548c33fb739bf02ce2636072'

url = BASE_URL + '/products/_search'

query = {
  "query": {
    "bool": {
      "must": [{
        "match": {
          "name_translations.en" : "chicken"
          }
       }]
      }
    }
  }

headers = {
  'Authorization': "Token token={}".format(API_KEY),
  'Accept': 'application/vnd.api+json',
  'Content-Type': 'application/vnd.api+json'
}

r = requests.post(url, json=query, headers=headers)


#print(r.status_code)


print(r.json())