import discord
from discord.ext import commands
from config import token
import random
import simple_gpt


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def rnd(ctx):
    await ctx.send(str(random.randint(1,100)))

@bot.command()
async def gpt(ctx, *text):
    t = ''
    for x in text:
        t += x + ' '
    t = simple_gpt.gpt(t)
    t = t.split('.')
    for x in t:
        await ctx.send(x + ".")

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)



bot.run(token)