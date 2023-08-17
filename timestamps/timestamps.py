from datetime import datetime
import dateparser
import discord
from redbot.core import commands
from redbot.core.bot import Red, app_commands
from redbot.core.commands import BadArgument, Cog, Converter


class TimeStamps(Cog):
    """Retrieve timestamps for certain dates."""

    __author__ = "noahdm4321"
    __version__ = "1.0"

    def __init__(self, bot: Red):
        self.bot = bot

    async def convert(self, arg) -> datetime:
        """Date converter which uses dateparser.parse()."""
        parsed = dateparser.parse(arg)
        if parsed is None:
            raise BadArgument("Unrecognized date/time.")
        return parsed

    @app_commands.command()
    @app_commands.describe(time="The time you want")
    async def timestamp(self, interaction: discord.Interaction, time: str):
        """Produce a Discord timestamp.

        Timestamps are a feature added to Discord in the summer of 2021,
        which allows you to send timestamps will which update accordingly
        with any user's date time settings.

        **Example Usage**

        - `/timestamp 1st of october, 2021`
        - `/timestamp 20 hours ago`
        - `/timestamp in 50 minutes`
        - `/timestamp 01/10/2021`
        - `/timestamp now`
        """
        try:
            ts = int(self.convert(time))
        except OSError:
            await interaction.response.send_message(
                "An operating system error occured whilst attempting to get "
                "information for this timestamp.", ephemeral=True
            )
            return
        message = f"Timestamps for **<t:{ts}:F>**\n\n"
        # I'm aware that discord.utils.format_dt exists, but I prefer this layout
        # for readability purposes (and its more efficient for this specific use case)
        for i in "fdt":
            message += f"`<t:{ts}:{i.upper()}>`: <t:{ts}:{i.upper()}>\n"
            message += f"`<t:{ts}:{i.lower()}>`: <t:{ts}:{i.lower()}>\n"
        message += f"`<t:{ts}:R>`: <t:{ts}:R>\n"
        await interaction.response.send_message(message,ephemeral=True)
