from discord.ext import commands


## These are the cog management commands ##

class CogCommands(commands.Cog, name='Cog Commands'):

	def __init__(self, client):
		self.client = client
		print('cog_commands online!')

	## The default check for this cog whenever a command is used. Returns True if the command is allowed. ##
	async def author_check(self, ctx):  
		return ctx.author.id in self.client.author_id

	## Reloads a cog ##
	@commands.command()
	async def reload(self, ctx, cog='all'):
		extensions = self.client.extensions
		if cog == 'all':
			for extension in extensions:
				self.client.unload_extension(extension)
				self.client.load_extension(extension)
			print('Reloaded all cogs!')
			await ctx.send('Reloaded all cogs!')	
		elif cog in extensions:
			self.client.unload_extension(cog)
			self.client.load_extension(cog)
			print(f'Reloaded {cog}!')
			await ctx.send(f'Reloaded {cog}!')
		else:
			print(f'{cog} is not loaded!')
			await ctx.send(f'{cog} is not loaded!')
	
	## Unload a cog ##
	@commands.command()
	async def unload(self, ctx, cog):
		extensions = self.client.extensions
		if cog in extensions:
			self.client.unload_extension(cog)
			print(f'Unloaded {cog}!')
			await ctx.send(f'Unloaded {cog}!')
		else:
			print(f'{cog} is not loaded!')
			await ctx.send(f'{cog} is not loaded!')
	
	## Loads a cog ##
	@commands.command()
	async def load(self, ctx, cog):
		try:
			self.client.load_extension(cog)
			print(f'Loaded {cog}!')
			await ctx.send(f'Loaded {cog}!')

		except commands.errors.ExtensionNotFound:
			print(f'{cog} does not exist!')
			await ctx.send(f'{cog} does not exist!')

	## Returns a list of all enabled commands ##
	@commands.command()
	async def listcogs(self, ctx):
		base_string = '```css\n'
		base_string += '\n'.join([str(cog) for cog in self.client.extensions])
		base_string += '\n```'
		await ctx.send(base_string)


def setup(client):
	client.add_cog(CogCommands(client))