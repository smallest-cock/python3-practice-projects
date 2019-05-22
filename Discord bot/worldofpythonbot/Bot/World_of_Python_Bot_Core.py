import discord
from discord.ext import commands
import asyncio

TOKEN = 'NTc5MDA0Njg3NjQzMzEyMTQ4.XN72Jw.6m1nn6vTn78m8ugd4SEOpa_eUaM'

# The character used to call commands
client = commands.Bot(command_prefix='!')
client.remove_command('help')

'''Names of the cogs.
Make sure to add your cog to this list for it to work properly'''
extensions = ['basic', 'faq', 'roadmap', 'help', 'admin', 'challenges']
extensions = ['cogs.' + name for name in extensions]

if __name__ == '__main__':
    try:
        for extension in extensions:
            client.load_extension(extension)
            print(f'Loaded {extension}')
    except Exception as e:
        print(f'{extension} cannot be loaded: {e}')


@client.event
async def on_ready():
    print(
        str(client.user.name)
        + " is online\nVersion: "
        + discord.__version__
    )
    print("------")


client.run(TOKEN)
