from discord.ext import commands


class IpcRoutes(commands.Cog):

    bot = None # fist set to none so when the __init__ is called we
               # set it as our actual bot
    
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @bot.ipc.app.route()
    async def get_member_count(self, data):
        guild = self.bot.get_guild(data.guild_id)  # get the guild object using parsed guild_id

        return guild.member_count  # return the member count to the client


async def setup(bot):
    await bot.add_cog(IpcRoutes(bot))
