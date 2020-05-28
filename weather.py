from discord.ext import commands
import requests


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
        temp_now = temp_now_data['temp']
        feels_like = temp_now_data['feels_like']
        wind_speed
        wind_dir
        condition
        humidity
        prec_type
        prec_strength






        member = '<@{mem}>'.format(mem=ctx.message.author.id)
        await ctx.send('{member}'.format(member=member))


def setup(bot):
    bot.add_cog(Weather(bot))
