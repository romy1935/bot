import discord
from discord.ext import commands
import asyncio
import time
import os

bot = commands.Bot(command_prefix="!")
token = os.environ["token"]


@bot.event
async def on_ready():
    print("bot is ready")


@bot.event
async def on_message(message):
    if message.content == "kms":
        await bot.send_message(message.channel, "pls do")
    args = message.content.split()
    if "gimme" in args and "cookie" in args:
        await bot.add_reaction(message, "🍪")
    args = message.content.split()
    if "was" in args and "given" in args:
        await bot.add_reaction(message, "💖")
    args = message.content.split()
    if "trap" in args:
        await bot.add_reaction(message, "<:blobaww:357967083960795137>")


bot.run(token)
