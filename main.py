from discord.ext import commands
from config import TOKEN


bot = commands.Bot(command_prefix='!')
cogs = ['weather', 'kinopoisk']


@bot.event
async def on_ready():
    print('Bot started')
    for cog in cogs:
        bot.load_extension(cog)

bot.run(TOKEN)
