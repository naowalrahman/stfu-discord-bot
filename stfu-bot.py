import discord
import random

client = discord.Client()

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
    if message.author == client.user:
        return 
    if message.content.lower() == ".stfu":
        await message.channel.send("stfu kid")
    if message.content.lower() in [".racistmeter", ".rm"]:
        await message.channel.send("you are {}% racist".format(random.choice(range(0, 100))))
    # if message.content.lower() == "~enablestfu" or message.content.lower == "~es":
    #     await message.channel.send("who do you want to enable stfu for?")
    #     try:
    #         user_ping = await client.wait_for("@", timeout=30)
    #     except: 
    #         message.channel.send("Too too long kid. Now stfu.")
    #     if user_ping == 

client.run("")