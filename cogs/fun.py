from discord.ext import commands

import random
import discord
import requests
import asyncio
import os

class Fun(commands.Cog, description="Random silly commands to play with"):

    def __init__(self, bot):
        self.bot = bot


    ##############################
    ##  8BALL
    ##############################
    @commands.command(name='8ball', brief="Ask me a question", description="Never wrong") # change command name to 8ball 
    async def eightball(self, ctx, question):
        await ctx.reply(random.choice([
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",      
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",      
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",      
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",   
        "Very doubtful."
    ]), mention_author=False)
            
    # must ask a question
    @eightball.error
    async def load_err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Ask me a question or use `.help 8ball`', mention_author=False)
        

    ##############################
    ##  SPAM
    ##############################
    @commands.command(brief="I'll spam for you", description="I'll spam it no more than 10 times")
    async def spam(self, ctx, number: int, *, message):
        limit = 10 # easy access for change
        
        if number > limit:
            return await ctx.reply(f'No more than {limit}', mention_author=False)
        elif number <= 0:
            return await ctx.reply('Nice try, must be atleast 1', mention_author=False)
        
        for i in range(0, number):
            await ctx.send(f'{message}')

    @spam.error
    async def load_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.reply('Pass me a number or use `.help spam`', mention_author=False)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Pass me how many times to spam and something to spam or use `.help spam`', mention_author=False)


    ##############################
    ##  CHOOSE
    ##############################
    @commands.command(brief="I'll pick for you", description="I won't rig it, promise, I also take bribes.")
    async def choose(self, ctx, *, choices):
        str = choices.split(",")
        if len(str) < 2:
            return await ctx.send('Must have atleast two choices, use comma to split them.')
        
        await ctx.send(random.choice(str))

    @choose.error
    async def load_err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Must pass me something to choose between or use `.help choose`", mention_author=False)


    ##############################
    ##  RANDOM
    ##############################
    @commands.command(brief="I'll give you random number", description="Get a random number between 1 and 100")
    async def random(self, ctx):
        await ctx.send(random.randrange(1, 100))


    ##############################
    ##  FLIP
    ##############################
    @commands.command(brief="I'll flip a coin", description="Ultimate decision making via coin flip")
    async def flip(self, ctx):
        await ctx.send(random.choice(['heads', 'tails']))


    ##############################
    ##  ROAST
    ##############################
    @commands.command(breif="Lighthearted jokes", description="I will fight your fights for you")
    async def roast(self, ctx, target: discord.Member):
        url = os.getenv('ROAST_API')

        try:
            response = requests.get(url, timeout=10)
        except asyncio.TimeoutError:
            return await ctx.send('Server error, please try again later')

        if response.status_code == 200:
            data = response.json()
            await ctx.send(f'<@{target.id}> {data.get("roast")}')
        else: # api error 
            await ctx.reply("Ahh the a duck was accidentally sent, please try again")

    @roast.error
    async def load_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.reply('Pass me someone to roast @user or use `.help fight`', mention_author=False)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Pass me someone to roast with via ping or use `.help fight`', mention_author=False)




##############################
##  ADD COG
##############################
async def setup(bot):
    await bot.add_cog(Fun(bot))