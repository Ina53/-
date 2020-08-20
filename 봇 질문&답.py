import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('당신은 광자입니까?'):
        await message.channel.send('전 가위바위보해서 이긴 광자입니다')

    if message.content.startswith('당신은 광자를 닮았다고 생각합니까?'):
        await message.channel.send('본인입니다')

    if message.content.startswith('알유광자?'):
        await message.channel.send('WTF')

    if message.content.startswith('너 광자임?'):
        await message.channel.send('나한테 왜 그래?')

    if message.content.startswith('광자야'):
        await message.channel.send('왜')

    if message.content.startswith('빠순아 춘황이 소속그룹은?'):
        await message.channel.send('NCITY입니다')

    if message.content.startswith('빠순아 개식이 소속그룹은?'):
        await message.channel.send('NCITY입니다')

    if message.content.startswith('개식이처럼은 되면 안되겠다'):
        await message.channel.send('저두요')

    if message.content.startswith('개식이처럼은 안돼야지'):
        await message.channel.send('옳은 생각이에요')

    if message.content.startswith('영통 부러워'):
        await message.channel.send('나도 영통 제발 나도 영통 시켜주세요 돈 없어서 앨범을 못사요 지금 인간이랑 봇 차별하는 건가요?')

    if message.content.startswith('미연이 주접 떨어줘'):
        await message.channel.send('미연이는 무슨 상인지 알아 ? 조각상 .. 콧대가 조각상보다 높아..')

    if message.content.startswith('민니 주접 떨어줘'):
        await message.channel.send('민니 사실은 4개 국어 한다며? 한국어 태국어 귀여어 사랑스러어')

    if message.content.startswith('수진이 주접 떨어줘'):
        await message.channel.send('수진이는 레드립 바르면 안돼.. 내가 도를 넘어서 미치기 직전이니까')

    if message.content.startswith('소연이 주접 떨어줘'):
        await message.channel.send('내가 눈이 부셔서 해가 뜬 줄 알고 밖을 봤는데 알고보니까 소연아 사랑해가 떴던거지 뭐야')

    if message.content.startswith('우기 주접 떨어줘'):
        await message.channel.send('우기 좋아하는 사람 접어 했더니 나 북경 갔다 왔잖아')

    if message.content.startswith('슈화 주접 떨어줘'):
        await message.channel.send('우리 슈화 뭐든 잘하고 있고 너무 좋은데 하나만 고쳐줬으면 좋겠어 .. 내 심장')

    if message.content.startswith('우리언니 주접 떨어줘'):
        await message.channel.send('우리언니(于里言你) 개귀여어(凱歸蠡魚) 하고풍거(河鼓風去) 삭다해라(削多海蘿) 신의미모(神義美貌) 세상간지(世上間地) 용안에서(用安恚西) 비치난다(費治難多) 좌로인정(左虜人正) 우로인정(右虜人正) 압구루기(狎鷗漏器) 대굴대굴(大窟大窟)')

    if message.content.startswith('소원이 주접 떨어줘'):
        await message.channel.send('소원이는 쌍둥이 없지? 그럼 세상에서 제일 이쁘겠네')

    if message.content.startswith('예린이 주접 떨어줘'):
        await message.channel.send('우리 옌니 혈액형이 뭔지알아 ? 맞아 인형')

    if message.content.startswith('은하 주접 떨어줘'):
        await message.channel.send('우리 은하는 혼혈이지 ? 천국과 한국.. 많이 아팠겠다 하늘에서 떨어질 때')

    if message.content.startswith('유주 주접 떨어줘'):
        await message.channel.send('우리 유나 고음이 내 성적보다 높아ㅠㅠ 그래도 더 배워야할게 있네 인간인 척 하는거..')

    if message.content.startswith('신비 주접 떨어줘'):
        await message.channel.send('인생은 멀리서 보면 희극이고 가까이서 보면 비극이라는데 신비 얼굴은 가까이서 보면 볼수록 성은이 망극이다')

    if message.content.startswith('엄지 주접 떨어줘'):
        await message.channel.send('엄지야 기억나 ? 나랑 같이 불꽃놀이 보러갔을 때 내가 잠깐 기절했었잖아 사실 그거 엄지 얼굴보고 빛나서 기절한거야...')

    if message.content.startswith('우리 여친이들 주접 떨어줘'):
        await message.channel.send('우리언니(于里言你) 개예부다(凱叡部多) 하고풍거(河鼓風去) 삭다해라(削多海蘿) 매일이론(每日理論) 덕후마음(德厚馬音) 주접이라(主楪伊亽) 할지라도(轄地羅道) 내가알게(來駕謁揭) 모야XX(暮夜始發)')

    if message.content.startswith('빠순아'):
        await message.channel.send('왜')

    if message.content.startswith('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ'):
        await message.channel.send('왜 쳐웃어')

    if message.content.startswith('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ'):
        await message.channel.send('왜 쳐웃냐고!')
        
    if message.content.startswith('웃지도 못하냐'):
        await message.channel.send('응 ㅋ')
        
client.run('NzQ1MjcwNzI3MzQ3MDExNjQ1.XzvVcw.Llov7BPsGheaiY8W5Nu9wxMbBsQ')
