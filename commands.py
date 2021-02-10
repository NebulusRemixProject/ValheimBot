import discord
from decouple import config
from discord.ext import commands
from modules.wikisearch import get_link

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

bot.run(config('TOKEN'))

