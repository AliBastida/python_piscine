import sys

def get_name(cookbook):
    for name in cookbook:
        print(name)
def get_recipe(recipe_name, cookbook):
    recipe = cookbook.get(recipe_name)
    if recipe:
        print("Nombre de la receta '{}':".format(recipe_name))
        print("Ingredients: {}".format(', '.join(recipe['ingredients'])))
        print("meal: {}".format(recipe['meal']))
        print("prep_time: {}".format(recipe['prep_time']))
cookbook = {
    'bocadillo':{
        'ingredients': ['jamon', 'pan', 'queso', 'tomate'],
        'meal': 'almuerzo',
        "prep_time": 10
    },
    'tarta':{
        'ingredients': ['harina', 'azucar', 'huevos'],
        'meal': 'postre',
        'prep_time': 60
    },
    'ensalada':{
        'ingredients': ['aguacate', 'rucula', 'tomates', 'espinacas'],
        'meal': 'almuerzo',
        'prep_time': 15
    }
}

get_recipe("recipe_name", cookbook)
#get_name(cookbook)

    
