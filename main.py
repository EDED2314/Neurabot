from os import getenv
import discord
from discord import app_commands
from discord.interactions import Interaction

class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
    
    async def on_ready(self):
        if not self.synced:
            await commands.sync(guild=discord.Object(id=941049795949264969))
            print("Ready.")

bot = Bot()
commands = app_commands.CommandTree(bot)