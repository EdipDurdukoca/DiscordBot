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
                        title="!!!Spoiler Uyarısı!!!",
                        description=
                        "Spoiler kanalına hoşgeldin. Spoiler atarken anime ismini açıkta bırakacak şekilde spoilerin her iki tarafına '\||' koyarak spoileri gizlemeyi unutmayın.\n \n Örnek:\n Yaprak Dökümü Spoiler \||Behlül deliriyor\|| \n Düzgün kullanırsanız mesaj şöyle görünecektir: \n Yaprak Dökümü Spoiler ||Behlül Deliriyor||",
                        color=discord.Color.green())
                    embed.set_footer(
                        text=
                        "Kanalda mesaj atabilmek için alttaki emojiye tepki at."
                    )
                    emoji = '👍'
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
                        await message.channel.send("Artık spoiler atabilirsin."
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
    await ctx.send("Bot çalışıyor.")


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
            embed = discord.Embed(title="Loncalar ve üye sayıları:", )
            embed.add_field(name="1)Akira", value=len(ak))
            embed.add_field(name="2)Jaegerist", value=len(ja))
            embed.add_field(name="3)Winchester", value=len(ne))
            embed.set_footer(text="Sıralama puanlara göre değildir.")
            await ctx.send(embed=embed)
        if lon == "1":
            embed = discord.Embed(title="Akira loncasındaki üyeler:",
                                  description=str(ak))
            await ctx.send(embed=embed)
        if lon == "2":
            embed = discord.Embed(title="Jaegerist loncasındaki üyeler:",
                                  description=str(ja))
            await ctx.send(embed=embed)
        if lon == "3":
            embed = discord.Embed(title="Winchester loncasındaki üyeler:",
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
        print("Test başarılı")


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
        print("Test başarılı")


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
                title="Uyarı",
                description=
                "Merhaba トランスレ sunucusuna katılıp uzun süredir kendini onaylatmadığını fark ettik.  Eğer onaylama ile ilgili bir sorun yaşıyorsan moderatörlerden birine mesaj atabilirsin.",
                color=discord.Color.purple())
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await member.send(embed=embed)
    await ctx.send("Hatırlatma mesajları gönderildi.")


@client.command()
async def testingcommand1(ctx):
    embed = discord.Embed(
        title="Uyarı",
        description=
        "Merhaba トランスレ sunucusuna katılıp uzun süredir kendini onaylatmadığını fark ettik.  Eğer onaylama ile ilgili bir sorun yaşıyorsan moderatörlerden birine mesaj atabilirsin.",
        color=discord.Color.purple())
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.author.send(embed=embed)


@client.command()
async def topic(ctx):
    sorular = [
        "Stresten kurtulmak için ne yapıyorsunuz?",
        "Takıntılı olduğunuz bir şey nedir?",
        "Sizi en iyi hangi üç kelime tanımlar?",
        "En sevdiğiniz numara nedir? Neden?", "Bu hafta sonu ne yapacaksınız?",
        "Sahip olduğunuz en yararlı şey nedir?",
        "Evcil hayvanınız var mı? Onların isimleri ne?",
        "Şimdi sizi rahatsız eden popüler bir şey nedir?",
        "En son ne zaman inanılmaz sıkı çalıştınız?",
        "Arkadaşlarınızla takıldığınızda genellikle ne yaparsınız?",
        "En eski arkadaşın kim? Onlarla nerede tanıştınız?",
        "Giriş müziğiniz olsaydı, hangi şarkı olurdu? Neden?",
        "Çocukken gerçekten neyin peşindeydiniz?",
        "Evcil hayvan olarak herhangi bir hayvana sahip olsaydınız, hangi hayvanı seçerdiniz?",
        "Bir işletme açarsanız, bu nasıl bir işletme olurdu?",
        "En sevdiğiniz şovmen kim (komedyen, müzisyen, aktör, vb.)?",
        "Çok organize bir insan mısınız?",
        "Hiç büyük bir grup insanın önünde sunum yaptınız mı? Nasıl gitti?",
        "Şimdiye kadar gördüğünüz en garip rüya nedir?",
        "Hayatında kim sana en büyük sevinci getiriyor?",
        "Olduğunuz kişi üzerinde en büyük etkisi kim oldu?",
        "Birinin sahip olabileceği en sinir bozucu alışkanlık nedir?",
        "Bulunduğunuz en güzel yer neresi?",
        "Serbest zamanınızın / günün çoğunu nerede geçiriyorsunuz?",
        "Hangisi daha önemli, harika bir arabaya veya harika bir eve sahip olmak? Neden?",
        "İnsanların hangi hayvan veya böcekleri yok etmesini istersiniz?",
        "Gittiğiniz her yere yanınızda ne getiriyorsunuz?",
        "Adınızı değiştirmek zorunda olsaydınız, yeni adınız ne olurdu?",
        "Sizi gerçekten rahatsız eden ama çoğu insanı rahatsız etmeyen bir şey nedir?",
        "Geçmişten hangi kelimeyi veya söylemeyi geri almanız gerektiğini düşünüyorsunuz?",
        "Başarı nasıl ölçülmelidir? Ve bu ölçümle tanıdığınız en başarılı kişi kim?",
        "Hayatınızda açıklamaya meydan okuyan bir olay oldu mu?",
        "Geleceğinizle ilgili bir sorunun cevabını öğrenebilseydiniz, soru ne olurdu?",
        "Ölmeden önce başarmak istediğiniz bazı şeyler nelerdir?",
        "Ne tuhaf ya da işe yaramaz yeteneğin var?",
        "Gördüğünüz en komik TV dizisi nedir?",
        "Hayatınızın hangi TV şovuna benzemesini istiyorsunuz?",
        "Sence en çok abartılan film hangisi?",
        "Hangisini tercih edersiniz? Kitap mı film mi?",
        "Belgeselleri sever misiniz? Neden / neden olmasın?",
        "Son zamanlarda izlediğiniz en kötü film hangisi?",
        "En son izlediğiniz film neydi? Nasıldı?",
        "Filmler dünyayı değiştirmek için kitaplarla aynı güce sahip mi?",
        "Sinema mı evde izlemek mi?", "En son hangi kitabı okudunuz?",
        "Çocukken en sevdiğiniz kitap neydi?",
        "Fiziksel kitapları veya e-kitapları mı tercih ediyorsunuz?",
        "Okuduğunuz en uzun kitap nedir?",
        "Hangi kitap türlerini okumayı seviyorsunuz?",
        "Sizi en çok hangi kitap etkiledi?",
        "Kurgu ya da kurgu olmayan kitapları mı tercih ediyorsunuz?",
        "En son dinlediğiniz şarkı neydi",
        "En sevdiğiniz film müziği hangisidir?",
        "Hangi şarkı sizi her zaman iyi bir ruh haline sokar?",
        "Yeni müzik keşfetmenin en iyi yolu nedir?",
        "Her dinlediğinizde gözünüzü yaşartan bir şarkı var mı?",
        "Popüler müziği veya nispeten bilinmeyen müziği hangisini tercih edersiniz?",
        "Telefonunuzdaki en iyi üç uygulama hangileri?",
        "Uygulama üreticileri sizi rahatsız eden ne yapıyor?",
        "Telefonunuzu ne sıklıkla kontrol ediyorsunuz?",
        " Daha fazla mesaj atıyor musunuz veya daha fazlasını mı arıyorsunuz? Neden?",
        "10 yıl içinde telefonlar nasıl olacak?",
        "Telefonunuzu yanlışlıkla evde bırakırsanız ne hissedersiniz?",
        "Fantom titreşimi yaşıyor musunuz? (Telefonunuzun, olmasa bile titreştiğini hissetmek.)",
        "Hangi sporları izlemeyi seviyorsunuz?",
        "Sporcular aldıkları yüksek maaşları hak ediyorlar mı? Neden ya da neden olmasın?",
        "İzlemek için en heyecan verici spor hangisidir? İzlemek için en sıkıcı olan hangisi?",
        "En kötü fast food restoranı hangisi?",
        "Bir restoran açarsanız ne tür yiyecekler servis ederdiniz?",
        "Duyduğunuz en garip temalı restoran nedir?",
        "Nereye seyahat etmek isterdin?",
        "Seyahat etmenin en iyi yolu nedir? (Uçak, araba, tren vb.)",
        "Yalnız mı yoksa bir grupla mı seyahat etmeyi tercih edersiniz?",
        "Farklı ülkelere seyahat ettiniz mi? Hangileri?",
        "Sahip olduğunuz en sevdiğiniz teknoloji hangisidir?",
        "Hangi teknolojiyi kullanmak gerçekten sinir bozucu?",
        "Son 50 yılın en iyi icadı neydi?",
        "Teknoloji hayatı kolaylaştırıyor mu yoksa daha karmaşık hale mi getiriyor?",
        "Teknoloji insan ırkını kurtaracak mı yoksa yok mu edecek?",
        "Sizce bir sonraki büyük teknolojik gelişme ne olacak?",
        "Gelecek 5 yıl içinde teknoloji hangi sorunları çözecek? Hangi sorunları yaratacak?",
        "Ortaçağ Avrupası’ndaki insanlar için hangi teknoloji büyü veya mucize gibi görünür?",
        "Dünyayı daha da kötüleştiren herhangi bir teknolojiyi düşünebilir misiniz?",
        "Moda topluma herhangi bir şekilde yardımcı oluyor mu?",
        "Giysiler, karşı cinsin bir insanı nasıl gördüğünü nasıl değiştirir?",
        "İnsanların senin hakkında ne düşündüğünü umursamıyorsan, hangi kıyafetleri giyerdin?",
        "Hangi kişisel hedefleriniz var?",
        "Önümüzdeki iki yıl için hedefleriniz neler?",
        "Profesyonel yaşamınızda neyi başarmayı umuyorsunuz?",
        "Ailen hedeflerini etkiliyor mu?",
        "Zihniniz bir ada olsaydı, nasıl olurdu?",
        "Ne tür bir dondurma çeşidi olmasını istersiniz?",
        "Kişisel bir maskotunuz olsaydı, maskotunuz ne olurdu?",
        "Eğer bir kral / kraliçe olsaydınız, tahtınız nasıl olurdu?",
        "Bir günlüğüne senden başka herkes için zaman donuyor. Ne yaparsın?",
        "Hayatından bir gününü sonsuza dek yeniden yaşaman gerekseydi hangi günü seçerdin?",
        "Dünyadaki herhangi birini arayabilir ve bir saatlik bir görüşme yapabilseydiniz, kimi arardınız?",
        "Başka bir dünyaya açılan portal önünde açılıyor. Ne kadar süre açık kalacağını veya geçtikten sonra geri dönüp dönemeyeceğini bilmiyorsun. Ne yapardın?",
        "Yarın öleceğini öğrenseydin bugün ne yapardın?",
        "Para mutluluk getirmiyorsa, para olmadan gerçekten mutlu olabilir misin?",
        "Olumlu bir görünüm herhangi bir durumu daha iyi hale getirebilir mi?",
        "Geri dönüp bir şansı değerlendirmek isteseydin bu hangi fırsat olurdu?",
        "Sana en yakın insanlar seni nasıl tanımlarlar?",
        "Sadece beş şeye sahip olma şansın olsaydı bunlar ne olurdu? Ve neden bunları seçerdin?",
        "İç dünyanda kendini kaç yaşında hissediyorsun?",
        "Hiç vazgeçmenin daha doğru olduğunu düşündüğün bir zaman oldu mu?",
        "Hayatın yarın sonlanacak olsa insanlar seni nasıl hatırlardı?",
        "Hayatının bir gününü tekrar yaşama şansın olsaydı hangi günü seçerdin?",
        "Özgürlüğü kendi sözcüklerinle tanımlayabilir misin?",
        "Huzur bulmak istediğinde nereye gidersin?",
        "Ailenden öğrendiğin en değerli hayat dersi nedir?",
        "Başarıyı düşündüğünde aklına gelen ilk şey nedir?",
        "Yaşlanmanın en iyi ve en kötü yanı nedir?",
        "Ne için ölene kadar savaşmak istersin?",
        "Ülkenle ilgili üç şey değiştirme şansın olsaydı neleri değiştirirdin?",
        "Herhangi bir yerde yaşayacak olsaydın bu neresi olurdu?",
        "Günümüz dünyasının en büyük dezavantajı nedir?",
        "Toplumu düşündüğünde en çok neyi değiştirmek isterdin?",
        "Nefret edilmek mi yoksa unutulmak mı istersin?",
        "Dünyanın daha iyi bir yer olması için yapmak istediğin en küçük değişiklik nedir?",
        "Sence insanlığın ulaşmak için yeterince odaklanmadığı hedefi nedir?",
        "Tam olarak hayattaki hangi şeyin daha modernize edilmesi gerekir?",
        "Herhangi bir şeyde en iyi mi olmak isterdin yoksa her şeyden biraz anlamak mı?",
        "Karmaya inanır mısın? Neden?",
        "Seçimlerinin hayatta çok önemli bir yere sahip olduğunu düşünüyor musun?",
        "Bugün ülkende geçireceğin son gün olsaydı tam olarak ne yapardın?",
        "İnsan ırkının yok olmasına en çok neden olacak şey sence nedir?",
        "Bir şeyde başarısız olmak mı yoksa onu hiç denememiş olmak mı daha önemlidir?",
        "Kendin hakkında değiştirmek isteyeceğin şey nedir?",
        "Onsuz yaşayamam dediğin üç şey nedir?",
        "Seni anında mutlu edebilecek üç şey nedir?",
        "Anı yaşayan biri misin yoksa sürekli geleceği planlar mısın?",
        "En çok neyi veya kimi kaybetmekten korkuyorsun?",
        "Bir arkadaşlıkta en çok neye değer verirsin?",
        "Piyangodan büyük ikramiye çıksa hala çalışmaya devam eder miydin?",
        "Tüm yaşam kısıtlamaları ortadan kalksaydı her gün ne yapmak isterdin?",
        "Başka bir gezegene mi yoksa okyanusun dibine mi seyahat etmek isterdin?",
        "5 yaşındaki sene tam olarak hangi tavsiyeyi verirdin?",
        "Hangi icadın hiç bulunmamış olmasını isterdin?",
        "Bugüne kadar en çok dikkatini çeken komplo teorisi ne oldu?",
        "Mutlu ve huzurlu olup hiç bir şey başarmamış olmayı mı yoksa memnun olmayıp çok şey başarmış olmayı mı seçersin?",
        "Yardım istemek mi yoksa her şeyi kendin mi halletmek istersin?",
        "Eğer bir hayvanın vücudunda reenkarne olsaydınız, bu hangi hayvan olurdu?",
        "Bir gezegeni ziyaret etme şansın olsaydı hangisine giderdin?",
        "Dünyanın 7 Harikasından hangisi ilginizi en çok çekiyor?",
        "İzlerken sesli güldüğün son film hangisiydi?",
        "İzlerken ağladığın son film hangisiydi?",
        "Çocukluğunuzla en çok hangi şarkıyı ilişkilendiriyorsunuz?",
        "Doğduğun yıl hangi büyük tarihsel olay gerçekleşti?",
        "Uzaylılara inanıyor musunuz?", "Hiç paranormal bir anınız var mı?",
        "Yarın piyangoyu kazanırsan aldığın ilk şey ne olur?",
        "En pişman olduğunuz kararınız hangisi?",
        "Dünyadaki herhangi bir hayvanı evcilleştirebilirseniz, hangisini seçersiniz?",
        "Hangi durumlarda suç işlemeyi uygun görürsün?",
        "İrrasyonel bir fobin var mı, eğer varsa nedir?",
        "İnsanlar dışında zeki bir varlıkla iletişime geçebilseydin onlara insan ırkını nasıl anlatırdın?",
        "Hiç kurgusal bir karaktere aşık oldun mu, eğer olduysan, kim?",
        "Eğer Dünyadaki herhangi birine bir soru sorabilseydiniz ve o da doğru cevap vermek zorunda olsaydı, kime ne sorardınız?",
        "70 yıllık huzurlu ama sıkıcı bir hayatın mı olsun isterdin yoksa 35 yıllık heyecan dolu bir hayat mı?",
        "Önceliklerin zaman içinde nasıl değişti?",
        "İdeal yaşam tarzın nedir?",
        "Aşırı zengin olmayı mı yoksa derinden aşık olmayı mı tercih edersiniz?",
        "Ölümünün tarihini ve şeklini öğrenme şansın olsaydı,öğrenmek ister miydin?",
        "Zeka mı daha önemlidir bilgelik mi?", "İdolün kim?",
        "Okulda öğretilmesi gerektiği halde öğretilmeyen şeyler nelerdir?",
        "Bugün yaşayan en güçlü kişi kim ve neden?",
        "Aklınıza gelebilecek en rahatsız edici gerçek nedir?",
        "Bir kişinin yapabileceği en duyarsızca davranış nedir?",
        "Obsesif kompulsif olduğun herhangi bir şey var mı?",
        "Yasalar olmadan bir toplum var olabilir mi?",
        "Bir savaş adil olabilir mi?",
        "Sağlıklı bir toplumda ifade özgürlüğü ne kadar önemlidir?",
        "Hayvanlar akıl yürütebilir mi?",
        "İnsanlar dünyaya daha ne kadar hakim olacak?",
        "Aşk sadece bir duygu mu?",
        "Başarısız olmak mı yoksa hiç denememek mi daha kötü?",
        "Gerekli bir kötülük ya da beyaz bir yalan diye bir şey var mıdır?",
        "Sevip kaybetmek mi yoksa hiç sevmemek mi daha iyidir?",
        "Rüyaların anlamları var mı?",
        "Hangisi daha gerçek - akıl mı yoksa madde mi?",
        "İnsanların temelde kötü mü yoksa temelde iyi olduğunu mu düşünüyorsunuz?",
        "Yaşamak ve var olmak arasındaki fark nedir?",
        "Şu anda rüya görmediğini nasıl anlarsın? Peki şu an rüya görmediğinden emin misin?",
        "Paralel bir evrenin var olduğunu düşünüyor musun?",
        "Eğer tüm molekülleriniz parçalanırsa, Dünyanın diğer tarafına ışınlanır ve yeniden yapılandırılırsa, öldürülüp yeniden yaratılmış mı olurdunuz, bir klon mu olurdunuz yoksa hala aynı kişi mi olurdunuz?",
        "Zaman bir insan yapısı mı yoksa bir doğa kuralı mı?",
        "İnsanlar neyin yanlış gittiğinden çok neyin iyi gittiğine odaklanırsa işler daha iyi mi yoksa daha mı kötü olur?",
        "Felsefe cevap mı bulur yoksa daha çok soruya mı yol açar?",
        "Acıdan kaçınmaya ve zevk aramaya odaklanan bir yaşam, iyi ve değerli bir yaşam mıdır? Neden ya da neden olmasın?",
        "Kıskançlık insanları kendilerini geliştirmeye iter mi yoksa tamamen zararlı bir duygu mudur?",
        "Cahil olup mutlu olmak mı bilge olup mutsuz olmak mı?",
        "Sosyal medya daha çok yararlı mı yoksa zararlı mı?",
        "Ötenazi(Bir insanın kendi isteği ile hayatına son verdirmesi) sizce etik midir?",
        "Mümkünse ölümsüz olmak ister miydiniz?",
        "Özgecilik(Diğer insanların mutluluk ve huzuruna kendi mutluluk ve huzurundan daha çok önem vermek) hakkında ne düşünüyorsunuz?",
        "Bir hayvanın hayatı bir insanın hayatı kadar değerli olabilir mi?",
        "Evrensel bir güzellik tanımı olabilir mi?",
        "Nesnellik var mı, yoksa her şey öznel mi?",
        "Mutluluğun tarifi nedir?",
        "Küresel ısınmayı zamanında durdurabilecek miyiz?",
        "Herkes aynı fikre sahip olsaydı dünya nasıl olurdu?",
        "Daha katı yasalar daha barışçıl bir dünyaya mı yoksa daha fazla suça mı yol açar?",
        "Dünyaya nasıl bir iz bırakmak istiyorsunuz?",
        "Hedefiniz gerçekten erişilemez konumda mı, yoksa siz ona ulaşmak için yeterince çaba harcamıyor musunuz?",
        "Eğer hayat çok kısaysa neden sevmediğimiz bir sürü şeyi yapıyoruz ve neden yapmadığımız bir sürü şeyi seviyoruz?",
        "Bırakmak ya da devam etmek için doğru zaman olduğunu nasıl anlıyorsunuz?",
        "Eğer mutluluk para olsaydı, mesleğiniz ne olurdu?",
        "İhtiyacınız olmayan, ancak sahip olduğunuz için gerçekten mutlu olduğun bazı şeyler nelerdir?",
        "Hangi duygu daha kötüdür? Utanç,Öfke,Üzüntü?"
    ]
    a = random.choice(sorular)
    embed = discord.Embed(title=f"{ctx.author.name} konu başlattı:",
                          description=a,
                          color=discord.Color.blue())
    await ctx.send(embed=embed)


@client.command()
@commands.has_role("Moderatör")
async def kick(ctx, kullanici: discord.Member, *, sebep=None):
    await kullanici.kick(reason=sebep)
    if sebep == None:
        sebep = "Herhangi bir sebep belirtilmedi."
    await ctx.send(f"{kullanici} sunucudan atıldı.")
    log = client.get_channel(810127270458163210)
    logembed = discord.Embed(
        title=f"{kullanici} sunucudan atıldı.",
        description=f"{sebep}",
    )
    logembed.set_footer(text=f"Moderatör:{ctx.author}")
    await log.send(embed=logembed)


@client.command()
@commands.has_role("Moderatör")
async def ban(ctx, kullanici: discord.Member, *, sebep=None):
    await kullanici.ban(reason=sebep)
    if sebep == None:
        sebep = "Herhangi bir sebep belirtilmedi."
    await ctx.send(f"{kullanici} sunucudan banlandı.")
    log = client.get_channel(810127270458163210)
    logembed = discord.Embed(
        title=f"{kullanici} sunucudan banlandı.",
        description=f"{sebep}",
    )
    logembed.set_footer(text=f"Moderatör:{ctx.author}")
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
@commands.has_role("Moderatör")
async def mute(ctx, user: discord.Member = None, time=None, *, reason=None):
    if user == None:
        await ctx.send("Komutun kullanımı şöyledir: ',mute @kullanıcı <süre>.")
    elif time == None:
        await ctx.send("Süresini de ben mi belirleyeyim? \:D")
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
                title=f"{user}'in susturulma süresi doldu.",
                color=discord.Color.green())
            await logchannel.send(embed=muteremoved)
            await ctx.send(f"{user.mention} artık konuşabilir.")


@client.command(aliases=['sk'])
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, user: discord.Member):
    role_id = 799702960488710195
    muterole = discord.utils.get(ctx.guild.roles, id=role_id)
    logchannel = client.get_channel(810127270458163210)
    if muterole in user.roles:
        await user.remove_roles(muterole)
        muteremoved = discord.Embed(
            title=f"{user}'in susturulması {ctx.author} tarafından kaldırıldı.",
            color=discord.Color.green())
        await logchannel.send(embed=muteremoved)
        await ctx.send(f"{user.mention} artık konuşabilir.")
    else:
        await ctx.send("Bu kullanıcı zaten susturulmamış.")


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
        foto.save("Sonuç.png")
        await ctx.send(file=discord.File("Sonuç.png"))


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
    foto.save("Sonuç.gif")
    await ctx.send(file=discord.File("Sonuç.gif"))


guild_ids = [799630651191197737]


@slash.slash(name="gecikme", guild_ids=guild_ids)
async def _gecikme(ctx):
    embed = discord.Embed(
        title="Ping",
        description=f"Gecikme hesaplandı! ({client.latency*1000:.2f} ms)")
    await ctx.respond()
    await ctx.send(embed=embed)

@slash.slash(name="hype", guild_ids=guild_ids)
async def _hype(ctx):
    embed = discord.Embed(
        title="Ping",
        description=f"Gecikme hesaplandı! ({client.latency*1000:.2f} ms)")
    await ctx.respond()
    await ctx.send(embed=embed)


keep_alive()
TOKEN = os.environ.get('DISCORD_BOT_SECRET')
client.run(TOKEN)