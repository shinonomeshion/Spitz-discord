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
    if '#spitz' in message.content or '#Spitz' in message.content:
        if '12月の雨の日' in message.content or '１２月の雨の日' in message.content:
            with open('12gatunoamenohi.txt') as gatunoamenohi:
                kasi_12gatunoamenohi = gatunoamenohi.read()
            await message.channel.send(kasi_12gatunoamenohi)
        if '14番目の月' in message.content or '１４番目の月' in message.content:
            with open('14banmenotuki.txt') as banmenotuki:
                kasi_14banmenotuki = banmenotuki.read()
            await message.channel.send(kasi_14banmenotuki)
        if '1987' in message.content or '１９８７' in message.content:
            with open('1987.txt') as itikyuuhatinana:
                kasi_1987 = itikyuuhatinana.read()
            await message.channel.send(kasi_1987)
        if '8823' in message.content or '８８２３' in message.content:
            with open('8823.txt') as hayabusa:
                kasi_8823 = hayabusa.read()
            await message.channel.send(kasi_8823)
            


client.run(token)
