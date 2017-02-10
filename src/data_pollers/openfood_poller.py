import requests

BASE_URL='https://www.openfood.ch/api/v2'
API_KEY='7bae318b548c33fb739bf02ce2636072'


PROD_ID = '/products/' # ID
PROD_ALL = '/products'
SEARCH_PROD = PROD_ID + '_search'
NUTRIENTS = '/nutrients'
NUTRIENTS_ID = '/nutrients/'
SEARCH_NUT = NUTRIENTS + '_search'

class openFood(object):
    def __init__(self):
        self.base = 'https://www.openfood.ch/api/v2'
        self.api_key = '7bae318b548c33fb739bf02ce2636072'
        self.query = {"page[number]": "200","size[size]": "5000"}
        self.headers = {'Authorization': "Token token={}".format(API_KEY),'Accept': 'application/vnd.api+json','Content-Type': 'application/vnd.api+json'}
        self.recipe = Recipe()

    def connection(self):
        pass

    def print_result(self, req_type):
        if req_type == 1:
            self.get_ingredients()
            return 0
        elif req_type == 2:
            self.get_nutriments(recipe)
            return 0
        else:
            return 1

        """
        url = BASE_URL + '/products'
        r = requests.get(url, params=query, headers=headers)
        print(r.status_code)
        print(r.json())
        """
        


class Recipe(object):
    """docstring for Receipe"""
    def __init__(self):
        self.name
        self.ingredients = Ingredients()


    def create_recipe(self):
        #algo to get recipe name from API
        self.name = name

        #algo to get ingredients in list ==> ingr
        for i in ingr:
            Ingredients()
            Ingredients.name = i
        


    def print_ingredients(self):
        print(self.name)
        for i in ingredients:
            print(i)
    
    def print_nutriments(self):
        for i in nutriments:
            print(i)
    

class Ingredients(object):
    """docstring for Ingredient"""
    def __init__(self):
        self.name
        self.nutriments = []

    def matching(self):


    def get_nutriment(self):
        
        pass





