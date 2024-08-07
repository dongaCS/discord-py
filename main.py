import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

import random # 8ball

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print("------------- BOT RUNNING -------------")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#.8ball works as well as .eightball
@bot.command(aliases=['8ball']) 
async def eightball(ctx):
    await ctx.send(random.choice([
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
    ]))

load_dotenv() # set .env variables
bot.run(os.getenv("TOKEN"))