import os
import logging
import dotenv

import hikari
import lightbulb

dotenv.load_dotenv()

log = logging.getLogger(__name__)

class Pangu(lightbulb.BotApp):
    """Custom Class for Lightbulb Bot"""

    def __init__(self) -> None:
        super().__init__(
            token = os.environ["TOKEN"],
            prefix = lightbulb.when_mentioned_or('`'),
            intents = hikari.Intents.ALL,
            default_enabled_guilds = (int(os.environ["DEFAULT_GUILD_ID"]),),
            banner = None,
        )

        self.register_listeners()

    def register_listeners(self) -> None:
        self.subscribe(hikari.StartingEvent, self.on_starting)

    async def on_starting(self, event: hikari.StartingEvent) -> None:
        log.info("Pangu is Starting...")
        self.load_extensions_from("./extensions/", must_exist = True, recursive = True)

    async def on_started(self, event: hikari.StartedEvent) -> None:
        logging.info(f"Succesfully Booted, initialized as Pangu.")
        activity = hikari.Activity(name = f"@jwonnyleaf • Version 0.1", type = hikari.ActivityType.PLAYING)
        await self.update_presence(activity)
            
    