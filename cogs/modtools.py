import discord

from discord.ext import commands
from discord.ext.commands import Cog

class ModTools(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name = 'logout',
		brief = 'Logs me out and closes my connection to discord.'
		)
	@commands.is_owner()
	async def logout(self,ctx):
		await self.bot.close()
	async def cog_command_error(self,ctx,error):
		if isinstance(error, commands.errors.CheckFailure):
			await ctx.send('Sorry, you have no power over me.')


def setup(bot):
	bot.add_cog(ModTools(bot))