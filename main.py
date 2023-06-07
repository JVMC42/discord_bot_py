import discord
from cotacao import mostrar_cotacao
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/Bom dia'):
        await message.channel.send('Bom dia! 🌞')

    if message.content.startswith('/cota'):
        words = message.content.split()
        ticker = words[1].upper()
        cota = mostrar_cotacao(ticker)
        await message.channel.send(cota)

    if message.content.startswith('/obrigado'):
        await message.channel.send('Não tem de que! 🙂')

    if message.content == '/Qual o melhor anime que existe?':
        file_path = os.path.abspath('imgs/oplogo.png')
        
        with open(file_path, 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)


client.run(os.getenv('DISCORD_KEY'))
