import discord
import json
import asyncio
from discord.ext import commands
## discord.py documentation: https://discordpy.readthedocs.io/en/latest/api.html ##
## discord-components documentation: https://devkiki7000.gitbook.io/discord-components/ ##


# class CustomHelpCommand(commands.HelpCommand):

# 	def __init__(self):
# 		super().__init__()

# 	async def send_bot_help(self, mapping):
# 		for cog in mapping:
# 			await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]}')
	
# 	async def send_cog_help(self, cog):
# 		await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')

# 	async def send_group_help(self, group):
# 		await self.get_destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')

# 	async def send_command_help(self, command):
# 		await self.get_destination().send(command.name)


client = commands.Bot(command_prefix=[".", "<@!868102182128472075> "], case_insensitive=True, intents = discord.Intents.all())

client.author_id = [243543671293739008, 253988841885663233, 196275232774946817, 363469476764712971]
def author_check(ctx):
	return ctx.author.id in client.author_id



@client.event 
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Activity(name='for commands', type=discord.ActivityType.listening))
	print(f'Bot is ready: {client.user}')

## Error messages ##
@client.event 
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send('Missing required arguments.')
		print(error)
	elif isinstance(error, commands.TooManyArguments):
		await ctx.send("What's that last bit for? Now you're confusing me.")
		print(error)
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send('You do not have permission to use that command.')
		print(error)
	elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
		await ctx.send('You do not have the proper roles to use that command.')
		print(error)
	elif isinstance(error, commands.NotOwner):
		await ctx.send("That command can only be used by <@196692788283179008>. And you're him, are you?")
		print(error)
	elif isinstance(error, (commands.CheckFailure, commands.CheckAnyFailure)):
		await ctx.send('No')
		print(error)
	elif isinstance(error, commands.CommandNotFound):
		await ctx.send('There is no such command in my code. Check your spelling and try again.')
		print(error)
	elif isinstance(error, commands.UserNotFound):
		await ctx.send('User does not exist. Please double check and try again.')
		print(error)
	elif isinstance(error, commands.MessageNotFound):
		await ctx.send('Message does not exist. Please double check and try again.')
		print(error)
	elif isinstance(error, commands.ChannelNotFound):
		await ctx.send('Channel does not exist. Please double check and try again.')
		print(error)
	elif isinstance(error, commands.EmojiNotFound):
		await ctx.send('Emoji does not exist. Please double check and try again.')
		print(error)
	elif isinstance(error, commands.RoleNotFound):
		await ctx.send('Role does not exist. Please double check and try again.')
		print(error)
	elif isinstance(error, commands.GuildNotFound):
		await ctx.send('Server does not exist. Please double check and try again.')
		print(error)
	elif isinstance(error, (commands.BadArgument, commands.BadBoolArgument)):
		await ctx.send('Unrecognizable argument type. Please try again.')
		print(error)
	elif isinstance(error, commands.CommandOnCooldown):
		await ctx.send('Alright, alright. Give me a second. Geez.')
		print(error)
	elif isinstance(error, commands.CommandInvokeError):
		await ctx.send("Read the documentation please.")
		print(error)
	elif isinstance(error, commands.DisabledCommand):
		await ctx.send('That command is no longer supported. Sorry.')
		print(error)
	elif isinstance(error, (commands.ExpectedClosingQuoteError, commands.InvalidEndOfQuotedStringError)):
		await ctx.send("Wait. That's it? You can't leave me hanging like that.")
		print(error)
	elif isinstance(error, commands.UnexpectedQuoteError):
		await ctx.send("Ok. I don't need your sass right now. Try again without quotes.")
		print(error)
	elif isinstance(error, (commands.ExtensionError, commands.ExtensionFailed)):
		await ctx.send('Everything is failing! This is the end for me. Goodbye.')
		await ctx.sent('https://tenor.com/view/everything-is-fine-dog-fire-burning-nothing-wrong-gif-15379714')
		print(error)
		await asyncio.sleep(5)
		await client.change_presence(status=discord.Status.offline)
	elif isinstance(error, commands.ExtensionAlreadyLoaded):
		await ctx.send('I already did that. You want me to do it again?')
		print(error)
	elif isinstance(error, (commands.ExtensionNotFound, commands.ExtensionNotLoaded)):
		await ctx.send("What's that? Sounds pretty cool.")
		print(error)
	elif isinstance(error, commands.NoPrivateMessage):
		await ctx.send('Try asking me on the sever. That might work better.')
		print(error)
		await asyncio.sleep(2)
		await ctx.send('Maybe...')
		await asyncio.sleep(1)
		await ctx.send('Worth a shot at least.')
	elif isinstance(error, commands.PrivateMessageOnly):
		await ctx.send("Let's move this conversation to a private channel. Away from prying eyes :eyes:")
		print(error)
	elif isinstance(error, commands.NSFWChannelRequired):
		await ctx.send(":open_mouth: How lewd! I'm afraid my conscience won't allow me to do that.")
		print(error)
		await asyncio.sleep(1)
		await ctx.send("Just because I'm a bot doesn't mean I'm morally indigent.")
	else:
		await ctx.send(f"Unknown error. Ask a <@&877374498201018410> for help. They'll figure it out.")
		print(error)


## Log messages deleted ##
@client.event 
async def on_message_delete(message):
	print(f'Message from {message.author} deleted in #{message.channel}: "{message.clean_content}"')



## Extensions to load on startup ##
extensions = ['cogs.cog_commands', 
	'cogs.commands.mod',
	'cogs.commands.server',
	'cogs.events.registry',
	'cogs.events.clock']

## Ensures this is the file being ran ##
if __name__ == '__main__':
	for extension in extensions:
		client.load_extension(extension)

## Start Bot ##
config = json.load(open("config.json"))
client.run(config["token"])