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


@bot.event
async def on_ready():
    print("-------------PY BOT RUNNING -------------")


# load x cog
@bot.command(hidden=True) # hides from .help
async def load(ctx, extension):
    if str(ctx.author.id) in ADMIN:
        await bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded {extension}')


# unload x cog
@bot.command(hidden=True)
async def unload(ctx, extension):
    if str(ctx.author.id) in ADMIN:
        await bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded {extension}')


# reloads x cog
@bot.command(hidden=True)
async def reload(ctx, extension):
    if str(ctx.author.id) in ADMIN:
        await bot.unload_extension(f'cogs.{extension}')
        await bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded {extension}')


# loads cogs on start up
async def setup_hook(): 
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    async with bot:
        await setup_hook()
        await bot.start(os.getenv("TOKEN"))


asyncio.run(main()) # loads the cogs and runs bot


