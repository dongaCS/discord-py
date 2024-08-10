from discord.ext import commands
import os
import discord

class Clip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot # client


    ##############################
    ##  DELETE LISTENER
    ##############################
    # @commands.Cog.listener() # MUST BE ON
    async def on_message_delete(self, ctx):
        if ctx.author.bot: # makes sure its not a bot
            return

        type = "DELETE"

        # get logger channels
        channel_js = self.bot.get_channel(int(os.getenv("LOGGER_JS")))
        channel_embed = self.bot.get_channel(int(os.getenv("LOGGER_EMBED")))

        # json in case we want to parse data in future
        json = f'{{ "type": "{type}", "channel name": "{ctx.channel}", "channel id": "{ctx.channel.id}", "author": "{ctx.author.id}", "message id": "{ctx.id}", "message": "{ctx.content}", "time": "{ctx.created_at}"}}'

        # init for discord embed
        info = discord.Embed(
                        title = f'<@{ctx.author.id}> aka {ctx.author} ',
                        description = f'message: {ctx.id} created at {ctx.created_at}',
                        colour = discord.Colour.gold()
                    )
        
        # sets glasses image, deleted message, and channel detail
        info.set_thumbnail(url='https://runescape.wiki/images/thumb/Sunglasses_%28…png/200px-Sunglasses_%28clear%29_detail.png?708a7')
        info.add_field(name='context', value=f'{ctx.content}', inline=False)
        info.add_field(name=f'Channel: {ctx.channel}', value=f'{ctx.channel.id}', inline=False)

        # sends message to logger channels
        await channel_js.send(json)
        await channel_embed.send(embed=info)


    ##############################
    ##  EDIT LISTENER
    ##############################
    # @commands.Cog.listener() # MUST BE ON
    async def on_message_edit(self, before, after):
        if before.author.bot: # makes sure its not a bot
            return

        type = "EDIT"

        # get logger channels
        channel_js = self.bot.get_channel(int(os.getenv("LOGGER_JS")))
        channel_embed = self.bot.get_channel(int(os.getenv("LOGGER_EMBED")))

        # json in case we want to parse data in future
        json = f'{{ "type": "{type}", "channel name": "{before.channel}", "channel id": "{before.channel.id}", "author": "{before.author.id}", "message id": "{before.id}", "message": "{before.content}", "time": "{before.created_at}"}}'

        # init for discord embed
        info = discord.Embed(
                        title = f'<@{before.author.id}> aka {before.author} ',
                        description = f'message: {before.id} created at {before.created_at}',
                        colour = discord.Colour.purple()
                    )
        
        # sets glasses image, before and after edit message, and channel detail
        info.set_thumbnail(url='https://runescape.wiki/images/thumb/Sunglasses_%28…png/200px-Sunglasses_%28clear%29_detail.png?708a7')
        info.add_field(name='Before', value=f'{before.content}', inline=False)
        info.add_field(name='After', value=f'{after.content}', inline=False)
        info.add_field(name=f'Channel: {before.channel}', value=f'{before.channel.id}', inline=False)

        # sends message to logger channels
        await channel_js.send(json)
        await channel_embed.send(embed=info)


##############################
##  ADD COG
##############################
async def setup(bot):
    await bot.add_cog(Clip(bot))

