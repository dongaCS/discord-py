from discord.ext import commands
import random
import asyncio

class Guess(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guess(self, ctx):
        await ctx.send("Guess a number between 1 and 10.")

        # our check function for wait_for()
        # check if same user
        # check if same channel
        # makes sure it's a number
        def is_correct(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id and m.content.isdigit()
        
        answer = random.randint(1, 10) # print(answer)

        # timer for user guessing
        try:
            guess = await self.bot.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await ctx.send('Times up, you`ll never know now.')

        # checks guess to answer
        if int(guess.content) == answer:
            await ctx.send('Correct!')
        else:
            await ctx.send(f'Wrong, it was {answer}')


async def setup(bot):
    await bot.add_cog(Guess(bot))

