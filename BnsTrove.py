import discord
import asyncio
from discord.ext import commands
from random import randint
from random import choice
from itertools import islice
from enum import Enum


class Trove:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def trove(self, ctx):
		"""Run out of keys? Trove on me!"""
		# await self.bot.say(MSG)
		n = randint(0, 100)
		author = ctx.message.author
		description = "Why daily when you can trove?"
		field_name = "Results:"
		color = 0x000000
		ITEMS = []
		if n < 10:
			generator = randint(0, 9)
			counter = generator * 8
			with open('/Users/ukiitomi/Documents/BOT/Red-DiscordBot/data/trove/crit.txt', 'r') as f:
				for line in islice(f, counter, counter + 8):
					ITEMS.append(line)
			field_contents = '\n'.join(ITEMS)
			color = 0x008000
		else:
			generator = randint(0, 23)
			counter = generator * 8
			with open('/Users/ukiitomi/Documents/BOT/Red-DiscordBot/data/trove/noncrit.txt', 'r') as f:
				for line in islice(f, counter, counter + 8):
					ITEMS.append(line)
			field_contents = '\n'.join(ITEMS)
			color = 0xFF0000
		footer_text = "Feel free to spam Uki for trove results."

		embed = discord.Embed(colour=color, description=description)  # Can use discord.Colour()
		embed.title = "Happy Troving <3"
		embed.set_author(name=str(author.name), icon_url=author.avatar_url)
		embed.add_field(name=field_name, value=field_contents)
		embed.set_footer(text=footer_text)

		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(Trove(bot))