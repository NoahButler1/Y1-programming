Recipe = []

RecipeName = input("what is the name of your recipe? ")
Name = "recipe:  " + str(RecipeName)
Recipe.append(Name)

PeopleServes = int(input("how many people does the recipe serve? "))
Serves = "serves:  " + str(PeopleServes)
Recipe.append(Serves)

NumberOfIngredients = int(input("how many ingredients does the recipe require? "))
for i in range (NumberOfIngredients):
    
    IngredientName = input("what is the name of the ingredient? ")
    Ingredient = "ingredient:  " + IngredientName
    Recipe.append(Ingredient)
    
    IngredientAmount = str(input("how much of the ingredient do you need? "))
    Amount = "amount:  " + IngredientAmount
    Recipe.append(Amount)

    IngredientUnit = input("what unit is that in (leave blank if none)? ")
    Unit = "unit:  " + IngredientUnit
    Recipe.append(Unit)
   


print(Recipe)
