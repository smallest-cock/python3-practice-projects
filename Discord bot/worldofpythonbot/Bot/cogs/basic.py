import discord
from discord.ext import commands


class Basics(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def submit(self, ctx):
        '''The Submit command: Replies to the user with the link for submissions'''
        await ctx.send(
            "Please upload your solution to the appropriate folder at: https://github.com/DevDact/World-of-Python"
        )

    @commands.command()
    async def rank(self, ctx, *rank):
        '''The !rank command: Applies requested rank to the user (if the rank is below the bot's rank)'''
        if len(rank) != 0:
            rank = rank[0]
            try:
                user = ctx.message.author
                rank = rank.capitalize()
                role = discord.utils.get(
                    user.guild.roles, name=rank
                )
                await user.add_roles(role)
            except Exception as e:
                await ctx.send(e)
        else:
            await ctx.message.author.send(
                "If you are unsure of what rank to assign use the !roadmap command to see which rank suits "
                "you best!"
            )

    @commands.Cog.listener()
    async def on_member_join(self, member):
        name = member.name

        embed = discord.Embed(
            colour=discord.Colour.blurple()
        )

        embed.set_author(
            name='Welcome '
            + name
            + ', to the World of Python Discord Server!'
        )

        embed.add_field(
            name='The goal of the server!',
            value='This server is a community designed for learning Python with other like-minded individuals '
            'here to help each other on our journey to learn programming.',
            inline=False,
        )

        embed.add_field(
            name='The Basic Rules!',
            value='Rule #1: If you have any problems with the server or a person use @mod to get help.\n'
            'Rule #2: Be respectful and helpful to others. We are all here to help each other learn.\n'
            'Rule #3: NO Racism, Spam, or Political/Religious Debate',
            inline=False,
        )

        # !roadmap and !requirements commands
        embed.add_field(
            name='Getting started!',
            value='To get started simply type !roadmap to view a list of the ranks and their requirements if you already '
            'know which rank you fall under type !rank <tier> to assign that rank to yourself (Ex. !rank Novice).',
            inline=False,
        )

        await member.send(embed=embed)


def setup(client):
    client.add_cog(Basics(client))