import discord
from discord.ext import commands
from random import randint

heroes = [
	"Genji",
	"McCree",
	"Pharah",
	"Reaper",
	"Soldier: 76",
	"Sombra",
	"Tracer",
	"Bastion",
	"Hanzo",
	"Junkrat",
	"Mei",
	"Torbjorn",
	"Widowmaker",
	"D.Va",
	"Reinhardt",
	"Roadhog",
	"Winston",
	"Zarya",
	"Ana",
	"Lucio",
	"Mercy",
	"Symmetra",
	"Zenyatta",
	"Orisa"
]

class Overwatcher:
	def __init__(self, bot):
		self.bot = bot
		
	def buildStringForHeroPlayer(self, hero, player):
		return "{0}, play **{1}**!".format(player.mention, hero)
		
	def getHeroForPlayer(self, player):
		return self.buildStringForHeroPlayer(self.getRandomHero(), player)
		
	def getRandomHero(self):
		rand = randint(0, len(heroes) - 1)
		return heroes[rand]
		
	@commands.command(pass_context=True)
	async def buildmeanarmy(self, ctx, unique=None):
		channel = ctx.message.server.get_channel("134727416038817793")
		army = []
		string = ""
		
		self.bot.say(unique);
		
		for member in channel.voice_members:
			if unique:
				hero = self.getRandomHero()
				while hero in army:
					hero = self.getRandomHero()
					if len(army) >= len(heroes):
						break

				army.append(hero)
				string = self.buildStringForHeroPlayer(hero, member)
			else:
				string = self.getHeroForPlayer(member)
			await self.bot.say(self.getHeroForPlayer(member))

	@commands.command(pass_context=True)
	async def hitme(self, ctx):
		author = ctx.message.author

		#Your code will go here
		await self.bot.say(self.getHeroForPlayer(author))

def setup(bot):
	bot.add_cog(Overwatcher(bot))