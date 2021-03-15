# io.py
import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

# Load .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set bot prefix
bot = commands.Bot(command_prefix="|")

# Load in cogs:
bot.load_extension('cogs.basic')
bot.load_extension('cogs.modtools')
bot.load_extension('cogs.requestcalls')

# Global check, never run commands from bots
@bot.check
async def never_run_from_bots(ctx):
	return not ctx.author.bot

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected. At your service!')


bot.run(TOKEN)