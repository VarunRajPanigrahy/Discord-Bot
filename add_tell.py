import os
import random
import sqlite3
import discord.client
from discord.ext import commands
from dotenv import load_dotenv
from discord.utils import get
import dbp
from datetime import date
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

dbp.create_table()
client=discord.Client()
@bot.command(name='add', help='Add hours to your coding streak.')
async def add(ctx, hours:float):
    
    name=ctx.message.author.name

    dbp.insert_data(name,hours)

    #channel=get(ctx.message.server.channels,name="test-channel",type=discord.ChannelType.text)
    #print(channel)

    #await ctx.send(channel,"hi")

@bot.command(name="tell",help='know how many hours you have coded.')
async def tell(ctx):
    name=ctx.message.author.name
    hours=dbp.find(name)
    await ctx.send(hours)

@client.event
async def on_message(message):
    cont=message.content
    today=date.today()
    if(cont=="!done"):
        guild=get(client.guilds,name="samurai_01")
        channel=get(guild.channels,name="daily-coding-streak")
        await channel.send(f'Congrats {message.author.name} you have completed coding on {today}')



client.run(TOKEN)

bot.run(TOKEN)