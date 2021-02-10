import discord
from decouple import config

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('!hi'):
        await msg.channel.send('Ohai')

client.run(config('TOKEN'))