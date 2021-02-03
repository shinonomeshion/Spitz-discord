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
        if 'エンドロールには早すぎる' in message.content:
            with open('endoro-runihahayasugiru.txt') as endororunihahayasugiru:
                kasi_endororunihahayasugiru = endororunihahayasugiru.read()
            await message.channel.send(kasi_endororunihahayasugiru)
        if 'えにし' in message.content:
            with open('enisi.txt') as enisi:
                kasi_enisi = enisi.read()
            await message.channel.send(kasi_enisi)
        if 'エスカルゴ' in message.content:
            with open('esukarugo.txt') as esukarugo:
                kasi_esukarugo = esukarugo.read()
            await message.channel.send(kasi_esukarugo)
        if 'エスペランサ' in message.content:
            with open('esuperansa.txt') as esuperansa:
                kasi_esuperansa = esuperansa.read()
            await message.channel.send(kasi_esuperansa)
        if 'エトランゼ' in message.content:
            with open('etoranze.txt') as etoranze:
                kasi_etoranze = etoranze.read()
            await message.channel.send(kasi_etoranze)
        if 'フェイクファー' in message.content:
            with open('feikufa-.txt') as feikufa:
                kasi_feikufa = feikufa.read()
            await message.channel.send(kasi_feikufa)
        if 'ガーベラ' in message.content:
            with open('ga-bera.txt') as gabera:
                kasi_gabera = gabera.read()
            await message.channel.send(kasi_gabera)
        if 'ガラクタ' in message.content:
            with open('garakuta.txt') as garakuta:
                kasi_garakuta = garakuta.read()
            await message.channel.send(kasi_garakuta)
        if '五千光年の夢' in message.content:
            with open('gosennkounennnoyume.txt') as gosennkounennnoyume:
                kasi_gosennkounennnoyume = gosennkounennnoyume.read()
            await message.channel.send(kasi_gosennkounennnoyume)
        if '群青' in message.content:
            with open('gunzyou.txt') as gunzyou:
                kasi_gunzyou = gunzyou.read()
            await message.channel.send(kasi_gunzyou)
        if 'グラスホッパー' in message.content:
            with open('gurasuhoppa-.txt') as gurasuhoppa:
                kasi_gurasuhoppa = gurasuhoppa.read()
            await message.channel.send(kasi_gurasuhoppa)
        if 'グリーン' in message.content:
            with open('guri-n.txt') as gurin:
                kasi_gurin = gurin.read()
            await message.channel.send(kasi_gurin)
        if 'ハートが帰らない' in message.content:
            with open('ha-togakaeranai.txt') as hatogakaeranai:
                kasi_hatogakaeranai = hatogakaeranai.read()
            await message.channel.send(kasi_hatogakaeranai)
        if '裸のままで' in message.content:
            with open('hadakanomamade.txt') as hadakanomamade:
                kasi_hadakanomamade = hadakanomamade.read()
            await message.channel.send(kasi_hadakanomamade)
        if 'はぐれ狼' in message.content:
            with open('hagureookami') as hagureookami:
                kasi_hagureookami = hagureookami.read()
            await message.channel.send(kasi_hagureookami)
        if 'ハイファイ・ローファイ' in message.content:
            with open('haifairo-fai.txt') as haifairofai:
                kasi_haifairofai = haifairofai.read()
            await message.channel.send(kasi_haifairofai)
        if '花泥棒' in message.content:
            with open('hanadorobou.txt') as hanadorobou:
                kasi_hanadorobou = hanadorobou.read()
            await message.channel.send(kasi_hanadorobou)
        if '花の写真' in message.content:
            with open('hananosyasin.txt') as hananosyasin:
                kasi_hananosyasin = hananosyasin.read()
            await message.channel.send(kasi_hananosyasin)
        if '花と虫' in message.content:
            with open('hanatomusi.txt') as hanatomusi:
                kasi_hanatomusi = hanatomusi.read()
            await message.channel.send(kasi_hanatomusi)
        if 'ハネモノ' in message.content:
            with open('hanemono.txt') as hanemono:
                kasi_hanemono = hanemono.txt
            await message.channel.send(kasi_hanemono)
        if 'ハニーハニー' in message.content:
            with open('hani-hani-.txt') as hanihani:
                kasi_hanihani = hanihani.read()
            await message.channel.send(kasi_hanihani)
        if '遥か' in message.content:
            with open('haruka.txt') as haruka:
                kasi_haruka = haruka.read()
            await message.channel.send(kasi_haruka)
        if '春夏ロケット' in message.content:
            with open('harunaturoketto.txt') as harunaturoketto:
                kasi_harunaturoketto = harunaturoketto.read()
            await message.channel.send(kasi_harunaturoketto)
        if '春の歌' in message.content:
            with open('harunouta.txt') as harunouta:
                kasi_harunouta = harunouta.read()
            await message.channel.send(kasi_harunouta)
        if 'ハチミツ' in message.content:
            with open('hatimitu.txt') as hatimitu:
                kasi_hatimitu = hatimitu.read()
            await message.channel.send(kasi_hatimitu)
        if 'ハチの針' in message.content:
            with open('hatinohari.txt') as hatinohari:
                kasi_hatinohari = hatinohari.read()
            await message.channel.send(kasi_hatinohari)
        if '初恋クレイジー' in message.content:
            with open('hatukoikureizi-.txt') as hatukoikureizi:
                kasi_hatukoikureizi = hatukoikureizi.read()
            await message.channel.send(kasi_hatukoikureizi)
        if '初恋に捧ぐ' in message.content:
            with open('hatukoinisasagu.txt') as hatukoinisasagu:
                kasi_hatukoinisasagu = hatukoinisasagu.read()
            await message.channel.send(kasi_hatukoinisasagu)
        if 'ハヤテ' in message.content:
            with open('hayate.txt') as hayate:
                kasi_hayate = hayate.read()
            await message.channel.send(kasi_hayate)
        if 'ヘビーメロウ' in message.content:
            with open('hebi-merou.txt') as hebimerou:
                kasi_hebimerou = hebimerou.read()
            await message.channel.send(kasi_hebimerou)
        if 'ヘチマの花' in message.content:
            with open('hetimanohana.txt') as hetimanohana:
                kasi_hetimanohana = hetimanohana.read()
            await message.channel.send(kasi_hetimanohana)
        if 'ヒバリのこっころ' in message.content:
            with open('hibarinokokoro.txt') as hibarinokokoro:
                kasi_hibarinokokoro = hibarinkokoro.read()
            await message.channel.send(kasi_hibarinokokoro)
        if 'ヒビスクス' in message.content:
            with open('hibisukusu.txt') as hibisukusu:
                kasi_hibisukusu = hibisukusu.read()
            await message.channel.send(kasi_hiisukusu)
        if 'hinatanomadoniakogarete' in message.content:
            with open('hinatanomadoniakogarete.txt') as hinatanomadoniakogarete:
                kasi_hinatanomadoniakogarete = hinatanomadoniakogarete.read()
            await message.channel.send(kasi_hinatanomadoniakogarete)
        if 'HOLIDAY' in message.content or 'holiday' in message.content:
            with open('holiday.txt') as holiday:
                kasi_holiday = holiday.read()
            await message.channel.send(kasi_holiday)
        if 'ほのほ' in message.content:
            with open('honoho.txt') as honoho:
                kasi_honoho = honoho.read()
            await message.channel.send(kasi_honoho)
        if '惑星のかけら' in message.content:
            with open('hosinokakera') as hosinokakera:
                kasi_hosinokakera = hosinokakera.read()
            await message.channel.send(kasi_hosinokakera)
        if 'ホタル' in message.content:
            with open('hotaru.txt') as hotaru:
                kasi_hotaru = hotaru.read()
            await message.channel.send(kasi_hotaru)
        if 'ほうき星' in message.content:
            with open('houkibosi.txt') as houkibosi:
                kasi_houkibosi = houkibosi.read()
            await message.channel.send(kasi_houkibosi)
        if '放浪カモメはどこまでも' in message.content:
            with open('houroukamomehadokomademo.txt') as houroukamomehadokomademo:
                kasi_houroukamomehadokomademo = houroukamomehadokomademo.read()
            await message.channel.send(kasi_houroukamomehadokomademo)
        if '船乗り' in message.content:
            with open('hunanori.txt') as hunanori:
                kasi_hunanori = hunanori.read()
            await message.channel.send(kasi_hunanori)
        if '不思議' in message.content:
            with open('husigi') as husigi:
                kasi_husigi = husigi.read()
            await message.channel.send(kasi_husigi)
        if '不死身のビーナス' in message.content:
            with open('huziminobi-nasu.txt') as huziminobinasu:
                kasi_huziminobinasu = huziminobinasu.read()
            await message.channel.send(kasi_huziminobinasu)
        if '今' in message.content:
            with open('ima.txt') as ima:
                kasi_ima = ima.read()
            await message.channel.send(kasi_ima)
        if '田舎の生活' in message.content:
            with open('inakanoseikatu.txt') as inakanoseikatu:
                kasi_inakanoseikatu = inakanoseikatu.read()
            await message.channel.send(kasi_inakanoseikatu)
        if 'インディゴ地平線' in message.content:
            with open('indexigotiheisne.txt') as indexigotiheisen:
                kasi_indexigotiheisen = indexigotiheisen.read()
            await message.channel.send(kasi_indexigotiheisen)
        if 'いろは' in message.content:
            with open('iroha.txt') as iroha:
                kasi_iroha = iroha.txt
            await message.channel.send(kasi_iroha)
        if '楓' in message.content:
            with open('kaede') as kaede:
                kasi_kaede = kaede.read()
            await message.channel.send(kasi_kaede)
        if '快速' in message.content:
            with open('kaisoku.txt') as kaisoku:
                kasi_kaisoku = kaisoku.read()
            await message.channel.send(kasi_kaisoku)
        if 'けもの道' in message.content:
            with open('kemonomiti.txt') as kemonomiti:
                kasi_kemonomiti = kemonomiti.read()
            await message.channel.send(kasi_kemonomiti)
        if '聞かせてよ' in message.content:
            with open('kikaseteyo.txt') as kikaseteyo:
                kasi_kikaseteyo = kikaseteyo.read()
            await message.channel.send(kasi_kikaseteyo)
        if '君だけを' in message.content:
            with open('kimidakewo.txt') as kimidakewo:
                kasi_kimidakewo = kimidakewo.read()
            await message.channel.send(kasi_kimidakewo)
        if '君が思い出になる前に' in message.content:
            with open('kimigaomoideninarumaeni.txt') as kimigaomoideninarumaeni:
                kasi_kimigaomoideninarumaeni = kimigaomoideninarumaeni.read()
            await message.channel.send(kasi_kimigaomoideninarumaeni)
        if '君は太陽' in message.content:
            with open('kimihataiyou.txt') as kimihataiyou:
                kasi_kimihataiyou = kimihataiyou.read()
            await message.channel.send(kasi_kimihataiyou)
        if '君と暮らせたら' in message.content:
            with open('kimitokurasetara') as kimitokurasetara:
                kasi_kimitokurasetara = kimitokurasetara.read()
            await message.channel.send(kasi_kimitokurasetara)
        if '子グマ！子グマ！' in message.content:
            with open('kogumakoguma.txt') as kogumakoguma:
                kasi_kogumakoguma = kogumakoguma.read()
            await message.channel.send(kasi_kogumakoguma)
        if '恋は夕暮れ' in message.content:
            with open('koihayuugure.txt') as koihayuugure:
                kasi_koihayuugure = koihayuugure.read()
            await message.channel.send(kasi_koihayuugure)
        if '恋のはじまり' in message.content:
            with open('koinohazimari.txt') as koinohazimari:
                kasi_koinohazimari = koinohazimari.read()
            await message.channel.send(kasi_koinohazimari)
        if '恋のうた' in message.content:
            with open('koinouta.txt') as koinouta:
                kasi_koinouta = koinouta.read()
            await message.channel.send(kasi_koinouta)
        if '恋する凡人' in message.content:
            with open('koisurubonzin.txt') as koisurubonzin:
                kasi_koisurubonzin = koisurubonzin.read()
            await message.channel.send(kasi_koisurubonzin)
        if '心の底から' in message.content:
            with open('kokoronosokokara.txt') as kokoronosokokara:
                kasi_kokoronosokokara = kokoronosokokara.read()
            await message.channel.send(kasi_kokoronosokokara)
        if 'コメット' in message.content:
            with open('kometto.txt') as kometto:
                kasi_kometto = kometto.read()
            await message.channel.send(kasi_kometto)
        if 'こんにちは' in message.content:
            with open('konnitiha.txt') as konnitiha:
                kasi_konnitiha = konnitiha.read()
            await message.channel.send(kasi_konnitiha)
        if 'コスモス' in message.content:
            with open('kosumusu.txt') as kosumosu:
                kasi_kosumosu = kosumosu.read()
            await message.channel.send(kasi_kosumosu)
        if 'クリスピー' in message.content:
            with open('kurisupi-.txt') as kurisupi:
                kasi_kurisupi = kurisupi.read()
            await message.channel.send(kasi_kurisupi)
        if '黒い翼' in message.content:
            with open('kuroitubasa.txt') as kuroitubasa:
                kasi_kuroitubasa = kuroitubasa.read()
            await message.channel.send(kasi_kuroitubasa)

client.run(token)
