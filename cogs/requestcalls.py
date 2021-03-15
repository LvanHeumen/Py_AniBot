import discord
import json
import requests

from discord.ext import commands
from discord.ext.commands import Cog


class Calls(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name = 'seiyuu',
		brief = 'Fetch a seiyuu\'s image',
		help = 'I can grab a voice actor\'s pictures for you. Currently I use the Jikan API to do this. The number to add can be found here: https:www.myanimelist.net/people/###',
		usage = '|seiyuu [number]'
		)
	async def seiyuu(self,ctx,numPerson: int):
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


	@commands.Cog.listener()
	async def on_reaction_add(self,reaction,user):
		if user.bot: return
		if reaction.emoji != "⬅" and reaction.emoji != "➡": return

		channel = reaction.message.channel

		print(f'{reaction.emoji} Added to message with ID {reaction.message.id}')

		if reaction.emoji == "➡":
			await channel.send('Forward innit?')
		elif reaction.emoji == "⬅":
			await channel.send('Backward innit?')




def setup(bot):
	bot.add_cog(Calls(bot))