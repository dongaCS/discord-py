from discord.ext import commands

import random

class EightBall(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball') # change command name to 8ball 
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
            await ctx.reply('Ask me a question next time', mention_author=False)
        

async def setup(bot):
    await bot.add_cog(EightBall(bot))