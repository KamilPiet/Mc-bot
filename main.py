import os
import discord
import asyncio
from discord.ext import commands, tasks
from mc_api import get_server_status

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot {0.user} '.format(bot) + ' started')
    update_status.start()


@bot.command(name='status', brief="Prints current server status", description="Prints current server status")
# !status
async def print_status(ctx):
    is_online, number_of_players = get_server_status()
    if is_online:
        await ctx.send("Serwer jest online, liczba graczy: {}".format(number_of_players))
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game("Online, liczba graczy: {}".format(number_of_players)))
    else:
        await ctx.send("Serwer jest offline")
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Offline"))


@tasks.loop(minutes=5)
async def update_status():
    is_online, number_of_players = get_server_status()
    if is_online:
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game("Online, liczba graczy: {}".format(number_of_players)))
    else:
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Offline"))


bot.run(os.getenv('TOKEN'))
