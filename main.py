import discord
from decouple import config
from discord.ext import commands
from modules.wikisearch import get_link
from modules.cauldron import cauldron
from modules.comfort import comfort

bot = commands.Bot(command_prefix=config('CMD_PREFIX'), description='I will help with Valheim')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Valheim", url="http://www.twitch.tv/"))
    print('My body is ready')

@bot.command()
async def search(ctx, *, query):
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
async def helpme(ctx, query=None):
    if query is None:
        embed = bot_help()
    else:
        embed = bot_help(query)
    await ctx.send(embed=embed)

@bot.command(
    name="comfort", 
    brief="", #shown in ?help
    help="", 
    description="" #shown in ?help <command>
)
async def command_comfort(ctx, *, query=None):
    await ctx.send(comfort(query))

@bot.command(
    name="cauldron", 
    brief="Returns a list of all items that can be crafted in the cauldron", #shown in ?help
    #help="Test3", 
    description="Returns a list of all items that can be crafted in the cauldron" #shown in ?help <command>
)
async def command_cauldron(ctx, *, query = None):
    await ctx.send(cauldron(query))

bot.run(config('TOKEN'))
