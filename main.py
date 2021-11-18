
#emitswoh
from discord.ext import commands, tasks
import discord
import string
import sys
import asyncio
import random
import os


random_messages = ['Why you bully me?', 'Talk RIGHT NOW', 'Who likes Donald Trump here??', "How many chickens would it take to kill an elephant?", "mrbeast", "DM @ilikeducks", "i AM COOL"]

@tasks.loop(minutes=4.6)
async def test(channel):
    n_random_messages = random.choice(random_messages)
    await channel.send(n_random_messages)



bot = commands.Bot(command_prefix="!")


noob_emo = '<:noob:908513174972674068>'

@bot.event
async def on_ready():
    print(f"{bot.user} is ready! Go emitswohs!!")
    channel = bot.get_channel(905612759998296169)
    test.start(channel=channel)

bot.load_extension("setstatus")

bot.load_extension("ping")

bot.load_extension("snipe")

bot.load_extension("general_help")

bot.load_extension("info_help")




#scripts

noob_script = ["Am I noob?", "Am I pogs?", "me is emo?", noob_emo+'Am I cutes?', "Can you give me 1 million dollars??"]

answer_yes = ["pog", "yay", "_noob_", ":smiley:", "you nice nice nice"]

answer_no = ["I am _noob_", "e", ":rage:","*yu mean*"]

answer_hello = ["hi", "hello", "e", ":wave:", ":)"]


@bot.command()
async def noobquestion(ctx):
    r_noob_script = random.choice(noob_script)
    await ctx.channel.send(r_noob_script)

    try:
        message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

    except asyncio.TimeoutError:
        await ctx.channel.send("Ouch you igorned me.")

    else:
        r_noob_yes = random.choice(answer_yes)

        r_noob_no = random.choice(answer_no)
        if message.content.lower() == "yes":
            await ctx.channel.send(r_noob_yes)

        elif message.content.lower() == "no":
            await ctx.channel.send(r_noob_no)

        





@bot.command()
async def profile_info(ctx, member:discord.Member):
            embed = discord.Embed()
             

            embed.set_image(url=member.avatar_url)

            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

        
@bot.event
async def on_message(message:discord.Message):
    await bot.process_commands(message)
    if message.content.startswith("hello"):
        random_message = random.randint(1,100)
        if random_message <= 50:
           r_noob_hello = random.choice(answer_hello)
           await message.channel.send(r_noob_hello)
        else:
            return       










my_secret = os.environ['TOKEN']

bot.run(my_secret)