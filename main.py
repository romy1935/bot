import discord
from discord.ext import commands
import asyncio
import time
import os

bot = commands.Bot(command_prefix = "!")
token = os.environ["token"]

@bot.event
async def on_ready():
    print("bot is ready")

@bot.event
async def on_message(message):
    if message.content == "kms":
        await message.channel.send("pls do")
    elif "cookie" in message.content.split():
        await message.channel.send(":cookie:")

bot.run(token)
