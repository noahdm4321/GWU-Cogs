import discord
from discord.ext import commands


## These are the commands for server moderation ##

class ModCommands(commands.Cog, name='Moderator Commands'):
	
	def __init__(self, client):
		self.client = client
		print('mod online!')


	## Deletes messages from a channel ##
	@commands.command(aliases=['purge'])
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=1):
		await ctx.channel.purge(limit=(amount + 1))
		print(f'{ctx.author} cleared {amount} messages in #{ctx.channel}')

	## Kicks a user from the server ##
	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member:discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f'Kicked {member.mention}! Reason: {reason}')
		print(f'{ctx.author} kicked {member} because {reason}')

	## Bans a user from the server ##
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member:discord.Member, *, reason=None):
		await member.ban(reason=reason)
		await ctx.send(f'Banned {member.mention}! Reason: {reason}')
		print(f'{ctx.author} banned {member} because {reason}')

	## Removes the ban on a user from the server ##
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')
		for ban_entry in banned_users:
			user = ban_entry.user
			if (user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
				print(f'{ctx.author} unbanned {member}')
				return


def setup(client):
	client.add_cog(ModCommands(client))