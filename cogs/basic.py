import discord
import random

from discord.ext import commands
from discord.ext.commands import Cog



class Basic(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.command(name = 'ping',
		brief = 'Ping me to check if I\'m awake!'
		)
	async def ping(self, ctx):
		await ctx.send("Yes hello, I am awake!")

	@commands.command(
	name = 'roll',
	brief = 'Have me roll dice.',
	help = 'I can roll dice for you. Currently I accept up to 10 default dice or coins.',
	usage = '[1-10]d[2,4,6,8,10,12,20,100]'
	)
	async def roll(self, ctx, arg):
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

def setup(bot):
	bot.add_cog(Basic(bot))