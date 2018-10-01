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
        await message.channel.send("pls do")
    elif "cookie" in message.content():
        await message.channel.send(":cookie:")
    elif ":cookie:" in message.content():
        await message.channel.send(":cookie:")
    elif ":blobnomcookie:" in message.content():
        await message.channel.send(":cookie:")
    args = message.content.split()
    if "gimme" in args and "cookie" in args:
        await message.add_reaction("🍪")


bot.run(token)
