import discord
import random
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command()
async def stfu(ctx):
    await ctx.send("stfu kid")


@bot.command(aliases=['rm'])
async def racistmeter(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author.name
    await ctx.send("{0} is {1}% racist".format(member.name, random.choice(range(0, 100))))


@bot.command(aliases=['cm'])
async def clownmeter(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author.name
    await ctx.send("{0} is {1}% clown".format(member.name, random.choice(range(0, 100))))


@bot.command(aliases=['wa'])
async def whoasked(ctx, *, arg=None):
    if arg == None:
        await ctx.send("who asked what dumbass")

    channel_id = ctx.message.channel.id
    channel = bot.get_channel(channel_id)

    messages = await ctx.channel.history(limit=15).flatten()
    sent_once = False

    whoasked_gifs = [r'./who-asked-gifs/whoasked1.gif', r'./who-asked-gifs/whoasked2.gif',
                     r'./who-asked-gifs/whoasked3.gif', r'./who-asked-gifs/whoasked4.gif', r'./who-asked-gifs/whoasked5.jpg']

    for msg in messages:
        if arg in msg.content and "?" in msg.content:
            embed = discord.Embed()
            embed.description = "Someone may have asked [here]({0}).".format(
                msg.jump_url)
            await ctx.send(embed=embed)
            sent_once = True
        elif messages[-1] == msg and sent_once == False:
            await ctx.send("No one asked kid. now stfu", file=discord.File(random.choice(whoasked_gifs)))


@bot.command()
async def naowalplease(ctx):
    author = str(ctx.message.author.name)
    if author == "bigBrain++;":
        await ctx.send("Naowal please")
    elif author == "Feitan":
        await ctx.send("Zaryab please")
    elif author == "Toast":
        await ctx.send("Jing Nang please") 
    elif author == "anaturalinstinctnoise":
        await ctx.send("Areeb please") 
    elif author == "Lilhomie": 
        await ctx.send("Faidh please")
    elif author == "inooby333":
        await ctx.send("Eric please") 
    elif author == "ChocoFudge":
        await ctx.send("Quazi please") 
    else:
        await ctx.send("{0} please".format(ctx.message.author.name))
        
keep_alive()
bot.run(os.environ.get("TOKEN"))