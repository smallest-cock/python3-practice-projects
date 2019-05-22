import discord
from discord import commands

class Admin(commands.Cog):
    pass

def setup(client):
    bot.add_cog(Admin(client))    
    