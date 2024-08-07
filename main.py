import os
import asyncio
from dotenv import load_dotenv

import discord
from discord.ext import commands

import random # 8ball

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    print("-------------PY BOT RUNNING -------------")


async def setup_hook():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    async with bot:
        await setup_hook()
        load_dotenv() # set .env variables
        await bot.start(os.getenv("TOKEN"))


asyncio.run(main()) # loads the cogs and runs bot


