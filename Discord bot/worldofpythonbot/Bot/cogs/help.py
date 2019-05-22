import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour=discord.Colour.blurple()
        )

        embed.set_author(name='Help has arrived!')

        embed.add_field(
            name='!FAQ',
            value='Displays a list of Frequently Asked Questions',
            inline=False,
        )

        embed.add_field(
            name='!rank',
            value='Assigns the user with the specified rank. Ex: !rank Beginner',
            inline=False,
        )

        embed.add_field(
            name='!roadmap',
            value='Displays the requirements for all of the ranks or if passed a rank display the given ranks requirements. '
            'Ex: !roadmap Novice',
            inline=False,
        )

        embed.add_field(
            name='!submit',
            value='Replies with a link to submit your challenge solution',
            inline=False,
        )

        await author.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def admin_help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour=discord.Colour.blurple()
        )

        embed.set_author(name='Admin Commands!')

        embed.add_field(
            name='!ban',
            value='Bans a specified user',
            inline=False,
        )

        embed.add_field(
            name='!kick',
            value='Kicks a specified user',
            inline=False,
        )

        embed.add_field(
            name='!clear',
            value='Clears text in channel (default 100 messages) You can also specify the number and whos'
                  'messages you want deleted. Ex: !clear 5 @Natesc',
            inline=False,
        )

        embed.add_field(
            name='!mute',
            value="Mute's a user so they cannot use voice or text chat.",
            inline=False,
        )

        embed.add_field(
            name='!unmute',
            value="Unmute's a user so they can use the chat's again.",
            inline=False,
        )

        await author.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))