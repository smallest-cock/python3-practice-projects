import discord
from discord import commands

class SOS(commands.Cog):
    pass

def setup(client):
    client.add_cog(SOS(client))