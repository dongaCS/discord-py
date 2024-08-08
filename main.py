import os
import asyncio
from dotenv import load_dotenv

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

load_dotenv() # set .env variables
ADMIN = [os.getenv("TEMP_ACC"), os.getenv("ALT_ACC")]


# simple ping 
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

'''
BOT START AND EXIT
'''
@bot.event
async def on_ready():
    print("------------- PY BOT RUNNING -------------")

# shutdown bot
@bot.command(hidden=True) # hides from .help
async def exit(ctx):
    if str(ctx.author.id) in ADMIN:
        await ctx.send('**Ciao**')
        await bot.close()
    else:
        await ctx.send('**No, you**')

# loads cogs on start up
async def setup_hook(): 
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    async with bot:
        await setup_hook()
        await bot.start(os.getenv("TOKEN"))


'''
COGS
'''
# load x cog
@bot.command(hidden=True) 
async def load(ctx, extension):
    if str(ctx.author.id) in ADMIN:
        await bot.load_extension(f'cogs.{extension}')
        await ctx.reply(f'Loaded {extension}', mention_author=False)

# unload x cog
@bot.command(hidden=True)
async def unload(ctx, extension):
    if str(ctx.author.id) in ADMIN:
        await bot.unload_extension(f'cogs.{extension}')
        await ctx.reply(f'Unloaded {extension}', mention_author=False)

# reloads x cog
@bot.command(hidden=True)
async def reload(ctx, extension):
    if str(ctx.author.id) in ADMIN:
        await bot.unload_extension(f'cogs.{extension}')
        await bot.load_extension(f'cogs.{extension}')
        await ctx.reply(f'Reloaded {extension}', mention_author=False)


'''
ERROR HANDLING
'''
@load.error
async def load_err(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Which cog file?", mention_author=False)

@unload.error
async def reload_err(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Which cog file?", mention_author=False)

@reload.error
async def unload_err(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Which cog file?", mention_author=False)


'''
STARTS THE BOT
'''
asyncio.run(main()) # loads the cogs and runs bot