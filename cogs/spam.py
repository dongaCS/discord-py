from discord.ext import commands

class Spam(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spam(self, ctx, count, *args):
        limit = 10 # easy access for change
        num = int(count) # count is a string
        if num > limit:
            return await ctx.reply(f'No more than {limit}', mention_author=False)
        elif num <= 0:
            return await ctx.reply('Nice try, must be atleast 1', mention_author=False)
        
        message = ' '.join(args) # *args is a tuple, we make it a string
        for i in range(0, num):
            await ctx.send(f'{message}')


async def setup(bot):
    await bot.add_cog(Spam(bot))