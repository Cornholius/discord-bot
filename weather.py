from discord.ext import commands


class Weather(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='погода')
    async def tell_weather_command(self, ctx):
        member = '<@{mem}>'.format(mem=ctx.message.author.id)
        await ctx.send('{member} Ублюдок, мать твою, а ну иди сюда говно собачье,'
                       ' решил ко мне лезть? Ты, засранец вонючий, мать твою, а?'
                       ' Ну иди сюда, попробуй меня трахнуть, я тебя сам трахну ублюдок,'
                       ' онанист чертов, будь ты проклят, иди идиот, трахать тебя и всю семью,'
                       ' говно собачье, жлоб вонючий, дерьмо, сука, падла, иди сюда, мерзавец,'
                       ' негодяй, гад, иди сюда ты - говно, ЖОПА!'.format(member=member))


def setup(bot):
    bot.add_cog(Weather(bot))
