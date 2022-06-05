import logging

import hikari
import lightbulb

from Pangu.bot import Pangu

log = logging.getLogger(__name__)


moderation_plugin = lightbulb.Plugin("moderation")

@moderation_plugin.command
@lightbulb.command("mute", "Mutes a User")
async def mute(ctx: lightbulb.Context) -> None:
    ...

def load(bot: Pangu) -> None:
    bot.add_plugin(moderation_plugin)

def unload(bot: Pangu) -> None:
    bot.remove_plugin(moderation_plugin)