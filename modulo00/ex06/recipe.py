from operator import truediv
import sys


def get_name():
    for name in cookbook:
        print(name)
def get_recipe(recipe_name):
    recipe = cookbook.get(recipe_name)
    if recipe:
        print("Nombre de la receta '{}':".format(recipe_name))
        print("Ingredients: {}".format(', '.join(recipe['ingredients'])))
        print("meal: {}".format(recipe['meal']))
        print(f"prep_time: {recipe['prep_time']}")

def erase_recipe(recipe_name):
    if recipe_name not in cookbook.keys():
        print("No such recipe in cookbook")
    else:
        del cookbook[recipe_name]

def include_recipe():
    new_recipe = input("Enter name:\n")
    ingredients = []
    ingredient = input("Enter ingredients: \n")
    while (ingredient != ''):
        ingredients.append(ingredient)
        ingredient = input()
    meal = input("Enter a meal type: \n")
    prep_time = input("Enter a preparation time: \n")
    cookbook[new_recipe] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}
   
    print(cookbook)

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

# include_recipe(cookbook)
# print(cookbook)
# get_recipe("tarta", cookbook)
# get_name(cookbook)
# erase_recipe('tarta', cookbook)



options = """
    '1': 'Add a recipe',
    '2': 'Delete a recipe',
    '3': 'Print a recipe',
    '4': 'Print the cookbook',
    '5': 'Quit'
    """

if __name__ == "__main__":
    control = True
    print("Welcome to the Python cookbook!")
    print(options)
    while(control):
        print("Choose an option:")
        key = input()
        if key == "1":
            include_recipe()
        elif key == "2":
            print("Which recipe?")
            recipe_name = input()
            print(cookbook)
            erase_recipe(recipe_name)
        elif key == "3":
            print("Which recipe?")
            recipe_name = input()
            get_recipe(recipe_name)
        elif key == "4":
            print(cookbook)
        elif key == "5":
            print("Bye bye!")
            control = False