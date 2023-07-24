#https://hackmd.io/@kangjw/Discordpy%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%BE%9E0%E5%88%B01%E8%B6%85%E8%A9%B3%E7%B4%B0%E6%95%99%E5%AD%B8
import discord
from discord.ext.commands import Bot

import youtubePic as y 
import helpguide as h
import stockReply as st
#client是我們與Discord連結的橋樑
#client = discord.Client()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
token = "OTYwODMzMjQ5MzQ3Nzk2OTky.Gyyt9y.g4cc-F7Zm0lnx5zE7QqaLEP7bjF3Qzk4YFPpio"

#******event == 24 mon 
#******commands = check only have correct
#https://discord.com/developers/applications/960833249347796992/bot

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('努力學習py中')
    #For setting statius
    #print(y.saySome())
    
#<Message id=962426414345375784 channel=<TextChannel id=960834155082567691 name='testing-channel' position=1 nsfw=False news=False category_id=947784637055389708> type=<MessageType.default: 0> author=<Member id=424439900314533888 name='CZenas' discriminator='8387' bot=False nick=None guild=<Guild id=947784637055389707 name='testingServer' shard_id=None chunked=False member_count=4>> flags=<MessageFlags value=0>>

@client.event
async def on_message(message):
    #print("Test text : \n\n"+message.content.split(" ",2)[1])
    #排除自己的訊息，避免陷入無限循環
    tmp = message.content.split(" ",1)
    print(message)
    if message.author == client.user:
        return
    #如果以「說」開頭
    if message.content.startswith('say'):
      #分割訊息成兩份
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send(" \(@~@)/ What do you want me to say ?")
      else:
        text = ""
        for i in range(1,len(tmp)):
            text += " "+tmp[i]
        await message.channel.send(text)
        
    if message.content.startswith('Ypic'or'ypic'):
        if len(tmp) == 1:
            await message.channel.send("????????") 
        else:
            text = y.searchpic(tmp[1])
            await message.channel.send(text)
    if message.content.startswith('-help'or'-Help'):
        text = h.guide()
        await message.channel.send(text)
    if message.content.startswith('Stock'or'stock'):
        if len(tmp) == 1:
            await message.channel.send("????????") 
        else:
            text = st.get_basic_Details(tmp[1])
            await message.channel.send(text)


#https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4
#using class as a menu of button
#create with button()

#https://stackoverflow.com/questions/69290541/attributeerror-module-discord-has-no-attribute-ui

client.run(token)
