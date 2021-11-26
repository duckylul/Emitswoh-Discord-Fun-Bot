from discord.ext import commands 
import discord
import traceback
from discord import Member


class set_stream(commands.Cog):
	"""Command to set bot's status"""
	def __init__(self, bot: commands.Bot):
		self.bot = bot
    
    
    @commands.command(name="setstream")	
	async def setstatus(self, ctx: commands.Context, *, text: str):
		"""Set the bot's Ilikeducks2405 stream status!"""
        #You can change it to your stream!
	    await client.change_presence(activity=discord.Streaming(name='Surviv.io 🔴LIVE🔴', url='https://www.twitch.tv/ilikeducks2405'))

    



def set_stream(bot: commands.Bot):
	bot.add_cog(set_stream(bot))
