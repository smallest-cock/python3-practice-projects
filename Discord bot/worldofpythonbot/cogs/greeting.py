import discord
from discord import commands

class Greeting(commands.Cog):
    pass

def setup(client):
    client.add_cog(Greeting(client))