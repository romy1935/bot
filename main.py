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
    if message.content == "cookie":
        await message.channel.send(":cookie:")
    elif "cookie" in message.content.split():
        await message.channel.send(":cookie:")
    args = message.content.split()
    if "gimme" in args and "cookie" in args:
        await message.add_reaction(":cookie:")
        
bot.run(token)
