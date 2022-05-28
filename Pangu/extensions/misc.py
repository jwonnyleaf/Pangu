import logging

import hikari
import lightbulb

from Pangu.bot import Pangu
from Pangu.utils import constants as const

log = logging.getLogger(__name__)


misc_plugin = lightbulb.Plugin("misc")


@misc_plugin.command
@lightbulb.command("ping", "Checks the Bot's latency")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    _latency = ctx.bot.heartbeat_latency * 1000
    
    if _latency >= 200:
        _color = const.RED_COLOR
    elif _latency >= 100:
        _color = const.YELLOW_COLOR
    else:
        _color = const.GREEN_COLOR

    await ctx.respond(
        embed = hikari.Embed(
            title = "🏓 Pong!",
            description = f"Latency: `{_latency:.2f}ms`",
            color = _color
        )
    )


def load(bot: Pangu) -> None:
    bot.add_plugin(misc_plugin)

def unload(bot: Pangu) -> None:
    bot.remove_plugin(misc_plugin)


