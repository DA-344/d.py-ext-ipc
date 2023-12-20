import discord
from discord.ext import commands, ipc


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.IPC(self)  # create our IPC Server

        self.load_extension("cogs.ipc")  # load the IPC Route cog

    async def on_ready(self):
        """Called everytime the bot starts a websocket connection"""
        print("Bot is ready.")

    async def on_ipc_ready(self):
        """Called when IPC server is running"""
        print("IPC is ready!")


my_bot = MyBot(command_prefix="!", intents=discord.Intents.all())


if __name__ == "__main__":
    my_bot.ipc.run("TOKEN")
