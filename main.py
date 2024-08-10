import os
import asyncio
from dotenv import load_dotenv

import discord
from discord.ext import commands
from pretty_help import EmojiMenu, PrettyHelp


##############################
##  BOT INIT and QUIT
##############################
intents = discord.Intents.default()
intents.message_content = True
# intents.members = True
intents.guilds = True # for seeing channels
bot = commands.Bot(command_prefix='.', intents=intents)

load_dotenv() # set .env variables
ADMIN = [os.getenv("TEMP_ACC"), os.getenv("ALT_ACC")]

@bot.event
async def on_ready():
    print("------------- PY BOT RUNNING -------------")

# shutdown bot
@bot.command(hidden=True, aliases=['q', 'exit']) # hides from .help
async def quit(ctx):
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


##############################
##  COGS
##############################
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
@bot.command(hidden=True, aliases=['r'])
async def reload(ctx, extension):
    if str(ctx.author.id) in ADMIN:
        await bot.unload_extension(f'cogs.{extension}')
        await bot.load_extension(f'cogs.{extension}')
        await ctx.reply(f'Reloaded {extension}', mention_author=False)

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


##############################
##  HELP
##############################
color = discord.Color.red()
menu = EmojiMenu(page_left="⬅️", page_right="➡️", remove="❌", active_time=30)
# updates help settings
bot.help_command = PrettyHelp(color=color, menu=menu)


##############################
##  START BOT
##############################
# simple ping for connection testing
@bot.command(hidden=True)
async def ping(ctx):
    await ctx.send('pong')

asyncio.run(main()) # loads the cogs and runs bot