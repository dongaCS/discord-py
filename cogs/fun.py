from discord.ext import commands

import random
import asyncio

class Fun(commands.Cog, description="Silly random commands to play with"):

    def __init__(self, bot):
        self.bot = bot


    ##############################
    ##  8ball
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
            await ctx.reply('Ask me a question or use ```.help 8ball```', mention_author=False)
        

    ##############################
    ##  GUESS 
    ##############################
    @commands.command(brief="Lets play a game", description="You win bragging rights")
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


    ##############################
    ##  SPAM
    ##############################
    @commands.command(brief="I'll spam for you", description="I'll spam it no more than 10 times")
    async def spam(self, ctx, num: int, *, message):
        limit = 10 # easy access for change
        
        if num > limit:
            return await ctx.reply(f'No more than {limit}', mention_author=False)
        elif num <= 0:
            return await ctx.reply('Nice try, must be atleast 1', mention_author=False)
        
        for i in range(0, num):
            await ctx.send(f'{message}')

    @spam.error
    async def load_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.reply('Pass me a number or use ```.help spam```', mention_author=False)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Pass me something to spam ```.help spam```', mention_author=False)









##############################
##  ADD COG
##############################
async def setup(bot):
    await bot.add_cog(Fun(bot))