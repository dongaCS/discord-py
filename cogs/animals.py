from discord.ext import commands
import requests


class Animals(commands.Cog, description="Stare into the void except at animal images"):

    def __init__(self, bot):
        self.bot = bot


    ##############################
    ##  DOG
    ##############################
    @commands.command(brief="The goodest boy and girl", description="Get a random dog")
    async def dog(self, ctx):
        url = "https://random.dog/woof.json"
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            img = data.get('url') # gets link from { url: link }
            await ctx.channel.send(img)
        else: 
            await ctx.reply('The dogs are out curing depression, please try again')
    

    ##############################
    ##  CAT
    ##############################
    @commands.command(brief="It's a cat", description="Disturb a random cat")
    async def cat(self, ctx):
        url = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            img = data[0].get('url') # [{ url: link }] so data[0]
            await ctx.channel.send(img)
        else: 
            await ctx.reply("The cats are ignoring you, please (don't) try again")


    ##############################
    ##  DUCK
    ##############################
    @commands.command(brief="Quack Quack!", description="Talk to the random duck and debug code")
    async def duck(self, ctx):
        url = "https://random-d.uk/api/v2/random"
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            img = data.get('url') 
            await ctx.channel.send(img)
        else: 
            await ctx.reply("The ducks went for a swim, please try again")


    ##############################
    ##  FOX 
    ##############################
    @commands.command(brief="Wa-pa-pa-pa-pa-pa-pow!", description="That's what the random fox is going to say")
    async def fox(self, ctx):
        url = "https://randomfox.ca/floof/"
        response = requests.get(url) 

        if response.status_code == 200:
            data = response.json()
            img = data.get('image') 
            await ctx.channel.send(img)
        else: 
            await ctx.reply("The foxes are trying to say something, what is it? Please try again.")


##############################
##  ADD COG
##############################
async def setup(bot):
    await bot.add_cog(Animals(bot))