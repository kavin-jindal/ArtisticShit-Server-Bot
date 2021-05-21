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
import urllib.request
import emoji

name="UCXX3bQwpddMsgHMSj-2opJA"


key=''


data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key=AIzaSyAGQcG9ssOwRxVnkISJBHVVzLWA9nYBRrA").read()
subs=json.loads(data)["items"][0]["statistics"]["subscriberCount"]
vids=json.loads(data)["items"][0]["statistics"]["videoCount"] 


a=emoji.emojize("%d" %int(subs) +" subscribers")
b=emoji.emojize("%d" %int(vids) +" videos")


yt_list = ['Check out the latest video by Artisticshit \n https://www.youtube.com/watch?v=rq-mnfOXpI0',
'https://www.youtube.com/watch?v=dAxIrcs4COU',
'https://www.youtube.com/watch?v=XE8zXc-D3hY',
'https://www.youtube.com/watch?v=cN6PltuRmzM',
'https://www.youtube.com/watch?v=xP87aOohvII',
'Check out the most popular video on the Official ArtisticShit Channel \n https://www.youtube.com/watch?v=k1-koFbn1Ug',
'https://www.youtube.com/watch?v=UfH8HWvDgKI',
'https://www.youtube.com/watch?v=QB6PbpBZUqA',
'https://www.youtube.com/watch?v=N47cwD5kYhM',]
class Youtube(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vids(self, ctx):
      await ctx.send(random.choice(yt_list))

    @commands.command()
    async def channel(self, ctx):
      yt_channel = discord.Embed(
        title = 'Official Channel of ArtisticShit' '\n' '--------------', 
        colour = discord.Colour.red()
      )
      
      yt_channel.set_thumbnail(url = 'https://media.giphy.com/media/QFnuuHeRSz6Mh5fKr2/giphy.gif')
      yt_channel.set_image(url = 'https://cdn.discordapp.com/attachments/802781270248652822/844443108804132914/unnamed.jpg')
      yt_channel.add_field(name = 'Subscriber Count', value=a)
      yt_channel.add_field(name = 'Video Count', value=b)
      yt_channel.add_field(name = 'Make sure to subscribe :)', 
      value='[ArtisticShit](https://www.youtube.com/channel/UCXX3bQwpddMsgHMSj-2opJA)', inline=False)
      await ctx.send(embed = yt_channel)
      
      
      
     
        

    

def setup(client):
    client.add_cog(Youtube(client))
