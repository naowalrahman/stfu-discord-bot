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


@bot.command(aliases=['hp'],
             help="displays a help image with detailed syntax description")
async def h(ctx, arg=None):
    if arg == None:
        await ctx.send(file=discord.File(r'./help-img.png'))


@bot.command(help="just says stfu")
async def stfu(ctx):
    await ctx.send("stfu kid")


@bot.command(aliases=['rm'], help="tells you what percent racist you are")
async def racistmeter(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    if str(member.name) == "Feitan":
        await ctx.send("{0} is {1}% racist".format(member, 100))
    else:
        await ctx.send("{0} is {1}% racist".format(
            member, random.choice(range(0, 100))))


@bot.command(aliases=['cm'], help="tells you what percent clown you are")
async def clownmeter(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author.name
    await ctx.send("{0} is {1}% clown".format(member,
                                              random.choice(range(0, 100))))


@bot.command(aliases=['bbm'], help="tells you what percent beanbag you are")
async def beanbagmeter(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author.name
    await ctx.send("{0} is {1}% beanbag".format(member,
                                                random.choice(range(0, 100))))


@bot.command(aliases=['wa'],
             help="sees if anyone actually asked (takes a string as parameter)"
             )
async def whoasked(ctx, *, arg=None):
    if arg == None:
        await ctx.send("who asked what dumbass")

    channel_id = ctx.message.channel.id
    channel = bot.get_channel(channel_id)
    channel = bot.get_channel(channel_id)
    sent_once = False

    messages = await ctx.channel.history(limit=15).flatten()
    del messages[0]

    whoasked_gifs = [
        r'./who-asked-gifs/whoasked1.gif', r'./who-asked-gifs/whoasked2.gif',
        r'./who-asked-gifs/whoasked3.gif', r'./who-asked-gifs/whoasked4.gif',
        r'./who-asked-gifs/whoasked5.jpg'
    ]

    for msg in messages:
        if arg in msg.content:
            sent_once = True
            embed = discord.Embed()
            embed.description = "Someone may have asked [here]({0}).".format(
                msg.jump_url)
            await ctx.send(embed=embed)

    if sent_once == False:
        await ctx.send("No one asked kid. now stfu",
                       file=discord.File(random.choice(whoasked_gifs)))
        sent_once = True
    sent_once = False


@bot.command(help="says user please, with the user being the arg given")
async def naowalplease(ctx):
    author = str(ctx.message.author.name)
    if author == "bigBrain++;":
        await ctx.send("Naowal please")
    elif author == "Feitan":
        await ctx.send("Zaryab Khan please")
    elif author == "Toast":
        await ctx.send("Jing Nang Liu please")
    elif author == "anaturalinstinctnoise":
        await ctx.send("Areeb please")
    elif author == "Lilhomie":
        await ctx.send("Faidh please")
    elif author == "inooby333":
        await ctx.send("Eric Liu please")
    elif author == "ChocoFudge":
        await ctx.send("Quazi please")
    else:
        await ctx.send("{0} please".format(ctx.message.author.name))


@bot.command(help="annoy jing with ketchup on chicken nuggets")
async def annoyjing(ctx):
    await ctx.send("ketchup ketchup ketchup")
    await ctx.send(file=discord.File(r'./annoyjing.mp4'))


keep_alive()
bot.run(os.environ.get("TOKEN"))
