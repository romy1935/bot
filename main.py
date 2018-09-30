import discord
from discord.ext import commands
import asyncio
import time
import os

bot = commands.bot(command_prefix = "!")
token = os.environ["token"]

@bot.event
async def on_ready():
    print("bot is ready")
@bot.event
async def on_message(message):
    if message.content == "cookie":
        await bot.send_message(message.channel, ":cookie:")

@bot.event
async def on_message(message):
    if "cookie" in message.content.split():
        await message.add_reaction("🍪")

bot.run (token)
