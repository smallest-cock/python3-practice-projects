# challenge bot for discord - posts challenges from a text file randomly at regular time intervals

import discord
from random import randint
import asyncio

client = discord.Client()

postedList = []


async def post_challenge_background_task():
    await client.wait_until_ready()
    global postedList
    while not client.is_closed():
        try:
            with open("BeginnerChallenges.txt") as f:  # text file that contains challenges
                channel = client.get_channel(channelIDnumbergoeshere123)  # channel ID # in parentheses
                text = f.read()
                # challenges must be separated by a blank line in txt file
                challengeList = text.split('\n\n')
                keepLooking = True
                tryAgain = False
                while keepLooking is True:
                    randChall = challengeList[randint(0, len(challengeList) - 1)]
                    if randChall not in postedList:
                        await channel.send("```%s```" % randChall)
                        postedList.append(randChall)
                        keepLooking = False
                        break
                    for chall in challengeList:
                        if chall not in postedList:
                            tryAgain = True
                            break
                    if keepLooking is True and tryAgain is False:
                        await channel.send("Oops. I've ran out of new challenges. Please update my text file... *bleep bloop*")
                        break
                    elif tryAgain is True:
                        continue

            await asyncio.sleep(86400)  # time to wait between posts (in seconds) in parentheses
        except Exception as e:
            print(str(e))
            await asyncio.sleep(86400)  # time to wait between posts (in seconds) in parentheses


@client.event  # event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if '!oink' in message.content.lower():
        await message.channel.send("Oink oink oink!")
    elif "hello there" in message.content.lower():
        await message.channel.send("General Kenobi!")


client.loop.create_task(post_challenge_background_task())

client.run('tokengoeshere')  # server token in parentheses (and as a string)
