from discord.ext import commands # Again, we need this imported
import discord
import traceback
import time
from datetime import datetime


class help(commands.Cog):
    """Help commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    

    @commands.command(name="info_help") 
    async def general_help(self, ctx: commands.Context):
        info_embed = discord.Embed(title="Emitswoh's Fun Help", description="**Fun** and **Funny** features this noob bot can do!!", colour=0x87CEEB, timestamp=datetime.utcnow()) 

        await ctx.send(info_embed=info_embed)
    
    
    

def setup(bot: commands.Bot):
    bot.add_cog(help(bot))

