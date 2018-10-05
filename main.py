import discord
from discord.ext import commands
from data.Renge import renge_images
from data.traps import trap_images
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
    foo = ["🏓 Pong! I win!", "🏓 Pong! I win!", "🏓 Pong! I win!", "🏓 Pong! I win!", "🏓 ono you won"]
    moo = (random.choice(foo))
    await bot.say(moo)
    
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
    
bot.run(token)
