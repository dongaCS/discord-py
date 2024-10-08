from discord.ext import commands

import os
import random
import asyncio
import discord
import requests

ADMIN = [os.getenv("TEMP_ACC"), os.getenv("ALT_ACC")]

class Games(commands.Cog, description="It's game night."):

    def __init__(self, bot):
        self.bot = bot


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
            await ctx.send(f'Wrong, it was **{answer}**')


    ##############################
    ##  FIGHT
    ##############################
    @commands.command(brief="1v1 someone", description="Got beef with someone? Settle it here.")
    async def fight(self, ctx, opponent: discord.Member):
        class Player: 
            def __init__(self, user):
                self.user = user
                self.hp = 100
            
            def take_damage(self, damage):
                self.hp -= damage

        if (opponent.bot and opponent.id == int(os.getenv("BOT"))): # if you dare challenge the almighty bot
            await ctx.send("You dare challenge me? Fine.")
            await ctx.send(f'**{opponent.name}** backhands **{ctx.author.name}** and causes **9001** damage!')
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
                    return (m.content == "light" or m.content == "medium" or m.content == "heavy" or m.content == "ultra instinct") and m.author.id == ctx.author.id
                
                def player2_stlye(m):
                    return (m.content == "light" or m.content == "medium" or m.content == "heavy" or m.content == "ultra instinct") and m.author.id == opponent.id

                # calcs prop of attack style hitting
                def calc_damage(type, id):
                    if type == "light": # always hits
                        return 20
                    elif type == "medium" and random.random() <= .33: # 1 in 3
                        return 40
                    elif type == "heavy" and random.random() <= 0.125: # 1 in 8 
                        return 80
                    elif type == "ultra instinct" and str(id) in ADMIN:
                        return 9000
                    return 0
                
                if turn % 2 == 0: # player1 goes first
                    try:
                        style1 = await self.bot.wait_for('message', check=player1_stlye, timeout=10.0)
                        damage = calc_damage(style1.content, player1.user) # calc damage player2 takes based on player1's attack
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
                        style2 = await self.bot.wait_for('message', check=player2_stlye, timeout=10.0)
                        damage = calc_damage(style2.content, player2.user)
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
    ##  TRIVIA
    ##############################
    @commands.command(brief="Test your knowledge", description="Flex your IQ or negative IQ")
    async def trivia(self, ctx):
        url = "https://opentdb.com/api.php?amount=1"
        response = requests.get(url) 

        # making call to api and checking to see if it was successful
        if response.status_code == 200:
            data = response.json()
            results = data.get('results')[0] # save somes typing
            correct = results.get('correct_answer') # saves the correct answer

            # setup to ask user question
            question = discord.Embed(
                        title = f"{results.get('question')}",
                        colour = discord.Colour.blue()
                    )
            
            # we have multiple choice and true/false questions
            # we need to figure out which one was send as checking solutions methods are different
            if results.get('type') == 'multiple' : # multiple choice questions        
                options = results.get('incorrect_answers') + [correct] # setup for shuffle
                random.shuffle(options) # mix up choices

                # setup so that we can check answer later
                dic = {} 
                letters = ['a', 'b', 'c', 'd']
                str = ""
                for i in range(len(letters)):
                    dic.update({letters[i]: options[i]})
                    str += f'{letters[i].upper()}. {dic[letters[i]]} \n'

                question.description = str # displays the answer choices for user
            else: # true or false questions
                question.description = f'True or False'
            
            # asks the question with a ping at user
            await ctx.reply(embed=question) 

            # waiting for a response
            def is_correct(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
            try:
                response = await self.bot.wait_for('message', check=is_correct, timeout=10.0)
            except asyncio.TimeoutError:
                return await ctx.send('Times up, study harder text time!')
            
            # checks to see if response is right or wrong
            response = response.content.lower()
            if (response == "false" or response == "true") and response == correct.lower():        
                await ctx.send("Correct!")
            elif len(response) == 1 and response in letters and dic[response] == correct:
                await ctx.send("Well Done!")
            else:
                await ctx.send("Wrong, come back after studying some more.")
        else: # api error 
            await ctx.reply("Hmmm, still thinking of a question, please try again.")




##############################
##  ADD COG
##############################
async def setup(bot):
    await bot.add_cog(Games(bot))