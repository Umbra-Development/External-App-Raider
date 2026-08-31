import discord
from discord.ext import commands

from external_app_raider import config


class SyraBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(
            command_prefix=config.prefix,
            intents=intents,
            help_command=None,
        )

        self.user_usage = {}

    async def setup_hook(self) -> None:
        extensions = (
            "external_app_raider.cogs.utils",
            "external_app_raider.cogs.raid",
        )
        for extension in extensions:
            await self.load_extension(extension)

        synced = await self.tree.sync()
        print(f"Synced {len(synced)} commands to the Discord API.")


    async def on_ready(self):
        print("""
    _________                     
    /   _____/__.__.____________   
    \\_____  <   |  |\\_  __ \\__  \\  
    /        \\___  | |  | \\// __ \\_
    /_______  / ____| |__|  (____  /
            \\/\\/                 \\/ 
    (External app)
    """)


    


############################################################
