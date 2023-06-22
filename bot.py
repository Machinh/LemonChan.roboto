import discord
from discord.ext import commands

# Configuração do bot
token = ''
prefixo = '!'

# Criação do bot
bot = commands.Bot(command_prefix=prefixo)

# Evento de inicialização do bot
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

# Comando básico
@bot.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}!')

# Comando de repetição
@bot.command()
async def repetir(ctx, *, mensagem):
    await ctx.send(mensagem)

# Execução do bot
bot.run(token)
