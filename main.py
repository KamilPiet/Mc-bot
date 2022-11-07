import os
import discord
import asyncio
from discord.ext import commands
from mc_api import get_server_status

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot {0.user} '.format(bot) + ' started')
    is_online, number_of_players = get_server_status()
    if is_online:
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game("Online, liczba graczy: {}".format(number_of_players)))
    else:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("Offline"))


@bot.command(name='players', brief="",
             description="")
# !players
async def print_players_names(ctx, arg):
    pass

bot.run(os.getenv('TOKEN'))
