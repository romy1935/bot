import discord
from discord.ext import commands
from data.Renge import renge_images
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
    if message.content == "kms":
        await bot.send_message(message.channel, "ono")
    args = message.content.split()
    if "gimme" in args and "cookie" in args:
        await bot.add_reaction(message, "🍪")
    args = message.content.split()
    if "was" in args and "given" in args:
        await bot.add_reaction(message, "💖")
    args = message.content.split()
    if "trap" in args:
        await bot.add_reaction(message, "🍆")
    await bot.process_commands(message)

@bot.command()
async def git():
    await bot.say("**My Github:**\nhttps://www.github.com/Romy1935/bot")
    
@bot.command()
async def git():
    await bot.say("**My Github:**\nhttps://www.github.com/Romy1935/bot")
@bot.command()
async def say(message):
    output = random.sample(sloth_images, 1)
    em = discord.Embed(title="Nyanapsu~", colour=0xFBC1F0)
    em.set_image(url=output)
    await bot.say(embed=em)
    
bot.run(token)
