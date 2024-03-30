import discord
from config import token
import random
from simple_gpt import gpt

bot = discord.Client(intents=discord.Intents.all())


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP[ASDFGHJKL;ZXCVBNM,./]"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'hello':
        await message.channel.send("Hi!")
    elif message.content == 'by':
        await message.channel.send(":sob:")
    elif message.content == 'random':
        await message.channel.send(str(random.randint(1,100)))
    elif message.content == 'password':
        await message.channel.send(gen_pass(12))
    else:
        await message.channel.send(gpt(message.content))

bot.run(token)