from discord.ext import commands

import random
import asyncio
import discord
import os

class Fun(commands.Cog, description="Silly random commands to play with"):

    def __init__(self, bot):
        self.bot = bot


    ##############################
    ##  8ball
    ##############################
    @commands.command(name='8ball', brief="Ask me a question", description="Never wrong") # change command name to 8ball 
    async def eightball(self, ctx, question):
        await ctx.reply(random.choice([
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
    ]), mention_author=False)
            
    # must ask a question
    @eightball.error
    async def load_err(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Ask me a question or use ```.help 8ball```', mention_author=False)
        

    ##############################
    ##  GUESS 
    ##############################
    @commands.command(brief="Lets play a game", description="You win bragging rights")
    async def guess(self, ctx):
        await ctx.send("Guess a number between 1 and 10.")

        # our check function for wait_for()
        # check if same user
        # check if same channel
        # makes sure it's a number
        def is_correct(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id and m.content.isdigit()
        
        answer = random.randint(1, 10) # print(answer)

        # timer for user guessing
        try:
            guess = await self.bot.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await ctx.send('Times up, you`ll never know now.')

        # checks guess to answer
        if int(guess.content) == answer:
            await ctx.send('Correct!')
        else:
            await ctx.send(f'Wrong, it was {answer}')


    ##############################
    ##  SPAM
    ##############################
    @commands.command(brief="I'll spam for you", description="I'll spam it no more than 10 times")
    async def spam(self, ctx, num: int, *, message):
        limit = 10 # easy access for change
        
        if num > limit:
            return await ctx.reply(f'No more than {limit}', mention_author=False)
        elif num <= 0:
            return await ctx.reply('Nice try, must be atleast 1', mention_author=False)
        
        for i in range(0, num):
            await ctx.send(f'{message}')

    @spam.error
    async def load_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.reply('Pass me a number or use `.help spam`', mention_author=False)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Pass me something to spam or use `.help spam`', mention_author=False)


    ##############################
    ##  FIGHT
    ##############################
    @commands.command()
    async def fight(self, ctx, opponent: discord.Member):
        class Player: 
            def __init__(self, user):
                self.user = user
                self.hp = 100
            
            def take_damage(self, damage):
                self.hp -= damage

        if (opponent.bot and opponent.id == int(os.getenv("BOT"))): # if you dare challenge the almighty bot
            await ctx.send("You dare challenge me? Fine.")
            await ctx.send(f'**{opponent.name}** backhands {ctx.author.name}** and causes **9001** damage!')
            return await ctx.reply("https://tenor.com/view/filthy-frank-know-your-place-implicit-gif-26537479")
        
        if opponent.bot: # can't fight any bot
            return await ctx.send("You cannot challenge my people, peasant.")

        if ctx.author.id == opponent.id: # can't fight yourself
            return await ctx.send("You can't fight yourself, please consider calling `988` if you have negative thoughts. ❤️")

        def accept(m):
            return m.author.id == opponent.id and m.content == "accept"
        
        try:
            await ctx.send(f'<@{opponent.id}> type: `accept` to fight <@{ctx.author.id}>.')
            await self.bot.wait_for('message', check=accept, timeout=30.0)

            #setting up fight
            turn = 0
            player1 = Player(ctx.author.id) 
            player2 = Player(opponent.id) 
            rules = discord.Embed(
                        title = 'Fighting rules',
                        description = 'Take turns using: **light**, **medium** or **heavy** style attacks',
                        colour = discord.Colour.dark_gold()
                    )
            await ctx.send(embed=rules)
    
            # starting turn base attacks
            while (player1.hp > 0 and player2.hp > 0):
               
                # check functions for attack style
                def player1_stlye(m): 
                    return (m.content == "light" or m.content == "heavy" or m.content == "medium") and m.author.id == ctx.author.id
                
                def player2_stlye(m):
                    return (m.content == "light" or m.content == "heavy" or m.content == "medium") and m.author.id == opponent.id

                # calcs prop of attack style hitting
                def calc_damage(type):
                    if type == "light": # always hits
                        return 20
                    elif type == "medium" and random.random() <= .33: # 1 in 3
                        return 40
                    elif type == "heavy" and random.random() <= 0.125: # 1 in 8 
                        return 80
                    return 0
                
                if turn % 2 == 0: # player1 goes first
                    try:
                        style1 = await self.bot.wait_for('message', check=player1_stlye, timeout=5.0)
                        damage = calc_damage(style1.content) # calc damage player2 takes based on player1's attack
                        if damage:
                            player2.take_damage(damage) # deals damage if any
                            await ctx.send(f'**{ctx.author.name}** took **{damage}** damage! Leaving them with {player2.hp} hp.')
                        else:
                            await ctx.send(f'**{ctx.author.name}** missed') # roll for higher damage attack missed
                        turn += 1 # alternate turns
                    except asyncio.TimeoutError:
                        return await ctx.send(f"**{ctx.author.name}** has stopped responding. This is your win **{opponent.name}**.")       
                else:
                    try:
                        style2 = await self.bot.wait_for('message', check=player2_stlye, timeout=5.0)
                        damage = calc_damage(style2.content)
                        if damage:
                            player1.take_damage(damage) 
                            await ctx.send(f'**{opponent.name}** took **{damage}** damage! Leaving them with {player1.hp} hp.')
                        else:
                            await ctx.send(f'**{opponent.name}** missed')
                        turn += 1
                    except asyncio.TimeoutError:
                        return await ctx.send(f"**{opponent.name}** has stopped responding. This is your win **{ctx.author.name}**.")

            # end of turn base fighting and generating winner message
            winner = None
            loser = None
            if player1.hp > 0:
                winner = ctx.author
                loser = opponent
            else:
                winner = opponent
                loser = ctx.author

            banner = discord.Embed(
                        title = f'WINNER: {winner.name} ',
                        description = f'**{winner.name}** has pummeled **{loser.name}** into the the depths of shame.',
                        colour = discord.Colour.green()
                    )
            await ctx.send(embed=banner)

        except asyncio.TimeoutError: # error if "accept" wasn't typed 
            return await ctx.send(f"**{opponent.name}** didn't show. Coward.")

    @fight.error
    async def load_err(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.reply('Pass me someone to fight @user or use `.help fight`', mention_author=False)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('Pass me someone to fight with via ping or use `.help fight`', mention_author=False)









##############################
##  ADD COG
##############################
async def setup(bot):
    await bot.add_cog(Fun(bot))