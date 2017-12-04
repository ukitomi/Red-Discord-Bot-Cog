import discord
import asyncio
from discord.ext import commands
from random import randint
from random import choice


try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False
import aiohttp

class Mycog:
	"""https://twentysix26.github.io/Red-Docs/red_guide_command_args/ for custom commands argument"""

	def __init__(self, bot):
		# self.accounts = dataIO.load_json(file_path)
		self.bot = bot
		self.eggbreakfast = ["Toast with Green Garlic Confit and Poached <@171752453409210368>!", "Garlic Soup with Potatoes and Poached <@171752453409210368>!", 
							"Perfect Poached <@171752453409210368>!", "Cheesy Grits with Poached <@171752453409210368>, Greens, and <@125758147729031168>!", 
							"Smoked Fish and Rice Breakfast Bowl with <@171752453409210368>!", "Breakfast Bowl with Sweet Potatoes and Turmeric <@171752453409210368>!",
							"Toast with Ramp Kimchi and Poached <@171752453409210368>!", "Tofu Yum-Yum Rice Bowl with <@171752453409210368>!", 
							"Chickpeas and Chard with Poached <@171752453409210368>!", "Frisee-Lardon Salad with <@171752453409210368>",
							"Crazy-Fast Ramen with <@125758147729031168>, <@171752453409210368>, and Kimchi!", "Sorrel Rice Bowls with Poached <@171752453409210368>!"]
		self.punishment = ["take a selfie with pig/bunny filter", "facetime the others until not mad"]

	@commands.command()
	async def dotanow(self):
		""" How many players are online atm? """
		url = "https://steamdb.info/app/570/graphs/" #build the web adress
		async with aiohttp.get(url) as response:
			soupObject = BeautifulSoup(await response.text(), "html.parser")
		try:
			online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
			await self.bot.say(online + ' players are playing this game at the moment')
		except:
			await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")


	@commands.command()
	async def punch(self, user : discord.Member):
		""" Choose to punch someone """
		await self.bot.say("ONE PUNCH! AND " + user.mention + " is out! ლ(ಠ益ಠლ)")

	@commands.command()
	async def hammy(self):
		""" Instead of flipping a coin to decide ... We kill the hammy to decide! """
		n = randint(1, 2)
		if n == 1:
			await self.bot.say("Is it time to kill <@113170457326342144> :hee:")
		else:
			await self.bot.say("Is it time to kill <@146828602787364864> :hee:")

	@commands.command(pass_context=True)
	async def egg(self, ctx, text : str):
		""" What should I eat for breakfast? try the text to be: breakfast, lunch, or dinner!"""
		await self.bot.say("Your choice of " + text + " for today would be ....")
		if text == "breakfast":
			await self.bot.say(choice(self.eggbreakfast))
		elif text == "lunch":
			await self.bot.say("Uki is too lazy to implement this.")
		elif text == "dinner":
			await self.bot.say("Uki is too lazy to implement this.")
		else:
			await self.bot.say("oh... nothing for you right now :(")

	@commands.command(pass_context=True)
	async def mocking(self, ctx, *, text):
		""" randomly cap/lowercase the letters in the string """
		split = text.split(" ")
		string = ""
		for idx in split:
			for i in idx:
				n = randint(0, 1)
				if n == 0:
					string += i.upper()
				elif n == 1:
					string += i.lower()
			string += " "
		await self.bot.say(string)
		image = "/Users/ukiitomi/Desktop/mocking.png"
		channel = ctx.message.channel
		await self.bot.send_file(channel, image)

	@commands.command()
	async def botoftruth(self):
		"""This is def not bot of lies. For Queen and Uki use only"""
		n = randint(0, 1)
		if n == 0:
			await self.bot.say("The Bot of Truth: <@155767675379777536> loves <@162819465380102144> more !!!")
		else:
			await self.bot.say("The Bot of Truth: <@162819465380102144> loves <@155767675379777536> more !!!")

	@commands.command(pass_context=True)
	async def spam(self, ctx, user : discord.Member, time):
		""" when you hate someone in the channel.. spam to death! """
		for i in (0, time):
			dele = await self.bot.say("testing")
			await asyncio.sleep(3)
			await self.bot.delete_message(dele)
			await asyncio.sleep(3)
		await self.bot.say("Out of for loop")

	@commands.command()
	async def punish(self, user : discord.Member):
		""" Choose to punch someone """
		await self.bot.say("Bad " + user.mention + " will " + choice(self.punishment))

	@commands.command()
	async def eat(self, user : discord.Member):
		""" choose to eat someone """
		await self.bot.say("（￣ｗ￣）Ψ " + user.mention )

	@commands.command(pass_context=True)
	async def guessnumber(self, ctx):
		""" Guess a number between the input range """
		await self.bot.say("Guess the number between 0 to 10! ")
		msg = await self.bot.wait_for_message(timeout=5.0, author = ctx.message.author)
		answer = randint(1, 10)
		try:
			if msg is None:
				fmt = "Sorry you took too long. It was {}."
				await self.bot.say(fmt.format(answer))
			elif int(msg.content) == answer:
				await self.bot.say("(ノ*゜▽゜*).  You got it! You get 500 credits! ~ヾ(＾∇＾)  ")
				bank = self.bot.get_cog("Economy").bank
				bank.deposit_credits(ctx.message.author, 500)
			else:
				await self.bot.say("(｡•́︿•̀｡) You didn't get it.. it is actually {}.".format(answer))
		except ValueError:
			await self.bot.say("Oops! Error! Maybe try again? Type " + "```" + "*guessnumber" + "```" + "Make sure you type an integer!")

	@commands.command(pass_context=True)
	async def psts(self, ctx):
		"""Gambling psts"""
		try:
			n = randint(1, 3)
			author = ctx.message.author
			bank = self.bot.get_cog("Economy").bank
			field_name = "Results: "
			if n == 1 :
				field_contents = ("°˖✧◝(⁰▿⁰)◜✧˖° You successfully make a psts!! Get 50 credits! ≧(´▽｀)≦")
				bank.deposit_credits(ctx.message.author, 50)
				color = 0x008000
			else:
				field_contents = ("(.﹒︣︿﹒︣.) You failed to make a psts.. 100 credits have been take away! ")
				bank.withdraw_credits(ctx.message.author, 100)
				color = 0xFF0000
			embed = discord.Embed(colour=color)  # Can use discord.Colour()
			embed.title = "Premium Silverfrost Transformation Stone"
			embed.set_author(name=str(author.name), icon_url=author.avatar_url)
			embed.add_field(name=field_name, value=field_contents)
			await self.bot.say(embed=embed)
		except:
			await self.bot.say("Make sure you have a bank register!! Do ``*bank register`` if you dont!")
			await self.bot.say("If the bot continues to occur error, it might because you dont have enough credit balance! Do ``*payday`` to get your credit!")

	@commands.command(pass_context=True)
	async def give(self, ctx, rolename : str):
		""" give role """
		try:
			role = discord.utils.get(ctx.message.server.roles, name = "test")
			author = ctx.message.author
			description = ""
			if role in author.roles:
				description = ("YOU ALREADY HAVE THE ROLE.")
				color = 0xFF0000
			elif rolename == "role":
				await self.bot.add_roles(author, role)
				description = ("Congrats " + author.mention + ". You obtained the ``" + role.name + "`` role!")
				color = 0x008000
			else:
				description = ("No result.. check to see if you have made a typo?")	
				color = 0xFF0000
			embed = discord.Embed(colour = color, description = description)
			await self.bot.say(embed=embed)
		except:
			await self.bot.say("Exception catched.")
def setup(bot):
	if soupAvailable:
		bot.add_cog(Mycog(bot))
	else:
		raise RuntimeError("You need to run 'pip3 install beautifulsoup4'")