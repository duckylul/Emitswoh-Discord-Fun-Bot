from discord.ext import commands  # Again, we need this imported
import discord
import traceback
from discord import Member


class set_status(commands.Cog):
	"""Command to set bot's status"""
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name="setstatus")
   
	@commands.cooldown(rate=1, per=5)
	async def setstatus(self, ctx: commands.Context, *, text: str):
		"""Set the bot's status."""
		await self.bot.change_presence(activity=discord.Game(name=text))
        
        

		print(error)

	@setstatus.error
	async def setstatus_error(self, ctx: commands.Context,
	                          error: commands.CommandError):
		"""Handle errors for the example command."""

		if isinstance(error, commands.CommandOnCooldown):
			message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
		elif isinstance(error, commands.MissingPermissions):
			message = "You are missing the required permissions to run this command!"
		elif isinstance(error, commands.MissingRequiredArgument):
			message = f"Missing a required argument: {error.param}"
		elif isinstance(error, commands.ConversionError):
			message = str(error)
		else:
			return

		await ctx.send(message, delete_after=5)
		await ctx.message.delete(delay=5)


def setup(bot: commands.Bot):
	bot.add_cog(set_status(bot))
