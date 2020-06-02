import requests
import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs


class KinoPoisk(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test',
                      description='тестовая функция для допиливания')
    async def introvert(self, ctx):
        all_films = []
        r = requests.get('https://www.kinopoisk.ru/premiere/').content
        soup = bs(r, 'lxml')
        container = soup.select('div.premier_item')
        for block in container:
            filmlogo_string = block.select('meta')[1]
            logo = 'https://www.kinopoisk.ru' + str(filmlogo_string['content'])
            # print(logo)
            filmname_string = block.select_one('span.name')
            filmname_href = filmname_string.select('a')
            name = filmname_href[0].text
            # print(name)
            href = 'https://www.kinopoisk.ru' + str(filmname_href[0].get('href'))
            # print(href)
            filmgenre = block.select_one('div.textBlock')
            genre = filmgenre.select('span')
            # print(genre[3].text)
            film = '{logo}\n{name}\n{href}\n{genre}'.format(logo=logo, name=name, href=href, genre=genre[3].text)
            all_films.append(film)
        embed = discord.Embed(title='1231312', description='\n'.join(i for i in all_films[:2]))
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        msg = await ctx.send(content='Now generating the embed...')
        await msg.edit(embed=embed, content=None)


def setup(bot):
    bot.add_cog(KinoPoisk(bot))
