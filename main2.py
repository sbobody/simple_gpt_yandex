import discord
from discord.ext import commands
from config import token
import random
import simple_gpt
import os 
import requests

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
    t = simple_gpt.gpt('Ответь на этот вопрос в контексте загрязнения окружающей среды, не говори что вопрос не связан с темой экологии, просто ответь, вот вопрос -' + t)
    t = t.split('.')
    for x in t:
        await ctx.send(x + ".")

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command('sprut')
async def sprut(ctx,plast):
    await ctx.send(simple_gpt.gpt(f'сколько разалгается {plast} по продолжительности в среднем'))
@bot.command('tresh')
async def tresh(ctx,mysor):
    await ctx.send(simple_gpt.gpt(f'как правильно утелизировать {mysor}')) 

bot.run(token)