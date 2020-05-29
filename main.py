from discord.ext import commands
from config import TOKEN


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Bot started')
    bot.load_extension('weather')

bot.run(TOKEN)
