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



@bot.command()
async def spam(ctx, count, *args):
    limit = 10 # easy access for change
    num = int(count) # count is a string
    if num > limit:
        return await ctx.reply(f'No more than {limit}', mention_author=False)
    elif num <= 0:
        return await ctx.reply('Nice try, must be atleast 1', mention_author=False)
    
    message = ' '.join(args) # *args is a tuple, we make it a string
    for i in range(0, num):
        await ctx.send(f'{message}')
        

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


