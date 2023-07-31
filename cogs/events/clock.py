import datetime
from discord.ext import commands, tasks


class Clock(commands.Cog, name='Clock Channel'):

	def __init__(self, client):
		self.client = client
		print('clock online!')

	## The default check for this cog whenever a command is used. Returns True if the command is allowed. ##
	async def author_check(self, ctx):  
		return ctx.author.id in self.client.author_id

	## Server Clock Looping Function ##
	@tasks.loop(minutes=10)
	async def clock_name(self):
		if datetime.datetime.utcnow().strftime("%H") == "00":
			reset = f'Reset!!!'
		elif datetime.datetime.utcnow().strftime("%H") == "12":
			reset = f'Reset±12'
		elif int(datetime.datetime.utcnow().strftime("%H")) < 12:
			reset = f'Reset+{datetime.datetime.utcnow().strftime("%I")}'
		else:
			reset = f'Reset-{12-int(datetime.datetime.utcnow().strftime("%I"))}'
		current_time = f'{reset}　|　{datetime.datetime.utcnow().strftime("%R")} - UTC'
		await self.client.get_channel(879009710907482127).edit(name=current_time)
		print(f'Updated clock: {datetime.datetime.utcnow().strftime("%R")}')

	## Start looping function ##
	@commands.command()
	async def start_clock(self, ctx):
		self.clock_name.start()
		await ctx.send("Clock started!")
		print("Started clock")

	## Stop looping function ##
	@commands.command()
	async def stop_clock(self, ctx):
		self.clock_name.cancel()
		await ctx.send("Clock stopped!")
		print("Stopped clock")


def setup(client):
	client.add_cog(Clock(client))