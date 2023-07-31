from discord.ext import commands


## These are the commands for the server ##

class ServerCommands(commands.Cog, name='Server Commands'):

	def __init__(self, client):
		self.client = client
		print('server online!')


	## Tests the latency of the bot ##
	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong! Latency: {round(self.client.latency * 1000)}ms')
		print(f'{ctx.author} pinged in #{ctx.channel}')


def setup(client):
	client.add_cog(ServerCommands(client))