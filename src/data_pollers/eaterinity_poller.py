#from urllib2 import Request, urlopen

API_KEY = 'h4cK4tH0NOg75HjfK339KlOlpa39fJzxXw'
API_URL = 'https://test.eaternity.ch/'

# https://co2.eaternity.ch/api/recipes/
# Headers: Content-Type:application/json

request = Request('https://co2.eaternity.ch/api/kitchens/' + __ID__ + '/recipes')

response_body = urlopen(request).read()
print(response_body)



"""
__ID__ = $get input

GET https://co2.eaternity.ch/api/recipes/__ID__

"""