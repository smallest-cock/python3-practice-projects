import discord
from discord.ext import commands


class faq(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def FAQ(self, ctx):
        '''The FAQ command: Sends a PM to the user with FAQ's'''
        author = ctx.message.author

        embed = discord.Embed(colour=discord.Colour.green())

        embed.set_author(name='FAQ')

        embed.add_field(
            name="Why can't I assign my rank?",
            value='If you are having troubles assigning your rank please double check your spelling '
            'if the issue persists contact a mod with @mod',
            inline=False,
        )

        embed.add_field(
            name="I found a bug what should I do?",
            value='If you encounter a bug please report it in the "Known Issues" channel. Or squish it.',
            inline=False,
        )

        embed.add_field(
            name="What are the rank requirements?",
            value='To view the rank requirements please use the !roadmap command',
            inline=False,
        )

        await author.send(embed=embed)


def setup(client):
    client.add_cog(faq(client))