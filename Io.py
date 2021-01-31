# io.py
import os
import random
import re

from discord.ext import commands
from dotenv import load_dotenv

# Load .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set bot prefix
bot = commands.Bot(command_prefix="|")

# Global check, never run commands from bots
@bot.check
async def never_run_from_bots(ctx):
	return not ctx.author.bot

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected. At your service!')

@bot.command(
	name = 'ping',
	brief = 'Ping me to check if I\'m awake!'
	)
async def ping(ctx):
	await ctx.send("You rang?")

@bot.command(
	name = 'roll',
	brief = 'Have me roll dice.',
	help = 'I can roll dice for you. Currently I accept up to 10 default dice or coins.',
	usage = '[1-10]d[2,4,6,8,10,12,20,100]'
	)
async def roll(ctx, arg):
	dice = arg.split("d")
	num_of_dice = int(dice[0])
	num_of_sides = int(dice[1])
	accepted_dice_set = [2,4,6,8,10,12,20,100]

	if num_of_sides not in accepted_dice_set:
		await ctx.send('Sorry, I do not know that type of die. Please try one of the base dice.')
		return
	if num_of_dice > 10:
		await ctx.send('Sorry, I currently only support up to 10 dice.')
		return

	await ctx.send(f'Rolling *{arg}*...')

	diceRolls = [
	random.choice(range(1,num_of_sides+1))
	for _ in range(num_of_dice)
	]

	await ctx.send(f'You have rolled **{sum(diceRolls)}**')

@bot.command(
	name = 'logout',
	brief = 'Logs me out and closes my connection to discord.'
	)
@commands.has_role('Owner')
async def logout(ctx):
	await ctx.bot.logout()
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		await ctx.send('Sorry, you do not have enough permissions to tame me')



bot.run(TOKEN)