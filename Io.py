# io.py
import discord
import json
import os
import random
import re
import requests

from bs4 import BeautifulSoup
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

# Global check, never run commands from bots
@bot.check
async def never_run_from_bots(ctx):
	return not ctx.author.bot

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected. At your service!')

@bot.event
async def on_reaction_add(reaction,user):
	if user.bot: return
	if reaction.emoji != "⬅" and reaction.emoji != "➡": return
	
	channel = reaction.message.channel

	print(f'{reaction.emoji} Added to message with ID {reaction.message.id}')

	if reaction.emoji == "➡":
		await channel.send('Forward innit?')
	elif reaction.emoji == "⬅":
		await channel.send('Backward innit?')

@bot.command(
	name = 'seiyuu',
	brief = 'Fetch a seiyuu\'s image',
	help = 'I can grab a voice actor\'s pictures for you. Currently I use the Jikan API to do this. The number to add can be found here: https:www.myanimelist.net/people/###',
	usage = '|seiyuu [number]')
async def seiyuu(ctx, numPerson: int):
	r = requests.get(f'https://api.jikan.moe/v3/person/{numPerson}/pictures')

	msgArray = []
	imgArray = r.json()['pictures']

	for x in range(len(imgArray)):
		imgURL = imgArray[x]['large']
		embedVar = discord.Embed()
		embedVar.set_image(url = imgURL)
		embedVar.set_footer(text = f'{x+1}/{len(imgArray)}')
		msgArray.append(embedVar)

	msg = await ctx.send(embed=msgArray[0])
	await msg.add_reaction("⬅")
	await msg.add_reaction("➡")


bot.run(TOKEN)