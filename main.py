import discord
from discord.ext import commands
import asyncio
import time
import os

bot = commands.Bot(command_prefix="!")
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

@bot.command()
async def git():
    await bot.say("**The github repository of the bot:**\nhttps://www.github.com/Romy1935/bot")
    
bot.run(token)
