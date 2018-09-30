import discord
from discord.ext import commands
import asyncio
import time
import os

client = commands.Bot(command_prefix = "!")
token = os.environ["token"]

@client.event
async def on_ready():
    print("bot is ready")
@client.event
async def on_message(message):
    if message.content == "cookie":
        await Bot.send_message(message.channel, ":cookie:")
client.run (token)
