import discord
from discord.ext import commands
from discord import DMChannel
import random
import time
import keep_alive
import webbrowser
import json
import os
from discord.utils import get
import praw
from discord.voice_client import VoiceClient
import time, datetime
from discord.ext.commands import Bot
from multiprocessing.connection import Client
from discord.ext.commands.cooldowns import BucketType
import platform
import asyncio
from datetime import datetime
from discord import Intents

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
      help = discord.Embed(
        title = 'ArtisticShit YT', 
        colour = discord.Colour.teal()
      )
      help.add_field(name = 'Help', 
      value='Hey I am a bot made for the Youtube Channel of ArtisticShit. You can see the latest videos on the channel, channel statistics and much more. I am updated and managed time to time and new features are being added.')
      help.set_thumbnail(url = 'https://media.giphy.com/media/QFnuuHeRSz6Mh5fKr2/giphy.gif')
      help.add_field(name = 'Prefix', value='as!', inline=False)
      help.add_field(name = 'Commands', value='Here are the commands available for use' '\n' '`as!vids` `as!channel` `as!help`', inline=False)
      help.set_footer(text='Beta v0.1')
      await ctx.send(embed=help)

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.content == 'hello':
        await message.channel.send('hey :wave: sup... long time no see')
      if message.content == 'sup':
        await message.channel.send(f'nothin much {message.author}, life is fricked up... what bout u?')
      if message.content == 'stfu':
        await message.channel.send(f'STFU {message.author}')     
      if message.content == 'nothing much':
        await message.channel.send('hmm..') 
        

    

def setup(client):
    client.add_cog(Help(client))
