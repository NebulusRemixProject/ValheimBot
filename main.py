import discord
from decouple import config

foods = ["Raspberry", "Blueberry", "Queens Jam"]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('!food '):
        await get_good(msg)
       

async def get_good(msg):
    if (msg.content[6:len(msg.content)] == ""):
        await msg.channel.send(", ".join(foods))
        return

    await msg.channel.send('Ohai2')

client.run(config('TOKEN'))