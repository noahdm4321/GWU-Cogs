"""WelcomeRand - Welcomes users with a randomly generated message."""
import asyncio

from .welcomerand import WelcomeRand


async def setup(bot):
    """Load welcomerand."""
    cog = WelcomeRand()

    if asyncio.iscoroutinefunction(bot.add_cog):
        await bot.add_cog(cog)
    else:
        bot.add_cog(cog)
