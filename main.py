import discord
from decouple import config
from modules.library import *

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
