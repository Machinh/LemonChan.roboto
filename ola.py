from discord.ext import commands

@commands.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}!')

def setup(bot):
    bot.add_command(ola)
