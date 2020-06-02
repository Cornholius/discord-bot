import discord
from discord.ext import commands
import requests
import random
from config import *


class Weather(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='погода')
    async def tell_weather_command(self, ctx):
        headers = {'X-Yandex-API-Key': api_key}
        url = 'https://api.weather.yandex.ru/v1/informers?lat=59.9386&lon=30.3141&extra=false'
        r = requests.get(url, headers=headers).json()
        temp_now_data = r['fact']
        temp_forecast_data = r['forecast']
        text = []
        now = '{condition}\n' \
               'Температура {temp} °C\n' \
               'По ощущениям {feels_like} °C\n' \
               'Ветер {wind_speed} м/с {wind_dir}\n' \
               ''.format(condition=condition[temp_now_data['condition']],
                         temp=temp_now_data['temp'],
                         feels_like=temp_now_data['feels_like'],
                         wind_speed=temp_now_data['wind_speed'],
                         wind_dir=wind_dir[temp_now_data['wind_dir']])
        text.append(now)
        for i in list(temp_forecast_data['parts']):
            period = 'Температура {part_name} {temp_avg} °C\n' \
                     'По ощущениям {feels_like} °C\n' \
                     'Ветер {wind_speed} м/с {wind_dir}\n' \
                     '{condition}\n'.format(part_name=part_name[i['part_name']],
                                            temp_avg=i['temp_avg'],
                                            feels_like=i['feels_like'],
                                            wind_speed=i['wind_speed'],
                                            wind_dir=wind_dir[i['wind_dir']],
                                            condition=condition[temp_now_data['condition']])
            text.append(period)

        embed = discord.Embed(title='Погода на сегодня',
                              description="\n".join(map(str, text)),
                              color=random.choice(color_list))
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        msg = await ctx.send(content='Now generating the embed...')
        await msg.edit(embed=embed, content=None)
# print("\n".join(map(str, qwe)))


def setup(bot):
    bot.add_cog(Weather(bot))
