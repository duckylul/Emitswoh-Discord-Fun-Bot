from discord.ext import commands
import discord
import string
import sys
import asyncio
import traceback








class dm(commands.Cog):
    """In progess"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @command.command(name="test")
    async def dm(self, ctx, member:discord.Member):
        await.ctx.send("What is the message?")
        def check(m):
            return m.author.id == ctx.author.id

        message = await client.wait_for('message', check=check)
        await ctx.send(f'sent message to {member}')

        await member.send(f'{ctx.author.mention} Has a message for you:\n{message.content}')


def setup(bot: commands.Bot):
    bot.add_cog(dm(bot))