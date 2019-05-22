import discord
from discord import commands

class Cave(commands.Cog):
    pass

def setup(client):
    client.add_cog(Cave(client))