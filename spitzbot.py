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
        if '虹を越えて' in message.content:
            with open('NIZIWOKOETE.txt') as niziwokoete:
                kasi_niziwokoete = niziwokoete.read()
            await message.channel.send(kasi_niziwokoete)
        if '会いに行くよ' in message.content:
            with open('ainiikuyo.txt') as ainiikuyo:
                kasi_ainiikuyo = ainiikuyo.read()
            await message.channel.send(kasi_ainiikuyo)
        if '愛のことば' in message.content:
            with open('ainokotoba.txt') as ainokotoba:
                kasi_ainokotoba = ainokotoba.read()
            await message.channel.send(kasi_ainokotoba)
        if '愛のしるし' in message.content:
            with open('ainosirusi.txt') as ainosirusi:
                kasi_ainosirusi = ainosirusi.read()
            await message.channel.send(kasi_ainosirusi)
        if 'アカネ' in message.content:
            with open('akane.txt') as akane:
                kasi_akane = akane.read()
            await message.channel.send(kasi_akane)
        if 'あかりちゃん' in message.content:
            with open('akarityan.txt') as akarityan:
                kasi_akarityan = akarityan.read()
            await message.channel.send(kasi_akarityan)
        if 'あかさたな' in message.content:
            with open('akasatana.txt') as akasatana:
                kasi_akasatana = akasatana.read()
            await message.channel.send(kasi_akasatana)
        if '悪役' in message.content:
            with open('akuyaku.txt') as akuyaku:
                kasi_akuyaku = akuyaku.read()
            await message.channel.send(kasi_akuyaku)
        if '甘い手' in message.content:
            with open('amaite.txt') as amaite:
                kasi_amaite = amaite.read()
            await message.channel.send(kasi_amaite)
        if '甘ったれクリーチャー' in message.content:
            with open('amattarekuri-tya-.txt') as amattarekuritya:
                kasi_amattarekuritya = amattarekuritya.read()
            await message.channel.send(kasi_amattarekuritya)
        if '青い車' in message.content:
            with open('aoikuruma.txt') as aoikuruma:
                kasi_aoikuruma = aoikuruma.read()
            await message.channel.send(kasi_aoikuruma)
        if 'アパート' in message.content:
            with open('apa-to.txt') as apato:
                kasi_apato = apato.read()
            await message.channel.send(kasi_apato)
        if 'ありがとさん' in message.content:
            with open('arigatosan.txt') as arigatosan:
                kasi_arigatosan = arigatosan.read()
            await message.channel.send(kasi_arigatosan)
        if 'ありふれた人生' in message.content:
            with open('arihuretazinsei.txt') as arihuretazinsei:
                kasi_arihuretazinsei = arihuretazinsei.read()
            await message.channel.send(kasi_arihuretazinsei)
        if '歩き出せ、クローバー' in message.content:
            with open('arukidasekuro-ba-.txt') as arukidasekuroba:
                kasi_arukidasekuroba = arukidasekuroba.read()
            await message.channel.send(kasi_arukidasekuroba)
        if 'あわ' in message.content:
            with open('awa.txt') as awa:
                kasi_awa = awa.read()
            await message.channel.send(kasi_awa)
        if 'あじさい通り' in message.content:
            with open('azisaidoori.txt') as azisaidoori:
                kasi_azisaidoori = azisaidoori.read()
            await message.channel.send(kasi_azisaidoori)
        if 'ババロア' in message.content:
            with open('babaroa.txt') as babaroa:
                kasi_babaroa = babaroa.read()
            await message.channel.send(kasi_babaroa)
        if 'バニーガール' in message.content:
            with open('bani-ga-ru.txt') as banigaru:
                kasi_banigaru = banigaru.read()
            await message.channel.send(kasi_banigaru)
        if 'ベビーフェイス' in message.content:
            with open('bebi-feisu') as bebifeisu:
                kasi_bebifeisu = bebifeisu.read()
            await message.channel.send(kasi_bebifeisu)
        if 'ビー玉' in message.content:
            with open('bi-dama.txt') as bidama:
                kasi_bidama = bidama.read()
            await message.channel.send(kasi_bidama)
        if 'ビギナー' in message.content:
            with open('bigina-.txt') as bigina:
                kasi_bigina = bigina.read()
            await message.channel.send(kasi_bigina)
        if '僕はきっと旅に出る' in message.content:
            with open('bokuhakittotabinideru.txt') as bokuhakittotabinideru:
                kasi_bokuhakittotabinideru = bokuhakittotabinideru.read()
            await message.channel.send(kasi_bokuhakittotabinideru)
        if '僕はジェット' in message.content:
            with open('bokuhazyetto.txt') as bokuhazyetto:
                kasi_bokuzyatto = bokuhazyetto.read()
            await message.channel.send(kasi_bokuhazyetto)
        if '僕のギター' in message.content:
            with open('bokunogita-.txt') as bokunogita:
                kasi_bokunogita = bokunogita.read()
            await message.channel.send(kasi_bokunogita)
        if '僕の天使マリ' in message.content:
            with open('bokunotensimari.txt') as bokunotensimari:
                kasi_bokunotensimari = bokunotensimari.read()
            await message.channel.send(kasi_bokunotensimari)
        if 'ブービー' in message.content:
            with open('bu-bi-.txt') as bubi:
                kasi_bubi = bubi.read()
            await message.channel.send(kasi_bubi)
        if 'ブランケット' in message.content:
            with open('buranketto.txt') as buranketto:
                kasi_buranketto = buranketto.read()
            await message.channle.send(kasi_buranketto)
        if 'ブチ' in message.content:
            with open('buti.txt') as buti:
                kasi_buti = buti.txt
            await message.channel.send(kasi_buti)
        if 'どんどどん' in message.content:
            with open('dondodon.txt') as dondodon:
                kasi_dondodon = dondodon.read()
            await message.channel.send(kasi_dondodon)
        if 'ドルフィン・ラヴ' in message.content:
            with open('dorufinravu.txt') as dorufinravu:
                kasi_dorufinravu = dorufinravu.read()
            await message.channel.send(kasi_dorufinravu)
           
                                       
                                                    
            
client.run(token)
