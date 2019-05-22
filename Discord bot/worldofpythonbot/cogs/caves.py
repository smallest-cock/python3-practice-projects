import discord
from discord import commands

class Caves(commands.Cog):
    pass

def setup(client):
    client.add_cog(Caves(client))