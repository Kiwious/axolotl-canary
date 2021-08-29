import asyncio
from os import terminal_size
from types import prepare_class
from lib.db.db import record
from discord.ext.commands import bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler

PREFIX = "/"
OWNER_IDS = [733403498766401554]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Bot ready")

    async def on_disconnect(self):
        print("Bot logged off")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(864146228232060958)
            print("Bot ready")

        else: 
            print("Bot reconnected")


    async def on_message(self, message):
        pass

bot = Bot()

