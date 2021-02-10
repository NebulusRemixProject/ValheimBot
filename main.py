import discord
from decouple import config
from discord.ext import commands
from modules.wikisearch import get_link
from modules.library import *


bot = commands.Bot(command_prefix=config('CMD_PREFIX'), description='I will help with Valheim')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Valheim", url="http://www.twitch.tv/"))
    print('My body is ready')

@bot.command()
async def search(ctx, query):
    (link_title, link_url) = get_link(query)
    if link_title == None:
        await ctx.send('Not found')
    else:
        embed = discord.Embed(
            title=link_title,
            description=link_url
        )

        await ctx.send(embed=embed)

@bot.command()
async def cauldron(ctx, msg):
    if (msg == ""):
            await msg.channel.send(", ".join(foods))
            return

    searchedMead = next((mead for mead in meads if mead.name.lower().find(msg.lower()) != -1), "")
    if (searchedMead != ""):
        embedVar = discord.Embed(title=searchedMead.name, description=searchedMead.description, color=0x00ff00)        
        for searchedMeadingredient in searchedMead.ingredients:
            if (searchedMeadingredient.itemType == ItemType.Food):
                ingredient = next(food for food in foods if food.name == searchedMeadingredient.name)
                embedVar.add_field(name="[" + searchedMeadingredient.amount + "] " + ingredient.name, value=ingredient.found, inline=True)
            if (searchedMeadingredient.itemType == ItemType.Ingredient):
                ingredient = next(ingredient for ingredient in ingredients if ingredient.name == searchedMeadingredient.name)
                embedVar.add_field(name="[" + searchedMeadingredient.amount + "] " + ingredient.name, value=ingredient.found, inline=True)
        await ctx.send(embed=embedVar)
    else:
        await ctx.send('Kunde inte hitta det du sökte')

bot.run(config('TOKEN'))
