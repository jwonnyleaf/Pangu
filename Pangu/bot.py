import os
import logging
import dotenv

import hikari
import lightbulb

from Pangu.database.db import Database

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

        # Initializing Database
        self._db = Database(self)

        # Initializing Listeners
        self.register_listeners()

    def register_listeners(self) -> None:
        self.subscribe(hikari.StartingEvent, self.on_starting)
        self.subscribe(hikari.StartedEvent, self.on_started)
        self.subscribe(hikari.GuildJoinEvent, self.on_guild_join)

    async def on_starting(self, event: hikari.StartingEvent) -> None:
        log.info("Pangu is Starting...")
        # Connect to Database
        await self._db.connect()

        # Load Extensions
        self.load_extensions_from("Pangu/extensions", must_exist = True)

    async def on_started(self, event: hikari.StartedEvent) -> None:
        logging.info(f"Succesfully Booted, initialized as Pangu.")

        # Set Bot Activity / Status
        await self.update_presence(
            activity = hikari.Activity(
                name = f" # Guilds • V0.1", 
                type = hikari.ActivityType.WATCHING
            )
        )

    async def database(self) -> Database:
        return self._db
            
    
    async def on_guild_join(self, event: hikari.GuildJoinEvent) -> None:
        # Update Guild Members
        await self._db.execute(
            "INSERT INTO guilds (guild_id, prefix) VALUES ($1, $2) ON CONFLICT (guild_id) DO NOTHING", event.guild_id, "`"
        )
        log.info(f"Pangu has been added by a new guild: {event.guild.name} ({event.guild_id})!")

        