import discord
from discord.ext import commands

import asyncio


class ADMIN(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(
        self,
        ctx,
        member: discord.Member = None,
        *,
        reason=None,
    ):
        if not member:
            await ctx.send(
                "No member was specified! Please use !kick <member> <reason>"
            )
            return
        author = ctx.author

        try:
            await member.kick(reason=reason)
            await ctx.send(
                f'{member.mention} was kicked by {author}. Reason: {reason}'
            )
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(
        self,
        ctx,
        member: discord.Member = None,
        *,
        reason=None,
    ):
        if not member:
            await ctx.send(
                "No member was specified! Please use !ban <member> <reason>"
            )
            return
        author = ctx.author

        try:
            await member.ban(reason=reason)
            await ctx.send(
                f'{member.mention} was banned by {author}. Reason: {reason}'
            )
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount = 100, *, member: discord.Member = None):
        print(member)
        if not member:
            deleted = await ctx.channel.purge(
                limit=int(amount)
            )
            await ctx.send(
                'Successfully cleared {} messages!'.format(
                    len(deleted)
                )
            )
            return
        else:
            deleted = -1
            for i in range(0, amount+1):
                await asyncio.sleep(.25)
                message = await ctx.channel.history().get(author=member)
                deleted += 1
                await message.delete()
            await ctx.send("Successfully cleared {} messages!".format(deleted))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member, *reason):
        '''Mutes specified user'''
        if member.guild_permissions.administrator:
            await ctx.send("Administrators cannot be muted!")
            return

        try:
            user = member
            role = discord.utils.get(
                user.guild.roles, name='Muted'
            )
            await user.add_roles(role)
        except Exception as e:
            await ctx.send(e)
        if reason:
            await member.send(
                "You have been muted by: {}\nReason: {}".format(ctx.author, ' '.join(reason))
            )
        else:
            await member.send("You have been muted by: {}".format(ctx.author))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member, *reason):
        '''Mutes specified user'''
        if member.guild_permissions.administrator:
            await ctx.send("Administrators cannot be muted!")
            return

        try:
            user = member
            role = discord.utils.get(
                user.guild.roles, name='Muted'
            )
            await user.remove_roles(role)
        except Exception as e:
            await ctx.send(e)

        if reason:
            await member.send(
                "You have been unmuted by: {}\nReason: {}".format(ctx.author, ' '.join(reason))
            )
        else:
            await member.send("You have been unmuted by: {}".format(ctx.author))


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def meck(self, ctx, member: discord.Member, amount=5):
        id = '<@186646663266304001>'
        while amount >= 0:
            asyncio.sleep(0.25)
            await ctx.send(f'{id}')
            await member.send(f'{id}')
            amount -= 1
            await member.m

def setup(client):
    client.add_cog(ADMIN(client))
