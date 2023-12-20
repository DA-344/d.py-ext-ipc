import discord
from discord.ext import commands, ipc


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ipc = ipc.IPC(self)  # create our IPC Server

    async def on_ready(self):
        """Called everytime the bot starts a websocket connection"""
        print("Bot is ready.")

    async def on_ipc_start(self):
        """Called when IPC server is running"""
        print('IPC is ready!')


my_bot = MyBot(command_prefix="!", intents=discord.Intents.all())


@my_bot.ipc.app.route()
async def get_member_count(data):
    guild = my_bot.get_guild(data.guild_id)
    # or...
    # guild = my_bot.ipc.get('guild', data.guild_id)

    return guild.member_count


if __name__ == "__main__":

    # Fist way to run it, not recommended though because it is blocking code
    # my_bot.ipc.start()  # start the IPC Server
    # my_bot.run("TOKEN")

    # Instead try using this:
    my_bot.ipc.run("TOKEN")
    # This runs both the web-server app and the bot at the same time.
