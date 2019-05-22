import discord
from discord.ext import commands


class roadmap(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def roadmap(self, ctx, *rank):
        '''The !roadmap command: Sends the user a PM with all of the rank requirements or a specific ranks requirements'''
        author = ctx.message.author

        embed = discord.Embed(colour=discord.Colour.blue())

        embed.set_author(name='Rank Roadmap')

        # Check to see if they want a specific rank requirements
        if len(rank) != 0:
            # If there is more than one arg use the first
            rank = rank[0]

            # Check which rank they want and embed the embed with the requirements.
            if rank.lower() == 'beginner':
                embed.add_field(
                    name='Beginner Requirements!',
                    value='This role is designed for people with little to no programming experience',
                    inline=False,
                )
            elif rank.lower() == 'novice':
                embed.add_field(
                    name='Novice Requirements!',
                    value='The REPL\nMathematical Operations\nBasic use of IDLE, explain what an IDE is\nprint()\ninput()\nrandom()\nCommenting\n'
                    'Basic knowledge of int, float, str, and booleans\nString manipulation\nHow to user variables\nCommon operators\n'
                    'If/Else/Elif\nFor/While loops\nImporting\nLists and Dictionaries\nDebugging',
                    inline=False,
                )
            elif rank.lower() == 'intermediate':
                embed.add_field(
                    name='Intermediate Requirements!',
                    value='Classes:\n---> Common dunder methods\n---> Inheritance (Parent/Child)\n---> Attributes\n---> Polymorphism\n---> Encapsulation\n'
                    '---> Everything is an object\n---> Statis Vs. Class methods\n---> super()\n---> Instantiation\nFile Manipulation (Read/Write)\n'
                    'List Comprehensions\nGenerators\nNesting\nError Handling\nAbsolute Vs. Relative Imports\nUsing the docs\nLogging/Debugging\n'
                    'Passing arguments to parameters (positionally or explicitly)\nConfig files\nSerialization\nUnit Testing\nScope\nPEP8',
                    inline=False,
                )
            elif rank.lower() == 'advanced':
                embed.add_field(
                    name='Advanced Requirements!',
                    value='Concurrency:\n---> Asynchronous\n---> Multi-threading/Multi-Processing\n---> GIL\n---> Continous Integration/Continous Deployment\n'
                    'Networking:\n---> Sockets (SocketsIO)\nRecursive\nAPIs\n---> REST\nRuntime Services\nMagic Methods\n---> Descriptors\n---> call()\n'
                    'Linked Lists\nImmutability\nMemory Management\n---> Caching\n---> Weak References\n---> Memoization\nArgparse\nPydoc\nMetaprogramming\nItertools',
                    inline=False,
                )
            elif rank.lower() == 'expert':
                embed.add_field(
                    name='Expert Requirements!',
                    value='Web Developer\n---> Django\n---> Flask\n---> Full Stacks (LAMP)',
                    inline=False,
                )
            # else the input is not a valid rank
            else:
                embed.add_field(
                    name='Invalid Rank',
                    value='Check your spelling and try again',
                    inline=False,
                )
            await author.send(embed=embed)
        # Else there is no specific request embed and send all
        else:
            # Beginner
            embed.add_field(
                name='Beginner Requirements!',
                value='This role is designed for people with little to no programming experience',
                inline=False,
            )

            # Novice
            embed.add_field(
                name='Novice Requirements!',
                value='The REPL\nMathematical Operations\nBasic use of IDLE, explain what an IDE is\nprint()\ninput()\nrandom()\nCommenting\n'
                'Basic knowledge of int, float, str, and booleans\nString manipulation\nHow to user variables\nCommon operators\n'
                'If/Else/Elif\nFor/While loops\nImporting\nLists and Dictionaries\nDebugging',
                inline=False,
            )

            # Intermediate
            embed.add_field(
                name='Intermediate Requirements!',
                value='Classes:\n---> Common dunder methods\n---> Inheritance (Parent/Child)\n---> Attributes\n---> Polymorphism\n---> Encapsulation\n'
                '---> Everything is an object\n---> Statis Vs. Class methods\n---> super()\n---> Instantiation\nFile Manipulation (Read/Write)\n'
                'List Comprehensions\nGenerators\nNesting\nError Handling\nAbsolute Vs. Relative Imports\nUsing the docs\nLogging/Debugging\n'
                'Passing arguments to parameters (positionally or explicitly)\nConfig files\nSerialization\nUnit Testing\nScope\nPEP8',
                inline=False,
            )

            # Advanced
            embed.add_field(
                name='Advanced Requirements!',
                value='Concurrency:\n---> Asynchronous\n---> Multi-threading/Multi-Processing\n---> GIL\n---> Continous Integration/Continous Deployment\n'
                'Networking:\n---> Sockets (SocketsIO)\nRecursive\nAPIs\n---> REST\nRuntime Services\nMagic Methods\n---> Descriptors\n---> call()\n'
                'Linked Lists\nImmutability\nMemory Management\n---> Caching\n---> Weak References\n---> Memoization\nArgparse\nPydoc\nMetaprogramming\nItertools',
                inline=False,
            )

            # Expert
            embed.add_field(
                name='Expert Requirements!',
                value='Web Developer\n---> Django\n---> Flask\n---> Full Stacks (LAMP)',
                inline=False,
            )

            await author.send(embed=embed)


def setup(client):
    client.add_cog(roadmap(client))