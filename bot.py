import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}!')

bot.run('SEU_TOKEN_AQUI')
