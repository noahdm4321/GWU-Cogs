import datetime

import dateparser
import discord
from redbot.core import commands
from redbot.core.bot import Red, app_commands
from redbot.core.commands import BadArgument, Cog, Context, Converter


class DateConverter(Converter):
    """Date converter which uses dateparser.parse()."""

    async def convert(self, ctx: Context, arg: str) -> datetime.datetime:
        parsed = dateparser.parse(arg)
        if parsed is None:
            raise BadArgument("Unrecognized date/time.")
        return parsed


class TimeStamps(Cog):
    """Retrieve timestamps for certain dates."""

    __author__ = "Kreusada"
    __version__ = "1.1.0"

    def __init__(self, bot: Red):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        context = super().format_help_for_context(ctx)
        return f"{context}\n\nAuthor: {self.__author__}\nVersion: {self.__version__}"

    async def red_delete_data_for_user(self, **kwargs):
        return

    @app_commands.command()
    async def timestamp(self, interaction: discord.Interaction, author: Context.author, member: discord.Member, embed: Context.embed_requested, colour: Context.embed_colour, dti: DateConverter):
        """Produce a Discord timestamp.

        Timestamps are a feature added to Discord in the summer of 2021,
        which allows you to send timestamps will which update accordingly
        with any user's date time settings.

        **Example Usage**

        - `[p]timestamp 1st of october, 2021`
        - `[p]timestamp 20 hours ago`
        - `[p]timestamp in 50 minutes`
        - `[p]timestamp 01/10/2021`
        - `[p]timestamp now`
        """
        try:
            ts = int(dti.timestamp())
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
        if await embed:
            await interaction.response.send_message(
                content=ts
                if isinstance(author, member) and author.is_on_mobile()
                else None,
                embed=discord.Embed(description=message, color=(await colour)),
                ephemeral=True,
            )
        else:
            await interaction.response.send_message(message,ephemeral=True)
