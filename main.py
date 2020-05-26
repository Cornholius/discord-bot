import discord
from discord import utils
import config



class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    @
    async def on_message(self, message):

        command = '!ктоя'
        if message.content == command:
            print('Это был', message.author)
            role = discord.utils.get(message.guild.roles, id=714822902855368814)
            member = utils.get(message.guild.members, id=285056432808919040)
            print(role)
            member.


client = MyClient()
client.run('NzE0ODE4NTc2MTQ5OTA1NDg4.Xs0M0g.N328v8P_ABewZmXOb-51hpEa5lg')

