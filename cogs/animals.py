from discord.ext import commands
import requests


class Animals(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # goodest dog, i'm not bias
    @commands.command()
    async def dog(self, ctx):
        url = "https://random.dog/woof.json"
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            img = data.get('url') # gets link from { url: link }
            await ctx.channel.send(img)
        else: 
            await ctx.reply('The dogs are out curing depression, please try again')
    
    # cat
    @commands.command()
    async def cat(self, ctx):
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            img = data[0].get('url') # [{ url: link }] so data[0]
            await ctx.channel.send(img)
        else: 
            await ctx.reply("The cats are ignoring you, please (don't) try again")

    # duck
    @commands.command()
    async def duck(self, ctx):
        url = "https://random-d.uk/api/v2/random"
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            img = data.get('url') 
            await ctx.channel.send(img)
        else: 
            await ctx.reply("The ducks went for a swim, please try again")

    # fox
    @commands.command()
    async def fox(self, ctx):
        url = "https://randomfox.ca/floof/"
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            img = data.get('image') 
            await ctx.channel.send(img)
        else: 
            await ctx.reply("The foxes are trying to say something, what is it? Please try again.")

async def setup(bot):
    await bot.add_cog(Animals(bot))