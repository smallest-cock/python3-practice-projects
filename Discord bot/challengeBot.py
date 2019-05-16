# challenge bot for discord - posts challenges from a text file randomly at regular time intervals

import discord
from random import randint
import asyncio

client = discord.Client()

channelInfo = (('Beginner_Challenges.txt', 555767513930268683),
               ('Novice_Challenges.txt', 576870446545371161),
               ('Intermediate_Challenges.txt', 576870475955699758),
               ('Advanced_Challenges.txt', 576870519974920202),
               ('Expert_Challenges.txt', 576870496449069066))

postedList = []


async def post_challenge_background_task():
    await client.wait_until_ready()
    global postedList
    while not client.is_closed():
        for channel in channelInfo:
            try:
                with open(channel[0]) as f:  # opens text file that contains challenges
                    # channel ID number in parentheses
                    challengeChannel = client.get_channel(channel[1])
                    modActionsChannel = client.get_channel(553343591834189835)
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
                            await modActionsChannel.send("*bleep bloop* I've ran out of new %s challenges. Please update my text file..." % channel[0].split('_')[0])
                            break
            except Exception as e:
                print(str(e))
        await asyncio.sleep(120)  # time to wait between posts (in seconds) in parentheses


@client.event  # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    # Important logistics
    if '!oink' in message.content.lower():
        await message.channel.send("Oink is my middle name")
    elif "hello there" in message.content.lower():
        await message.channel.send("General Kenobi!")


client.loop.create_task(post_challenge_background_task())

client.run('tokengoeshere')  # server token in parentheses (and as a string)
