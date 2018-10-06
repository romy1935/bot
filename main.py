import discord
from discord.ext import commands
from data.Renge import renge_images
import random
import asyncio
import time
import os

bot = commands.Bot(command_prefix="<")
token = os.environ["token"]
bot.remove_command("help")

@bot.event
async def on_ready():
    print("bot is ready")

@bot.event
async def on_message(message):
    args = message.content.split()
    if "gimme" in args and "cookie" in args:
        await bot.add_reaction(message, "🍪")
    args = message.content.split()
    if "was" in args and "given" in args:
        await bot.add_reaction(message, "💖")
    await bot.process_commands(message)

@bot.command()
async def git():
    await bot.say("**My Github:**\nhttps://www.github.com/Romy1935/bot")
    
@bot.command()
async def ping():
    await bot.say("🏓 Pong!")
    
@bot.command()
async def pingpong():
    me = 0
    you = 0
    hoo = ["🏓 Pong! I win!", "🏓 Pong! I win!", "🏓 ono you won"]
    coo = (random.choice(hoo))
    while me < 3:   
        await bot.say("🏓 Ping!")
        await bot.say("🏓 Pong!")
        await bot.say("🏓 Ping!")
        await bot.say("🏓 Pong!")
        await bot.say(coo)
        if coo == "🏓 Pong! I win!":
            me += 1
        else:
            you += 1
        await bot.say(me : you)
    
    
@bot.command()
async def renchon():
    output = random.sample(renge_images, 1)
    em = discord.Embed(title="Nyanpasu~", colour=0xFBC1F0)
    em.set_image(url=output[0])
    await bot.say(embed=em)


@bot.command()
async def renchonbomb():
    i = 1
    while i < 6:
        output = random.sample(renge_images, 1)
        em = discord.Embed(title="Nyanpasu~", colour=0xFBC1F0)
        em.set_image(url=output[0])
        await bot.say(embed=em)
        i += 1

@bot.command()
async def help():
    em = discord.Embed(title="My commands:", colour=0xFBC1F0)
    em.add_field(name="**git**", value="shows my github", inline=False)
    em.add_field(name="**ping**", value="you can play ping pong with me!", inline=False)
    em.add_field(name="**renchon**", value="shows a pick of renge!", inline=False)
    em.add_field(name="**renchonbomb**", value="shows lots of pics of renge!", inline=False)
    await bot.say(embed=em)
    
bot.run(token)
