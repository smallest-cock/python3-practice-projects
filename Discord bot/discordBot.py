# id 558404571446378516
# token NTU4NDA0NTcxNDQ2Mzc4NTE2.D3WpGw.G4tOf-H_77-qQykXEoKq_L9veg0
# permission integer 198720

# https://discordapp.com/oauth2/authorize?client_id=558404571446378516&scope=bot&permissions=198720


import discord
from random import randint
import asyncio
import time
import os
import ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

client = discord.Client()


async def post_challenge_background_task():
    await client.wait_until_ready()

    while not client.is_closed():
        try:
            with open("BeginnerChallenges.txt") as f:
                channel = client.get_channel(558403957408399362)
                text = f.read()
                challengeList = text.split('\n\n')
                randChall = challengeList[randint(0, len(challengeList) - 1)]
                await channel.send("```%s```" % randChall)

            await asyncio.sleep(3600)
        except Exception as e:
            print(str(e))
            await asyncio.sleep(3600)


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

client.run('NTU4NDA0NTcxNDQ2Mzc4NTE2.D3WpGw.G4tOf-H_77-qQykXEoKq_L9veg0')
