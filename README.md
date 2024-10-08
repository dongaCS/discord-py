# Discord Bot in PY
playing with discord bot in python

## Table of Contents
- [Setting up Python](#Setting-up-Python)
  - Installing Python
  - Virtual Environments (venv)
  - Dependencies
- [Setting up Discord App](#Setting-up-Discord-App)
  - Discord Account
  - Discord Bot Token
  - Running it Locally
- [The Bot](#The-Bot)
  - Commands
  - Commands for Dev
  - Commands for Mods
  - Command Takeaway
- [Future Commands](#Future-Commands)

## Setting up Python
### Installing Python
MacOS already comes with Python3 (system python, don't mess with it)
- To check current python verison open the terminal and type `python --verison`
- returns something like: `Python 3.9.6` 
  
We want a fresh install, of the latest verison of Python3 as 3.9's support is ending this year
- This project will use [Python 3.12.4 64-bit](https://www.python.org/downloads/)
- The version should change by itself, we can check by typing `python --verison`
- We can also look at the path by using command `which python3`
- returns: **/Library/Frameworks/Python.framework/Versions/3.12/bin/python3**
- Make sure at the end of the install to get the **certificate file** with (Install Certificates.command) in folder

---
### Virtual Environments (venv)
Because Python installs are system wide, if we were to install say NumPy 1.23 we won't be able to run version 1.26. If we want to installed 1.26 then we have to uninstall 1.23. This could lead to problems as the updated version may have new implementations of functions we used in our project. Ultimately it would cause us to reinstall 1.23 and 1.26 whenever we switch projects. **Virtual Environments** create a separate, isolated instance of the Python runtime for a project each with its own complement of packages.

#### Why venv
- Running with the system (path) Python and libraries limits us to one specific Python version
- Running all Python applications on one Python installation can lead to version conflicts
- venv is are ways to self-contain Python installs

---
#### Setting up Virtual Environment
1. In the folder make a file called `main.py`
2. Set the Python Interpreter to 3.12.4
3. Open a terminal at folder path and do command
```
python3 -m venv .ENV_DIR
```
   - .ENV_DIR is the folder name (don't forget to add to .gitignore)
   - In our project folder there should be a folder called `.ENV_DIR`
4. A prompt: **We noticed a new environment has been created. Do you want to select it for the workspace folder?**
   - Click **Yes**

![steps.png](https://github.com/dongaCS/discord-py/blob/main/images/step%20.png?raw=true)
- Open a new terminal and see if its (.ENV_DIR) CURRENT_PATH % then its activate
  
![active.png](https://github.com/dongaCS/discord-py/blob/main/images/active.png?raw=true)

- To exit out of the venv do command `deactivate` and (.ENV_DIR) should disappear
- To reactivate, open a new terminal at folder

---
### Dependencies
#### (.ENV_DIR) CURRENT_PATH % Installs
1. [discord.py 2.4.0](https://pypi.org/project/discord.py/)
```
python3 -m pip install -U discord.py
```
2. [python-dotenv 1.0.1](https://pypi.org/project/python-dotenv/)
```
pip3 install python-dotenv
```

---
#### Python dependencies are defined in: requirements.txt
```
pip3 freeze > requirements.txt
``` 
- will create txt file and save all our python libraries

## Setting up Discord App
### Discord Account 
In order to make a Discord Bot, we need a create a [Discord Account](https://discord.com/login)

---
### Discord Bot Token 
- Follow this to setup Bot and Token from [Discord.py](https://discordpy.readthedocs.io/en/stable/discord.html)

---
### Running it Locally
Starting code for main.py
```Python
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents) # prefix that comes before a command

@bot.event
async def on_ready():
    print("------------- BOT RUNNING -------------") # prints in terminal

@bot.command()
async def ping(ctx): # command called ping => .ping 
    await ctx.send('pong')

load_dotenv() # set .env variables
bot.run(os.getenv("TOKEN"))
```
To run the Bot, keep the terminal open and do command:
- `python3 main.py`
- returns: ------------- BOT RUNNING -------------

## The Bot 
### Commands for Users
| Command | Description |
| --- | --- |
| `8ball <question>` | ask it a *question* and get an answer |
| `spam <number> <message>` | spams a the *message* some *number* of times, max is 10|
| `guess` | play a guessing game |
| `dog` | get an image of a dog |
| `cat` | get an image of a cat |
| `duck` | get an image of a duck |
| `fox` | get an image of a fox |
| `fight <opponent>` | ping the *opponent* you want to fight |
| `trivia` | asks a trivia question |
| `choose <choices>` | picks one of the choices, seperate by comma |
| `random` | generates a random number between 1 and 100 |
| `flip` | flip a coin |
| `roast <target>` | ping the *target* you want to roast |
| `help` | get information about commands |

---
### Commands for Devs
| Command | Description |
| --- | --- |
| `ping` | sends back pong |
| `load <file_name>` | loads a cog |
| `unload <file_name>` | unloads a cog |
| `reload <file_name>` | reloads a cog |
| `quit` | shuts down the bot |
- Cogs are like modules/extensions for discord.py bots. They are used to organize commands, listeners and states into a class. In addiction, say we want to work on a function for our bot but don't want any downtime. We can use cogs to unload said function and then load it after updating the function. It's super useful for testing since we don't have to shutdown and reboot the bot each time we need to make small adjustments to the code.

---
### Commands for Mods
| Command | Description |
| --- | --- |
| `on_message_edit` | sends a copy of edited message to designated channel |
| `on_message_delete` | sends a copy of deleted message to designated channel |
- These commands are for making moderation of the server easier.

---
### Command Takeaway 
| Command | Takeaway |
| --- | --- |
| ping | - simple user command to check for response from bot |
| 8ball | - altering command name to not be function name <ul><li> ie) @commands.command(aliases=['8ball']) </li><li> ie) @commands.command(name='8ball') </li></ul> - replying to user message |
| spam | - sending multiple response back <br> - playing with multi arguments <ul><li>async def spam(self, ctx, number: int, *, arg):</li></ul>  - error handling <ul><li>`nummber: int` allows for commands.BadArgument error handling</li><li>`*, arg` allows for commands.MissingRequiredArgument</li></ul>
| guess |   - user interaction, waiting for user response<br> - time out function for if user takes too long
| quit | - hidden commands <ul><li> ie) @bot.command(hidden=True) </li></ul> - user base commands (admin only)
| load, unload, reload | - how to use cogs
| dog, cat, duck, fox | - `pip3 install requests`<br> - how to make api request |
| on_message_delete/edit | - built in discord event listener<br> - sending message in different channel<br> - discord embeds
| help | - `pip3 install discord-pretty-help`<br> - built in discord command<br> - description for cogs<br> - brief and description for commands |
| fight | - multi user interactions<br> - classes in commands |
| trivia | - processing api request with different types of payload |
| roast | - there was no free roast api just ai's<br> - made my own [api](https://roast-api.dongacs.workers.dev/) for the command
TO BE UPDATED

## Future Commands
- dog (DONE) => get image of dog (best pet) also added cat, duck and fox
  - pip3 install requests
  - pip3 freeze > requirements.txt
- clip (DONE - dev only) => sometimes people say things and then delete or edit, but i'm clipping it
- help (DONE) => improve the basic help menu
  - pip3 install discord-pretty-help
  - pip3 freeze > requirements.txt
- dm => sometimes the mods doesnt want to be the one to break the news so we send the bot
- fight (DONE) => someone wronged you, challenge them to a virtual fight
- trivia (DONE) => prove you have high IQ
- roast (DONE) => sometimes life isn't about food, it's about taking it easy
- pfp => can't see your friend's image, say less, we zoom in 
- currency system => i want to gamble but with infinite funds
