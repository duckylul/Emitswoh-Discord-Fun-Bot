from discord.ext import commands # Again, we need this imported
import discord
import traceback
import time
from datetime import datetime


class help(commands.Cog):
    """Help commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ghelp") 
    async def general_help(self, ctx: commands.Context):
        embed = discord.Embed(title="List of helps", description="Below are some help commands for different section.", colour=0x87CEEB, timestamp=datetime.utcnow())
        embed.set_author(name="Ducky", icon_url="https://cdn.discordapp.com/emojis/720361366900310047.png?size=128")
        embed.add_field(name="!g_help", value="A help that cotains general commands that bots have!", inline=False)
        embed.add_field(name="!fhelp", value="Help for some fun commands this funny noob bot can do!", inline=True)
        embed.add_field(name="!bhelp", value="This command is for only the bot controlers. Don't even try to use this command", inline=True)
        embed.set_footer(text="Wow! A footer!", icon_url="https://cdn.discordapp.com/emojis/746899128952291428.png?size=128")
        embed.add_field(name="!info_help", value="This command helps you with the info of the bot @emitswoh . You will learn all about it and the passive features that it contains!", inline=True)    


        await ctx.send(embed=embed)
    

    @commands.command(name="info_help") 
    async def general_help(self, ctx: commands.Context):
        embed = discord.Embed(title="Emitswoh's Fun Help", description="**Fun** and **Funny** features this noob bot can do!!", colour=0x87CEEB, timestamp=datetime.utcnow()) 

        await ctx.send(embed=embed)
    
    
    

def setup(bot: commands.Bot):
    bot.add_cog(help(bot))

