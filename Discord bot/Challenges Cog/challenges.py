from discord.ext import tasks, commands
import discord
from random import randint
import asyncio


channelInfo = (('Beginner_Challenges.txt', 577314909218537473),
               ('Novice_Challenges.txt', 577314955460608010),
               ('Intermediate_Challenges.txt', 577314987727650817),
               ('Advanced_Challenges.txt', 577315037849583620),
               ('Expert_Challenges.txt', 577315155990282250))

postedList = []


class ChallengeCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.regular_posts.start()

    def cog_unload(self):
        self.regular_posts.cancel()

    @tasks.loop(minutes=1)
    async def regular_posts(self):
        modActionsChannel = self.client.get_channel(577326085289803776)
        await modActionsChannel.send('!dropchallenges')

    @regular_posts.before_loop
    async def before_regular_posts(self):
        print('waiting to post...')
        await self.client.wait_until_ready()

    @commands.Cog.listener()
    async def on_message(self, message):
        modActionsChannel = self.client.get_channel(577326085289803776)
        if "hello there" in message.content.lower():
            await message.channel.send("General Kenobi!")
        if "!dropchallenges" in message.content and message.channel == modActionsChannel:
            for channel in channelInfo:
                try:
                    with open(channel[0]) as f:  # opens text file that contains challenges
                        # channel ID number in parentheses
                        challengeChannel = self.client.get_channel(channel[1])
                        text = f.read()
                        # challenges must be separated by a blank line in the txt file
                        challengeList = text.split('\n\n')
                        tryAgain = False
                        while True:
                            # chooses random challenge from txt file
                            randChall = challengeList[randint(0, len(challengeList) - 1)]
                            if randChall not in postedList:  # posts the random challenge from txt file if it's new/unposted
                                # formats challenge with triple backticks
                                await challengeChannel.send("```%s```" % randChall)
                                # adds the newly posted challenge to the posted list to avoid a future repost
                                postedList.append(randChall)
                                break
                            for chall in challengeList:  # checks if there are any unposted challenges in the txt file
                                if chall not in postedList:
                                    # if an unposted challenge is found, allows the while loop to continue
                                    tryAgain = True
                                    break
                            if tryAgain is False:  # sends message if there are no unposted/new challenges found in the txt file
                                await modActionsChannel.send(":robot: I've ran out of new %s challenges. Please update my text file..." % channel[0].split('_')[0])
                                break
                except Exception as e:
                    print(str(e))

    @commands.command(pass_context=True)
    async def newchallenge(self, ctx):
        submitted = False
        for channel in channelInfo:
            level = channel[0].split('_')[0]
            if level.lower() in ctx.message.content.split("```")[0].lower():
                addedChall = ctx.message.content.split("```")[1]
                modActionsChannel = self.client.get_channel(577326085289803776)
                await modActionsChannel.send(f"{level} challenge submission:\n```{addedChall}```")
                submitted = True
        if submitted is True:
            await ctx.message.channel.send("Challenge submitted!")
            await ctx.message.add_reaction('🤖')
        else:
            await ctx.message.channel.send("Sorry, I couldn't submit that challenge :(")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        chann = self.client.get_channel(577326085289803776)
        mess = reaction.message.content
        try:
            if reaction.emoji == "❤" and reaction.message.channel == chann and "```" in mess:
                for channel in channelInfo:
                    level = channel[0].split('_')[0]
                    if level.lower() in mess.split(' submitted')[0].lower():
                        with open(channel[0], 'a') as txtFile:
                            txtFile.write('\n\n' + mess.split("```")[1])
                await chann.send("%s approved this %s.\n✍ It was added to the txt file" % (user.name, mess.split(' submitted')[0]))
            elif reaction.emoji == "💩" and reaction.message.channel == chann and "```" in mess:
                await chann.send("%s does not think this is a worthy %s." % (user.name, mess.split(' submitted')[0]))
        except Exception as e:
            print(f'***Error: {e}')


def setup(client):
    client.add_cog(ChallengeCog(client))
