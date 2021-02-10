import discord
from decouple import config
from enum import Enum  

class ItemType(Enum):
    Food = 1,
    Ingredient = 2

class Food:
  def __init__(self, name, health, healing, stamina, duration, found):
    self.name = name
    self.health = health    
    self.healing = healing
    self.stamina = stamina
    self.duration = duration
    self.found = found

class Ingredient:
  def __init__(self, name, found):
    self.name = name
    self.found = found

class Mead:
  def __init__(self, name, description, ingredients):
    self.name = name
    self.description = description
    self.ingredients = ingredients

class MeadIngredient:
  def __init__(self, itemType, name, amount):
    self.itemType = itemType
    self.name = name
    self.amount = amount

foods = [
    Food("Raspberry", 10, 1, 20, 600, "Found in Meadows"),
    Food("Blueberry", 15, 1, 20, 600, "Found in Black Forest"),
    Food("Queens Jam", 30, 2, 40, 1200, "Crafted within a Cauldron"),
    Food("Cooked meat", 40, 2, 30, 1200, "By cooking raw meat in Cooking station"),
    Food("Mushroom", 15, 1, 20, 600, "Found in Meadows and Black Forest"),
    Food("Yellow Mushroom", 20, 1, 20, 600, "Found in crypt and dungeons within Black Forest and Swamp")
]

ingredients = [
    Ingredient("Bloodbag", "Dropped by Leeches found in the Swamp"),
    Ingredient("Honey", "Found in beehives"),
    Ingredient("Dandelion", "Found in Meadows")
]

meads = [
    Mead("Mead base: Medium healing", 
         "To get the potion you have to ferment your mead base in a fermenter, this takes a while.\n" +
         "You get 6 potions out of 1 mead base.",
        [
        MeadIngredient(ItemType.Ingredient, "Honey", "10"),
        MeadIngredient(ItemType.Ingredient, "Bloodbag", "4"),
        MeadIngredient(ItemType.Food, "Raspberry", "10"),
        MeadIngredient(ItemType.Ingredient, "Dandelion", "1")
    ])
]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('!cauldron '):
        await get_good(msg)
       

async def get_good(msg):
    if (msg.content[10:len(msg.content)] == ""):
        await msg.channel.send(", ".join(foods))
        return

    searchedMead = next((mead for mead in meads if mead.name.lower().find(msg.content[10:len(msg.content)].lower()) != -1), "")
    if (searchedMead != ""):
        embedVar = discord.Embed(title=searchedMead.name, description=searchedMead.description, color=0x00ff00)        
        for searchedMeadingredient in searchedMead.ingredients:
            if (searchedMeadingredient.itemType == ItemType.Food):
                ingredient = next(food for food in foods if food.name == searchedMeadingredient.name)
                embedVar.add_field(name="[" + searchedMeadingredient.amount + "] " + ingredient.name, value=ingredient.found, inline=False)
            if (searchedMeadingredient.itemType == ItemType.Ingredient):
                ingredient = next(ingredient for ingredient in ingredients if ingredient.name == searchedMeadingredient.name)
                embedVar.add_field(name="[" + searchedMeadingredient.amount + "] " + ingredient.name, value=ingredient.found, inline=False)
        await msg.channel.send(embed=embedVar)
    else:
        await msg.channel.send('Kunde inte hitta det du sökte')
    
client.run(config('TOKEN'))