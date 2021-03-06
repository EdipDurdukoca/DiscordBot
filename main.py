import discord
from discord.ext import commands
from discord.utils import get
import webserver
from webserver import keep_alive
import os
import asyncio
import json
import random
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from discord_slash import SlashCommand

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=",",
                      intents=intents,
                      case_insensitive=True)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True)


async def get_guild_data():
    with open("guilds.json", "r") as f:
        users = json.load(f)
    return users


async def get_emoji():
    with open("emoji.json", "r") as f:
        emojis = json.load(f)
    return emojis


@client.event
async def on_message(message):
    if message.guild.id == 799630651191197737:
        Akira = 821422824426176522
        Jaegerist = 821422920122499092
        Winchester = 821422982894583808
        Spoi = 822195285983756378
        Srole = discord.utils.get(message.guild.roles, id=Spoi)
        Arole = discord.utils.get(message.guild.roles, id=Akira)
        Jrole = discord.utils.get(message.guild.roles, id=Jaegerist)
        Nrole = discord.utils.get(message.guild.roles, id=Winchester)
        devredisikanal = [
            800616793353093170, 804721991306444836, 805854061910949981,
            810200046968242266, 800725036998721567, 812827209265577985,
            806291899316174859, 806294021956698162, 806316636968583168,
            800732646006849586, 822448842398105621
        ]
        spoikanal = [800470462882643999, 800470498743681025]
        users = await get_guild_data()
        pts = int(1)
				for em in await get_emoji():
					if em in message.content:
						webhook= await message.channel.create_webhook(name="Webhook")
						emoji= emojis[em]["code"]
						res= message.content.replace(em,emoji)
						await message.delete()
						if message.author.nick==None:
												user= message.author.name
										else:
												user= message.author.nick
						await webhook.send(content=res,username=user,avatar_url=message.author.avatar_url)
						await webhook.delete()

        if message.channel.id not in devredisikanal:
            if message.channel.id in spoikanal:
                if Srole not in message.author.roles:
                    await message.delete()
                    embed = discord.Embed(
                        title="!!!Spoiler Uyar??s??!!!",
                        description=
                        "Spoiler kanal??na ho??geldin. Spoiler atarken anime ismini a????kta b??rakacak ??ekilde spoilerin her iki taraf??na '\||' koyarak spoileri gizlemeyi unutmay??n.\n \n ??rnek:\n Yaprak D??k??m?? Spoiler \||Behl??l deliriyor\|| \n D??zg??n kullan??rsan??z mesaj ????yle g??r??necektir: \n Yaprak D??k??m?? Spoiler ||Behl??l Deliriyor||",
                        color=discord.Color.green())
                    embed.set_footer(
                        text=
                        "Kanalda mesaj atabilmek i??in alttaki emojiye tepki at."
                    )
                    emoji = '????'
                    msg = await message.channel.send(embed=embed)
                    await msg.add_reaction(emoji=emoji)

                    def check(reaction, user):
                        return user == message.author

                    try:
                        await client.wait_for('reaction_add',
                                              timeout=30.0,
                                              check=check)
                        await message.author.add_roles(Srole)
                        await msg.delete()
                        await message.channel.send("Art??k spoiler atabilirsin."
                                                   )
                    except:
                        await msg.delete()
            users = await get_guild_data()
            chid = 822027109522210856
            chan = client.get_channel(chid)
            await chan.send(users)
            if Arole in message.author.roles:
                users["Akira"]["points"] += pts
                with open("guilds.json", "w") as f:
                    json.dump(users, f)
                await client.process_commands(message)
            elif Jrole in message.author.roles:
                users["Jaegerist"]["points"] += pts
                with open("guilds.json", "w") as f:
                    json.dump(users, f)
                await client.process_commands(message)
            elif Nrole in message.author.roles:
                users["Winchester"]["points"] += pts
                with open("guilds.json", "w") as f:
                    json.dump(users, f)
                await client.process_commands(message)
            else:
                await client.process_commands(message)
        else:
            await client.process_commands(message)


@client.command()
@commands.is_owner()
async def test(ctx):
    await ctx.send("Bot ??al??????yor.")


@client.command()
async def eskigp(ctx):
    if ctx.channel.id == 807241767338246166:
        users = await get_guild_data()
        total = []
        sira = sorted(users, key=lambda s: users[s]['points'], reverse=True)
        total = sorted(total, reverse=True)
        embed = discord.Embed(title=":trophy: `Guild Points` :trophy:",
                              color=discord.Color(0xfa43ee))
        index = 0
        for item in sira:
            if item == "Akira":
                emoji = "<a:bongocat:815992301960036403>"
            if item == "Jaegerist":
                emoji = "<a:ah:812052285646962758>"
            if item == "Winchester":
                emoji = "<a:PeaceNeverOption:815993503573737535>"
            index += 1
            embed.add_field(name="``" + str(index) + "." + "``" + item + emoji,
                            value="``" + str(users[item]["points"]) + "``",
                            inline=False)
        await ctx.send(embed=embed)


@client.command()
async def lonca(ctx, lon=None):
    if ctx.channel.id == 807241767338246166:
        ja = []
        ak = []
        ne = []
        Akira = 821422824426176522
        Jaegerist = 821422920122499092
        Winchester = 821422982894583808
        Arole = discord.utils.get(ctx.guild.roles, id=Akira)
        Jrole = discord.utils.get(ctx.guild.roles, id=Jaegerist)
        Nrole = discord.utils.get(ctx.guild.roles, id=Winchester)
        for member in ctx.guild.members:
            if Arole in member.roles:
                ak.append(member.name)
            if Jrole in member.roles:
                ja.append(member.name)
            if Nrole in member.roles:
                ne.append(member.name)
        if lon == None:
            embed = discord.Embed(title="Loncalar ve ??ye say??lar??:", )
            embed.add_field(name="1)Akira", value=len(ak))
            embed.add_field(name="2)Jaegerist", value=len(ja))
            embed.add_field(name="3)Winchester", value=len(ne))
            embed.set_footer(text="S??ralama puanlara g??re de??ildir.")
            await ctx.send(embed=embed)
        if lon == "1":
            embed = discord.Embed(title="Akira loncas??ndaki ??yeler:",
                                  description=str(ak))
            await ctx.send(embed=embed)
        if lon == "2":
            embed = discord.Embed(title="Jaegerist loncas??ndaki ??yeler:",
                                  description=str(ja))
            await ctx.send(embed=embed)
        if lon == "3":
            embed = discord.Embed(title="Winchester loncas??ndaki ??yeler:",
                                  description=str(ne))
            await ctx.send(embed=embed)


@client.command()
async def rgb(ctx):
    kullananlar = [
        484669487698804747, 526098480389816353, 355339428996055043,
        518462266689978380
    ]
    if ctx.author.id in kullananlar:
        await ctx.message.delete()
        rolid = 820716505343197206
        role = discord.utils.get(ctx.guild.roles, id=rolid)
        a = 1
        while a < 10:
            await role.edit(color=discord.Color.from_rgb(255, 244, 58))
            asyncio.sleep(3)
            await role.edit(color=discord.Color.from_rgb(80, 0, 0))
            asyncio.sleep(3)
            a += 1
        print("Test ba??ar??l??")


@client.command()
async def aryarenk(ctx):
    kullananlar = [484669487698804747, 518462266689978380]
    if ctx.author.id in kullananlar:
        await ctx.message.delete()
        rolid = 807298301471752202
        role = discord.utils.get(ctx.guild.roles, id=rolid)
        a = 1
        while a < 10:
            await role.edit(color=discord.Color.from_rgb(150, 50, 50))
            asyncio.sleep(4)
            await role.edit(color=discord.Color.from_rgb(255, 244, 58))
            asyncio.sleep(4)
            a += 1
        print("Test ba??ar??l??")


@client.command()
async def selam(ctx):
    await ctx.send("Selam ben BMO")


@client.command()
async def hatirlat(ctx):
    role_id = 814596639594512425
    role = discord.utils.get(ctx.guild.roles, id=role_id)
    for member in ctx.guild.members:
        if role in member.roles:
            embed = discord.Embed(
                title="Uyar??",
                description=
                "Merhaba ??????????????? sunucusuna kat??l??p uzun s??redir kendini onaylatmad??????n?? fark ettik.  E??er onaylama ile ilgili bir sorun ya????yorsan moderat??rlerden birine mesaj atabilirsin.",
                color=discord.Color.purple())
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await member.send(embed=embed)
    await ctx.send("Hat??rlatma mesajlar?? g??nderildi.")


@client.command()
async def testingcommand1(ctx):
    embed = discord.Embed(
        title="Uyar??",
        description=
        "Merhaba ??????????????? sunucusuna kat??l??p uzun s??redir kendini onaylatmad??????n?? fark ettik.  E??er onaylama ile ilgili bir sorun ya????yorsan moderat??rlerden birine mesaj atabilirsin.",
        color=discord.Color.purple())
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.author.send(embed=embed)


@client.command()
async def topic(ctx):
    sorular = [
        "Stresten kurtulmak i??in ne yap??yorsunuz?",
        "Tak??nt??l?? oldu??unuz bir ??ey nedir?",
        "Sizi en iyi hangi ???? kelime tan??mlar?",
        "En sevdi??iniz numara nedir? Neden?", "Bu hafta sonu ne yapacaks??n??z?",
        "Sahip oldu??unuz en yararl?? ??ey nedir?",
        "Evcil hayvan??n??z var m??? Onlar??n isimleri ne?",
        "??imdi sizi rahats??z eden pop??ler bir ??ey nedir?",
        "En son ne zaman inan??lmaz s??k?? ??al????t??n??z?",
        "Arkada??lar??n??zla tak??ld??????n??zda genellikle ne yapars??n??z?",
        "En eski arkada????n kim? Onlarla nerede tan????t??n??z?",
        "Giri?? m??zi??iniz olsayd??, hangi ??ark?? olurdu? Neden?",
        "??ocukken ger??ekten neyin pe??indeydiniz?",
        "Evcil hayvan olarak herhangi bir hayvana sahip olsayd??n??z, hangi hayvan?? se??erdiniz?",
        "Bir i??letme a??arsan??z, bu nas??l bir i??letme olurdu?",
        "En sevdi??iniz ??ovmen kim (komedyen, m??zisyen, akt??r, vb.)?",
        "??ok organize bir insan m??s??n??z?",
        "Hi?? b??y??k bir grup insan??n ??n??nde sunum yapt??n??z m??? Nas??l gitti?",
        "??imdiye kadar g??rd??????n??z en garip r??ya nedir?",
        "Hayat??nda kim sana en b??y??k sevinci getiriyor?",
        "Oldu??unuz ki??i ??zerinde en b??y??k etkisi kim oldu?",
        "Birinin sahip olabilece??i en sinir bozucu al????kanl??k nedir?",
        "Bulundu??unuz en g??zel yer neresi?",
        "Serbest zaman??n??z??n / g??n??n ??o??unu nerede ge??iriyorsunuz?",
        "Hangisi daha ??nemli, harika bir arabaya veya harika bir eve sahip olmak? Neden?",
        "??nsanlar??n hangi hayvan veya b??cekleri yok etmesini istersiniz?",
        "Gitti??iniz her yere yan??n??zda ne getiriyorsunuz?",
        "Ad??n??z?? de??i??tirmek zorunda olsayd??n??z, yeni ad??n??z ne olurdu?",
        "Sizi ger??ekten rahats??z eden ama ??o??u insan?? rahats??z etmeyen bir ??ey nedir?",
        "Ge??mi??ten hangi kelimeyi veya s??ylemeyi geri alman??z gerekti??ini d??????n??yorsunuz?",
        "Ba??ar?? nas??l ??l????lmelidir? Ve bu ??l????mle tan??d??????n??z en ba??ar??l?? ki??i kim?",
        "Hayat??n??zda a????klamaya meydan okuyan bir olay oldu mu?",
        "Gelece??inizle ilgili bir sorunun cevab??n?? ????renebilseydiniz, soru ne olurdu?",
        "??lmeden ??nce ba??armak istedi??iniz baz?? ??eyler nelerdir?",
        "Ne tuhaf ya da i??e yaramaz yetene??in var?",
        "G??rd??????n??z en komik TV dizisi nedir?",
        "Hayat??n??z??n hangi TV ??ovuna benzemesini istiyorsunuz?",
        "Sence en ??ok abart??lan film hangisi?",
        "Hangisini tercih edersiniz? Kitap m?? film mi?",
        "Belgeselleri sever misiniz? Neden / neden olmas??n?",
        "Son zamanlarda izledi??iniz en k??t?? film hangisi?",
        "En son izledi??iniz film neydi? Nas??ld???",
        "Filmler d??nyay?? de??i??tirmek i??in kitaplarla ayn?? g??ce sahip mi?",
        "Sinema m?? evde izlemek mi?", "En son hangi kitab?? okudunuz?",
        "??ocukken en sevdi??iniz kitap neydi?",
        "Fiziksel kitaplar?? veya e-kitaplar?? m?? tercih ediyorsunuz?",
        "Okudu??unuz en uzun kitap nedir?",
        "Hangi kitap t??rlerini okumay?? seviyorsunuz?",
        "Sizi en ??ok hangi kitap etkiledi?",
        "Kurgu ya da kurgu olmayan kitaplar?? m?? tercih ediyorsunuz?",
        "En son dinledi??iniz ??ark?? neydi",
        "En sevdi??iniz film m??zi??i hangisidir?",
        "Hangi ??ark?? sizi her zaman iyi bir ruh haline sokar?",
        "Yeni m??zik ke??fetmenin en iyi yolu nedir?",
        "Her dinledi??inizde g??z??n??z?? ya??artan bir ??ark?? var m???",
        "Pop??ler m??zi??i veya nispeten bilinmeyen m??zi??i hangisini tercih edersiniz?",
        "Telefonunuzdaki en iyi ???? uygulama hangileri?",
        "Uygulama ??reticileri sizi rahats??z eden ne yap??yor?",
        "Telefonunuzu ne s??kl??kla kontrol ediyorsunuz?",
        " Daha fazla mesaj at??yor musunuz veya daha fazlas??n?? m?? ar??yorsunuz? Neden?",
        "10 y??l i??inde telefonlar nas??l olacak?",
        "Telefonunuzu yanl????l??kla evde b??rak??rsan??z ne hissedersiniz?",
        "Fantom titre??imi ya????yor musunuz? (Telefonunuzun, olmasa bile titre??ti??ini hissetmek.)",
        "Hangi sporlar?? izlemeyi seviyorsunuz?",
        "Sporcular ald??klar?? y??ksek maa??lar?? hak ediyorlar m??? Neden ya da neden olmas??n?",
        "??zlemek i??in en heyecan verici spor hangisidir? ??zlemek i??in en s??k??c?? olan hangisi?",
        "En k??t?? fast food restoran?? hangisi?",
        "Bir restoran a??arsan??z ne t??r yiyecekler servis ederdiniz?",
        "Duydu??unuz en garip temal?? restoran nedir?",
        "Nereye seyahat etmek isterdin?",
        "Seyahat etmenin en iyi yolu nedir? (U??ak, araba, tren vb.)",
        "Yaln??z m?? yoksa bir grupla m?? seyahat etmeyi tercih edersiniz?",
        "Farkl?? ??lkelere seyahat ettiniz mi? Hangileri?",
        "Sahip oldu??unuz en sevdi??iniz teknoloji hangisidir?",
        "Hangi teknolojiyi kullanmak ger??ekten sinir bozucu?",
        "Son 50 y??l??n en iyi icad?? neydi?",
        "Teknoloji hayat?? kolayla??t??r??yor mu yoksa daha karma????k hale mi getiriyor?",
        "Teknoloji insan ??rk??n?? kurtaracak m?? yoksa yok mu edecek?",
        "Sizce bir sonraki b??y??k teknolojik geli??me ne olacak?",
        "Gelecek 5 y??l i??inde teknoloji hangi sorunlar?? ????zecek? Hangi sorunlar?? yaratacak?",
        "Orta??a?? Avrupas?????ndaki insanlar i??in hangi teknoloji b??y?? veya mucize gibi g??r??n??r?",
        "D??nyay?? daha da k??t??le??tiren herhangi bir teknolojiyi d??????nebilir misiniz?",
        "Moda topluma herhangi bir ??ekilde yard??mc?? oluyor mu?",
        "Giysiler, kar???? cinsin bir insan?? nas??l g??rd??????n?? nas??l de??i??tirir?",
        "??nsanlar??n senin hakk??nda ne d??????nd??????n?? umursam??yorsan, hangi k??yafetleri giyerdin?",
        "Hangi ki??isel hedefleriniz var?",
        "??n??m??zdeki iki y??l i??in hedefleriniz neler?",
        "Profesyonel ya??am??n??zda neyi ba??armay?? umuyorsunuz?",
        "Ailen hedeflerini etkiliyor mu?",
        "Zihniniz bir ada olsayd??, nas??l olurdu?",
        "Ne t??r bir dondurma ??e??idi olmas??n?? istersiniz?",
        "Ki??isel bir maskotunuz olsayd??, maskotunuz ne olurdu?",
        "E??er bir kral / krali??e olsayd??n??z, taht??n??z nas??l olurdu?",
        "Bir g??nl??????ne senden ba??ka herkes i??in zaman donuyor. Ne yapars??n?",
        "Hayat??ndan bir g??n??n?? sonsuza dek yeniden ya??aman gerekseydi hangi g??n?? se??erdin?",
        "D??nyadaki herhangi birini arayabilir ve bir saatlik bir g??r????me yapabilseydiniz, kimi arard??n??z?",
        "Ba??ka bir d??nyaya a????lan portal ??n??nde a????l??yor. Ne kadar s??re a????k kalaca????n?? veya ge??tikten sonra geri d??n??p d??nemeyece??ini bilmiyorsun. Ne yapard??n?",
        "Yar??n ??lece??ini ????renseydin bug??n ne yapard??n?",
        "Para mutluluk getirmiyorsa, para olmadan ger??ekten mutlu olabilir misin?",
        "Olumlu bir g??r??n??m herhangi bir durumu daha iyi hale getirebilir mi?",
        "Geri d??n??p bir ??ans?? de??erlendirmek isteseydin bu hangi f??rsat olurdu?",
        "Sana en yak??n insanlar seni nas??l tan??mlarlar?",
        "Sadece be?? ??eye sahip olma ??ans??n olsayd?? bunlar ne olurdu? Ve neden bunlar?? se??erdin?",
        "???? d??nyanda kendini ka?? ya????nda hissediyorsun?",
        "Hi?? vazge??menin daha do??ru oldu??unu d??????nd??????n bir zaman oldu mu?",
        "Hayat??n yar??n sonlanacak olsa insanlar seni nas??l hat??rlard???",
        "Hayat??n??n bir g??n??n?? tekrar ya??ama ??ans??n olsayd?? hangi g??n?? se??erdin?",
        "??zg??rl?????? kendi s??zc??klerinle tan??mlayabilir misin?",
        "Huzur bulmak istedi??inde nereye gidersin?",
        "Ailenden ????rendi??in en de??erli hayat dersi nedir?",
        "Ba??ar??y?? d??????nd??????nde akl??na gelen ilk ??ey nedir?",
        "Ya??lanman??n en iyi ve en k??t?? yan?? nedir?",
        "Ne i??in ??lene kadar sava??mak istersin?",
        "??lkenle ilgili ???? ??ey de??i??tirme ??ans??n olsayd?? neleri de??i??tirirdin?",
        "Herhangi bir yerde ya??ayacak olsayd??n bu neresi olurdu?",
        "G??n??m??z d??nyas??n??n en b??y??k dezavantaj?? nedir?",
        "Toplumu d??????nd??????nde en ??ok neyi de??i??tirmek isterdin?",
        "Nefret edilmek mi yoksa unutulmak m?? istersin?",
        "D??nyan??n daha iyi bir yer olmas?? i??in yapmak istedi??in en k??????k de??i??iklik nedir?",
        "Sence insanl??????n ula??mak i??in yeterince odaklanmad?????? hedefi nedir?",
        "Tam olarak hayattaki hangi ??eyin daha modernize edilmesi gerekir?",
        "Herhangi bir ??eyde en iyi mi olmak isterdin yoksa her ??eyden biraz anlamak m???",
        "Karmaya inan??r m??s??n? Neden?",
        "Se??imlerinin hayatta ??ok ??nemli bir yere sahip oldu??unu d??????n??yor musun?",
        "Bug??n ??lkende ge??irece??in son g??n olsayd?? tam olarak ne yapard??n?",
        "??nsan ??rk??n??n yok olmas??na en ??ok neden olacak ??ey sence nedir?",
        "Bir ??eyde ba??ar??s??z olmak m?? yoksa onu hi?? denememi?? olmak m?? daha ??nemlidir?",
        "Kendin hakk??nda de??i??tirmek isteyece??in ??ey nedir?",
        "Onsuz ya??ayamam dedi??in ???? ??ey nedir?",
        "Seni an??nda mutlu edebilecek ???? ??ey nedir?",
        "An?? ya??ayan biri misin yoksa s??rekli gelece??i planlar m??s??n?",
        "En ??ok neyi veya kimi kaybetmekten korkuyorsun?",
        "Bir arkada??l??kta en ??ok neye de??er verirsin?",
        "Piyangodan b??y??k ikramiye ????ksa hala ??al????maya devam eder miydin?",
        "T??m ya??am k??s??tlamalar?? ortadan kalksayd?? her g??n ne yapmak isterdin?",
        "Ba??ka bir gezegene mi yoksa okyanusun dibine mi seyahat etmek isterdin?",
        "5 ya????ndaki sene tam olarak hangi tavsiyeyi verirdin?",
        "Hangi icad??n hi?? bulunmam???? olmas??n?? isterdin?",
        "Bug??ne kadar en ??ok dikkatini ??eken komplo teorisi ne oldu?",
        "Mutlu ve huzurlu olup hi?? bir ??ey ba??armam???? olmay?? m?? yoksa memnun olmay??p ??ok ??ey ba??arm???? olmay?? m?? se??ersin?",
        "Yard??m istemek mi yoksa her ??eyi kendin mi halletmek istersin?",
        "E??er bir hayvan??n v??cudunda reenkarne olsayd??n??z, bu hangi hayvan olurdu?",
        "Bir gezegeni ziyaret etme ??ans??n olsayd?? hangisine giderdin?",
        "D??nyan??n 7 Harikas??ndan hangisi ilginizi en ??ok ??ekiyor?",
        "??zlerken sesli g??ld??????n son film hangisiydi?",
        "??zlerken a??lad??????n son film hangisiydi?",
        "??ocuklu??unuzla en ??ok hangi ??ark??y?? ili??kilendiriyorsunuz?",
        "Do??du??un y??l hangi b??y??k tarihsel olay ger??ekle??ti?",
        "Uzayl??lara inan??yor musunuz?", "Hi?? paranormal bir an??n??z var m???",
        "Yar??n piyangoyu kazan??rsan ald??????n ilk ??ey ne olur?",
        "En pi??man oldu??unuz karar??n??z hangisi?",
        "D??nyadaki herhangi bir hayvan?? evcille??tirebilirseniz, hangisini se??ersiniz?",
        "Hangi durumlarda su?? i??lemeyi uygun g??r??rs??n?",
        "??rrasyonel bir fobin var m??, e??er varsa nedir?",
        "??nsanlar d??????nda zeki bir varl??kla ileti??ime ge??ebilseydin onlara insan ??rk??n?? nas??l anlat??rd??n?",
        "Hi?? kurgusal bir karaktere a????k oldun mu, e??er olduysan, kim?",
        "E??er D??nyadaki herhangi birine bir soru sorabilseydiniz ve o da do??ru cevap vermek zorunda olsayd??, kime ne sorard??n??z?",
        "70 y??ll??k huzurlu ama s??k??c?? bir hayat??n m?? olsun isterdin yoksa 35 y??ll??k heyecan dolu bir hayat m???",
        "??nceliklerin zaman i??inde nas??l de??i??ti?",
        "??deal ya??am tarz??n nedir?",
        "A????r?? zengin olmay?? m?? yoksa derinden a????k olmay?? m?? tercih edersiniz?",
        "??l??m??n??n tarihini ve ??eklini ????renme ??ans??n olsayd??,????renmek ister miydin?",
        "Zeka m?? daha ??nemlidir bilgelik mi?", "??dol??n kim?",
        "Okulda ????retilmesi gerekti??i halde ????retilmeyen ??eyler nelerdir?",
        "Bug??n ya??ayan en g????l?? ki??i kim ve neden?",
        "Akl??n??za gelebilecek en rahats??z edici ger??ek nedir?",
        "Bir ki??inin yapabilece??i en duyars??zca davran???? nedir?",
        "Obsesif kompulsif oldu??un herhangi bir ??ey var m???",
        "Yasalar olmadan bir toplum var olabilir mi?",
        "Bir sava?? adil olabilir mi?",
        "Sa??l??kl?? bir toplumda ifade ??zg??rl?????? ne kadar ??nemlidir?",
        "Hayvanlar ak??l y??r??tebilir mi?",
        "??nsanlar d??nyaya daha ne kadar hakim olacak?",
        "A??k sadece bir duygu mu?",
        "Ba??ar??s??z olmak m?? yoksa hi?? denememek mi daha k??t???",
        "Gerekli bir k??t??l??k ya da beyaz bir yalan diye bir ??ey var m??d??r?",
        "Sevip kaybetmek mi yoksa hi?? sevmemek mi daha iyidir?",
        "R??yalar??n anlamlar?? var m???",
        "Hangisi daha ger??ek - ak??l m?? yoksa madde mi?",
        "??nsanlar??n temelde k??t?? m?? yoksa temelde iyi oldu??unu mu d??????n??yorsunuz?",
        "Ya??amak ve var olmak aras??ndaki fark nedir?",
        "??u anda r??ya g??rmedi??ini nas??l anlars??n? Peki ??u an r??ya g??rmedi??inden emin misin?",
        "Paralel bir evrenin var oldu??unu d??????n??yor musun?",
        "E??er t??m molek??lleriniz par??alan??rsa, D??nyan??n di??er taraf??na ??????nlan??r ve yeniden yap??land??r??l??rsa, ??ld??r??l??p yeniden yarat??lm???? m?? olurdunuz, bir klon mu olurdunuz yoksa hala ayn?? ki??i mi olurdunuz?",
        "Zaman bir insan yap??s?? m?? yoksa bir do??a kural?? m???",
        "??nsanlar neyin yanl???? gitti??inden ??ok neyin iyi gitti??ine odaklan??rsa i??ler daha iyi mi yoksa daha m?? k??t?? olur?",
        "Felsefe cevap m?? bulur yoksa daha ??ok soruya m?? yol a??ar?",
        "Ac??dan ka????nmaya ve zevk aramaya odaklanan bir ya??am, iyi ve de??erli bir ya??am m??d??r? Neden ya da neden olmas??n?",
        "K??skan??l??k insanlar?? kendilerini geli??tirmeye iter mi yoksa tamamen zararl?? bir duygu mudur?",
        "Cahil olup mutlu olmak m?? bilge olup mutsuz olmak m???",
        "Sosyal medya daha ??ok yararl?? m?? yoksa zararl?? m???",
        "??tenazi(Bir insan??n kendi iste??i ile hayat??na son verdirmesi) sizce etik midir?",
        "M??mk??nse ??l??ms??z olmak ister miydiniz?",
        "??zgecilik(Di??er insanlar??n mutluluk ve huzuruna kendi mutluluk ve huzurundan daha ??ok ??nem vermek) hakk??nda ne d??????n??yorsunuz?",
        "Bir hayvan??n hayat?? bir insan??n hayat?? kadar de??erli olabilir mi?",
        "Evrensel bir g??zellik tan??m?? olabilir mi?",
        "Nesnellik var m??, yoksa her ??ey ??znel mi?",
        "Mutlulu??un tarifi nedir?",
        "K??resel ??s??nmay?? zaman??nda durdurabilecek miyiz?",
        "Herkes ayn?? fikre sahip olsayd?? d??nya nas??l olurdu?",
        "Daha kat?? yasalar daha bar????????l bir d??nyaya m?? yoksa daha fazla su??a m?? yol a??ar?",
        "D??nyaya nas??l bir iz b??rakmak istiyorsunuz?",
        "Hedefiniz ger??ekten eri??ilemez konumda m??, yoksa siz ona ula??mak i??in yeterince ??aba harcam??yor musunuz?",
        "E??er hayat ??ok k??saysa neden sevmedi??imiz bir s??r?? ??eyi yap??yoruz ve neden yapmad??????m??z bir s??r?? ??eyi seviyoruz?",
        "B??rakmak ya da devam etmek i??in do??ru zaman oldu??unu nas??l anl??yorsunuz?",
        "E??er mutluluk para olsayd??, mesle??iniz ne olurdu?",
        "??htiyac??n??z olmayan, ancak sahip oldu??unuz i??in ger??ekten mutlu oldu??un baz?? ??eyler nelerdir?",
        "Hangi duygu daha k??t??d??r? Utan??,??fke,??z??nt???"
    ]
    a = random.choice(sorular)
    embed = discord.Embed(title=f"{ctx.author.name} konu ba??latt??:",
                          description=a,
                          color=discord.Color.blue())
    await ctx.send(embed=embed)


@client.command()
@commands.has_role("Moderat??r")
async def kick(ctx, kullanici: discord.Member, *, sebep=None):
    await kullanici.kick(reason=sebep)
    if sebep == None:
        sebep = "Herhangi bir sebep belirtilmedi."
    await ctx.send(f"{kullanici} sunucudan at??ld??.")
    log = client.get_channel(810127270458163210)
    logembed = discord.Embed(
        title=f"{kullanici} sunucudan at??ld??.",
        description=f"{sebep}",
    )
    logembed.set_footer(text=f"Moderat??r:{ctx.author}")
    await log.send(embed=logembed)


@client.command()
@commands.has_role("Moderat??r")
async def ban(ctx, kullanici: discord.Member, *, sebep=None):
    await kullanici.ban(reason=sebep)
    if sebep == None:
        sebep = "Herhangi bir sebep belirtilmedi."
    await ctx.send(f"{kullanici} sunucudan banland??.")
    log = client.get_channel(810127270458163210)
    logembed = discord.Embed(
        title=f"{kullanici} sunucudan banland??.",
        description=f"{sebep}",
    )
    logembed.set_footer(text=f"Moderat??r:{ctx.author}")
    await log.send(embed=logembed)


def convert(time):
    pos = ["s", "m", "h", "d"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}
    unit = time[-1]
    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2
    return val * time_dict[unit]


@client.command()
@commands.has_role("Moderat??r")
async def mute(ctx, user: discord.Member = None, time=None, *, reason=None):
    if user == None:
        await ctx.send("Komutun kullan??m?? ????yledir: ',mute @kullan??c?? <s??re>.")
    elif time == None:
        await ctx.send("S??resini de ben mi belirleyeyim? \:D")
    else:
        logchannel = client.get_channel(810127270458163210)
        role_id = 799702960488710195
        muterole = discord.utils.get(ctx.guild.roles, id=role_id)
        await user.add_roles(muterole)
        await ctx.send(f"{user.name} susturuldu.")
        mutedtime = convert(time)
        muted = discord.Embed(title=f"{user} {time} kadar susturuldu.",
                              color=discord.Color.red())
        if reason != None:
            muted.add_field(name="Susturulma sebebi:", value=reason)
        await logchannel.send(embed=muted)
        await asyncio.sleep(mutedtime)
        if muterole in user.roles:
            await user.remove_roles(muterole)
            muteremoved = discord.Embed(
                title=f"{user}'in susturulma s??resi doldu.",
                color=discord.Color.green())
            await logchannel.send(embed=muteremoved)
            await ctx.send(f"{user.mention} art??k konu??abilir.")


@client.command(aliases=['sk'])
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, user: discord.Member):
    role_id = 799702960488710195
    muterole = discord.utils.get(ctx.guild.roles, id=role_id)
    logchannel = client.get_channel(810127270458163210)
    if muterole in user.roles:
        await user.remove_roles(muterole)
        muteremoved = discord.Embed(
            title=f"{user}'in susturulmas?? {ctx.author} taraf??ndan kald??r??ld??.",
            color=discord.Color.green())
        await logchannel.send(embed=muteremoved)
        await ctx.send(f"{user.mention} art??k konu??abilir.")
    else:
        await ctx.send("Bu kullan??c?? zaten susturulmam????.")


@client.command()
async def pillowtest(ctx, *, agh):
    asset = ctx.author.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    font = ImageFont.truetype("arial.ttf", 24)
    draw = ImageDraw.Draw(pfp)
    text = agh
    draw.text((0, 30), text, (0, 0, 0), font=font)
    pfp.save("text.png")
    await ctx.send(file=discord.File("text.png"))


@client.command()
async def icon(ctx):
    await ctx.send(ctx.guild.icon_url)


@client.command()
async def gp(ctx):
    if ctx.channel.id == 807241767338246166:
        users = await get_guild_data()
        sira = sorted(users, key=lambda s: users[s]['points'], reverse=True)
        birisim = sira[0]
        ikiisim = sira[1]
        ucisim = sira[2]
        birpuan = users[sira[0]]["points"]
        ikipuan = users[sira[1]]["points"]
        ucpuan = users[sira[2]]["points"]
        foto = Image.open("Foto.jpg")
        font = ImageFont.truetype("FONT.ttf", 36)
        draw = ImageDraw.Draw(foto)
        draw.text((160, 376), birisim, (255, 255, 255), font=font)
        draw.text((480, 376), str(birpuan), (255, 255, 255), font=font)
        draw.text((160, 445), ikiisim, (255, 255, 255), font=font)
        draw.text((480, 448), str(ikipuan), (255, 255, 255), font=font)
        draw.text((160, 517), ucisim, (255, 255, 255), font=font)
        draw.text((480, 523), str(ucpuan), (255, 255, 255), font=font)
        foto.save("Sonu??.png")
        await ctx.send(file=discord.File("Sonu??.png"))


@client.command()
async def say(ctx, *, tex):
    await ctx.message.delete()
    await ctx.send(tex)


@client.command()
async def yenigp(ctx):
    users = await get_guild_data()
    img = []
    sira = sorted(users, key=lambda s: users[s]['points'], reverse=True)
    birisim = sira[0]
    ikiisim = sira[1]
    ucisim = sira[2]
    birpuan = users[birisim]["points"]
    ikipuan = users[ikiisim]["points"]
    ucpuan = users[ucisim]["points"]
    foto = Image.open("GIF.gif")
    font = ImageFont.truetype("FONT.ttf", 36)
    draw = ImageDraw.Draw(foto)
    foto.seek(foto.tell() + 1)
    a = foto.tell()
    await ctx.send(a)
    draw.text((134, 306), birisim, (255, 255, 255), font=font)
    draw.text((390, 306), str(birpuan), (255, 255, 255), font=font)
    draw.text((134, 366), ikiisim, (255, 255, 255), font=font)
    draw.text((390, 366), str(ikipuan), (255, 255, 255), font=font)
    draw.text((134, 420), ucisim, (255, 255, 255), font=font)
    draw.text((390, 420), str(ucpuan), (255, 255, 255), font=font)
    for i in range(21):
        fot = foto.seek[i]
        img.append(fot)
    await ctx.send(img)
    foto.save("Sonu??.gif")
    await ctx.send(file=discord.File("Sonu??.gif"))


guild_ids = [799630651191197737]


@slash.slash(name="gecikme", guild_ids=guild_ids)
async def _gecikme(ctx):
    embed = discord.Embed(
        title="Ping",
        description=f"Gecikme hesapland??! ({client.latency*1000:.2f} ms)")
    await ctx.respond()
    await ctx.send(embed=embed)

@slash.slash(name="hype", guild_ids=guild_ids)
async def _hype(ctx):
    embed = discord.Embed(
        title="Ping",
        description=f"Gecikme hesapland??! ({client.latency*1000:.2f} ms)")
    await ctx.respond()
    await ctx.send(embed=embed)


keep_alive()
TOKEN = os.environ.get('DISCORD_BOT_SECRET')
client.run(TOKEN)