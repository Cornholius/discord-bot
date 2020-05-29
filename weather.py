from discord.ext import commands
import requests
import discord

class Weather(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='погода')
    async def tell_weather_command(self, ctx):
        key = 'a7cb15e0-43e3-4506-8fe6-3e567b02fa5b'
        headers = {'X-Yandex-API-Key': key}
        url = 'https://api.weather.yandex.ru/v1/forecast?lat=55.75396&lon=37.620393&extra=true'
        r = requests.get(url, headers=headers)
        r = r.json()
        temp_now_data = r['fact']
        member = '<@{mem}>'.format(mem=ctx.message.author.id)
        text = '{member} погода на сегодня:*' \
               '{condition}*' \
               'температура {temp}*' \
               'ощущается как {feels_like}*' \
               'ветер {wind_speed}*' \
               ''.format(member=member,
                         condition=temp_now_data['condition'],
                         temp=temp_now_data['temp'],
                         feels_like=temp_now_data['feels_like'],
                         wind_speed=temp_now_data['wind_speed'])
        # await ctx.send('\n'.join(text.split('*')))
        embed = discord.Embed(title=member, description='\n'.join(text.split('*')))

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        msg = await ctx.send(content='Now generating the embed...')

        await msg.edit(embed=embed)

def setup(bot):
    bot.add_cog(Weather(bot))
