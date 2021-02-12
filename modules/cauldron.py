from discord import Embed
from .library import meads, ingredients

def cauldron(query=None):
    if query is None:
        allMaeds = ""
        for mead in meads:
            if (allMaeds != ""):
                allMaeds = allMaeds + ", "
            allMaeds = allMaeds + mead.name        
        return allMaeds  

    searchedMead = next((mead for mead in meads if mead.name.lower().find(query.lower()) != -1), None)
    if (searchedMead is not None):
        #embedVar = Embed(title=searchedMead.name, description=searchedMead.description, color=0x00ff00)    
        #for searchedMeadingredient in searchedMead.ingredients:
        #    ingredient = next(ingredient for ingredient in ingredients if ingredient.name == searchedMeadingredient.name)
        #    embedVar.add_field(name="[" + searchedMeadingredient.amount + "] " + ingredient.name, value=ingredient.found, inline=False)            
        #return embedVar
        embedVar = "```\n"
        embedVar = embedVar + searchedMead.name + "\n"
        embedVar = embedVar + searchedMead.description + "\n"
        for searchedMeadingredient in searchedMead.ingredients:
            ingredient = next(ingredient for ingredient in ingredients if ingredient.name == searchedMeadingredient.name)
            #embedVar = embedVar + "[" + searchedMeadingredient.amount + "] " + ingredient.name + ". " + ingredient.found + "\n" 
            embedVar = "{0} [{1:>2}] {2:<13}  {3}\n".format(embedVar, searchedMeadingredient.amount, ingredient.name, ingredient.found) 
        embedVar = embedVar + "```"
        return embedVar
    else:
        return 'Not found'