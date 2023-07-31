import discord
import datetime
import random
import asyncio
from discord.ext import commands
from database import data
from cogs import util


class Registry(commands.Cog, name='Member Registry'):

	def __init__(self, client):
		self.client = client
		print('registry online!')


	## Sends user join message ##
	@commands.Cog.listener()
	async def on_member_join(self, member):
		embed = discord.Embed(description=f"📥 {member.mention} joined the server!", color=58880, timestamp=datetime.datetime.utcnow())
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text="Joined on")
		embed.add_field(name="Member Count", value=member.guild.member_count, inline=False)
		await self.client.get_channel(879009713281462329).send(embed=embed)
		print(f"{member} has joined the server.")
		data.write('join', str(member.id), int(datetime.datetime.utcnow().timestamp()))
		
		await asyncio.sleep(60)

		## Send user welcome message ##
		mentions = []
		async for message in self.client.get_channel(879009714069962843).history(after=datetime.datetime.utcnow().__sub__(datetime.timedelta(seconds=60))):
			mentions.append(message.author)
			mentions.extend(message.mentions)
		if self.client.get_guild(879009710701957130).get_member(member.id) is None:
			mentions.append(member)
		if member not in mentions:
			first = [f'<@!{member.id}>, welcome to Guild Wars 2 University!', 
				f'Welcome <@!{member.id}> to Guild Wars 2 University!', 
				f'Welcome <@!{member.id}>!', 
				f'Welcome to Guild Wars 2 University, <@!{member.id}>!']
			last = ['Feel free to introduce yourself.', 
				'Feel free to introduce yourself here if you want.', 
				'Please introduce yourself here.', 
				'Please introduce yourself here if you want.', 
				'What is your favorite class in the game?', 
				'How long have you been playing Guild Wars 2?', 
				'Are you excited for the new expansion, End of Dragons?', 
				'Do you have a favorite gamemode or playstyle?', 
				'It is recommend to change your discord nickname to your Gw2 account name, so that people can identify you in-game.']
			await self.client.get_channel(879009714069962843).send(f'{random.choice(first)} {random.choice(last)}')
			id = data.read('id', 'welcome')
			message = await self.client.get_channel(879009714069962843).fetch_message(id)
			await message.delete()
			message = await self.client.get_channel(879009714069962843).send("New to Guild Wars 2? Check out our <#797318280826191922>. New to Discord? Check out our <#875232316010668082>.\nIf you still have questions about the Guid Wars 2 or Discord, you can ask in <#736254186353721454>.\nWe have events scheduled in our <#852189307031781426>. Be sure to you have the correct <#735989626455457894> to attend them.")
			data.write('id', 'welcome', message.id)
	
	## Sends user leave message ##
	@commands.Cog.listener()
	async def on_member_remove(self, member):
		join = datetime.datetime.utcfromtimestamp(data.read('join', str(member.id)))
		duration = datetime.datetime.utcnow().__sub__(join).total_seconds()
		time = util.HumanizeDuration(duration)
		embed = discord.Embed(description=f"📤 {member.mention} left the server!", color=15073281)
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=f"Member for {time}")
		embed.add_field(name="Member for", value=member.guild.member_count, inline=False)
		await self.client.get_channel(879009713281462329).send(embed=embed)
		print(f"{member} has left the server.")
		data.write('leave', str(member.id), int(datetime.datetime.utcnow().timestamp()))


def setup(client):
	client.add_cog(Registry(client))