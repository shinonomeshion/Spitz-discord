import discord
import asyncio
import os

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('起動しました')

@client.event
async def on_message(message):
    if '#spitz' in message.content:
        if '12月の雨の日' in message.content or '１２月の雨の日' in message.content:
            with open('12gatunoamenohi.txt') as gatunoamenohi:
                kasi_12gatunoamenohi = gatunoamenohi.read()
            await message.channel.send(kasi_12gatunoamenohi)
        if '14番目の月' in message.content or '１４番目の月' in message.content:
            with open('14banmenotuki.txt') as banmenotuki:
                kasi_14banmenotuki = banmenotuki.read()
            await message.channel.send(kasi_14banmenotuki)
        
            


client.run(token)
