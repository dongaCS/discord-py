import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print("------------- BOT RUNNING -------------")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


load_dotenv() # set .env variables
bot.run(os.getenv("TOKEN"))