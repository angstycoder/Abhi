import discord
import asyncio
import json
import logging
from DiscordHandler import DiscordHandler
from discord.ext import commands
import os

startup_extensions = ["guild", "RNG" , "ExampleRepl", "Utils" ,"api"]
bot = commands.Bot(command_prefix='?a ', description="Nothing here")

#Get all the secret stuff
with open('token.json') as secret:
    token = json.load(secret)

@bot.event
async def on_ready():
    print("Logged in as Abhi")
    await bot.change_presence(game=discord.Game(name='?a help'))
    #bot.load_extension("api")
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

webhook_url = "gey webhook token here"
agent = "discord"

logger = logging.getLogger("discord")
logger.setLevel(logging.WARNING)

# Create formatter
FORMAT = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Create DiscordHandler and StreamHandler
discord_handler = DiscordHandler(webhook_url, agent)
stream_handler = logging.StreamHandler()

# Add log level to handlers
discord_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.INFO)

# Add format to handlers
discord_handler.setFormatter(FORMAT)
stream_handler.setFormatter(FORMAT)

# Add the handlers to the Logger
logger.addHandler(discord_handler)
logger.addHandler(stream_handler)



bot.run(os.environ['TOKEN']))
