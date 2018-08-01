print('Developer: Tugba Akan')
print('\n')      
print('Recipe Journal: A journal keeping your recipes in categories by the ingredients,')
print('letting you enter a new recipe,')
print('listing the recipes of the desired category')

#The recipes are taken from the website https://www.nefisyemektarifleri.com/

#Version 1 : The categories are in Turkish: 'Et yemekleri, Tavuk yemekleri, Sebze yemekleri'
print('\n')
print('if you would like to add a new recipe, put the text document into the folder that the code runs')
print('and run the code. It will load all the text documents including the new one.')
print('You can run the jupyter notebook')
print('or the py file from the command line')

#Python 3
#the subjects used in the code are : 
#importing text document and text mining
#object oriented programming
#Exception handling

#create a class for categories
class Category(object):
    def __init__(self, ID, name, keywords):
        self.ID = ID
        self.name = name
        self.keywords = keywords


cate1 = Category( ID = 1, name='Et yemekleri', keywords=[' et ', ' et\n', ' eti ', ' eti\n', 'kıyma',  'kıyması', 'kıyması'])
cate2 = Category( ID = 2, name='Tavuk yemekleri', keywords= ['tavuk'])
cate3 = Category( ID = 3, name='Sebze yemekleri', keywords= ['patlıcan', 'semiz', 'lahana', 'kabak'] )

categories = [cate1, cate2, cate3 ]

#create a class for recipes
class Recipe(object):
    def __init__(self,name, ingredients, categories):
        self.name = name
        self.ingredients = ingredients
        self.category = []
        self.setCategory(categories)
        
    #method to set the category of the recipe
    def setCategory(self, categories):
        for cate in categories:
            for ingr in self.ingredients:
                if any(kw in ingr for kw in cate.keywords):
                    self.category.append(cate.name)
                    break

#enter a new recipe as a txt document
#we assume max 20 recipes will be given
recipes = []
for i in range(1,20):
    try:
        with open('tarif' + str(i) + '.txt', 'r') as f:
            new_recipe = f.readlines()
            rec = Recipe(name=new_recipe[0], ingredients = new_recipe[4::], categories = categories)
            recipes.append(rec)
    except IOError:
        # This will only check for an IOError exception and then execute this print statement
        print( "Error: Could not find file or read data" )
    else:
        print( "Content written successfully" )

#print the categories
#for item in categories:
#    print(item.name)

#print the name and the categories of the recipes
#for item in recipes:
#    print(item.name)
#    print(item.category)

#list the recipes in the desired category
print('Type the number of the category you wish to be listed')
for item in categories:
    print( str(item.ID) + ' for ' + item.name)
inp_cate_ID = input('')
for item in categories:
    if item.ID == int(inp_cate_ID):
        print(item.name)
        for item2 in recipes:
            for item3 in item2.category:
                if item3 == item.name:
                    print(item2.name)

                    