#https://hackmd.io/@kangjw/Discordpy%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%BE%9E0%E5%88%B01%E8%B6%85%E8%A9%B3%E7%B4%B0%E6%95%99%E5%AD%B8
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice

import cogs.youtubePic as y 
import helpguide as h
import stockReply as st

#--------------------------------------------------------------------------------------------------------------------------#
#bot是我們與Discord連結的橋樑
#bot = discord.bot()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "%", intents = intents)
token = "OTYwODMzMjQ5MzQ3Nzk2OTky.Gyyt9y.g4cc-F7Zm0lnx5zE7QqaLEP7bjF3Qzk4YFPpio"

#--------------------------------------------------------------------------------------------------------------------------#

#******event == 24 mon 
#******commands = check only have correct
#https://discord.com/developers/applications/960833249347796992/bot

#調用event函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    slash = await bot.tree.sync()
    print('目前登入身份：',bot.user)
    game = discord.Game('努力學習py中')
    #For setting statius
    #print(y.saySome())
    
#<Message id=962426414345375784 channel=<TextChannel id=960834155082567691 name='testing-channel' position=1 nsfw=False news=False category_id=947784637055389708> type=<MessageType.default: 0> author=<Member id=424439900314533888 name='CZenas' discriminator='8387' bot=False nick=None guild=<Guild id=947784637055389707 name='testingServer' shard_id=None chunked=False member_count=4>> flags=<MessageFlags value=0>>

@bot.event
async def on_message(message):
    #print("Test text : \n\n"+message.content.split(" ",2)[1])
    #排除自己的訊息，避免陷入無限循環
    tmp = message.content.split(" ",1)
    print(message)
    if message.author == bot.user:
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

#Command : ( name = {slash comment}, descriptions = {the funciton})
@bot.tree.command(name = "hello", description = "Hello, world!")
async def hello(interaction: discord.Interaction):
    # 回覆使用者的訊息
    await interaction.response.send_message("Hello, world!")

#Describe : create two varibale and adding in the coming function
@app_commands.command(name = "add", description = "計算相加值")
@app_commands.describe(a = "輸入數字", b = "輸入數字")
async def add(self, interaction: discord.Interaction, a: int, b: int):
    await interaction.response.send_message(f"Total: {a + b}")

# 參數: Optional[資料型態]，參數變成可選，可以限制使用者輸入的內容
@app_commands.command(name = "say", description = "大聲說出來")
@app_commands.describe(name = "輸入人名", text = "輸入要說的話")
async def say(self, interaction: discord.Interaction, name: str, text: Optional[str] = None):
    if text == None:
        text = "。。。"
    await interaction.response.send_message(f"{name} 說 「{text}」")

# @app_commands.choices(參數 = [Choice(name = 顯示名稱, value = 隨意)])
@app_commands.command(name = "order", description = "點餐機")
@app_commands.describe(meal = "選擇餐點", size = "選擇份量")
@app_commands.choices(
    meal = [
        Choice(name = "漢堡", value = "hamburger"),
        Choice(name = "薯條", value = "fries"),
        Choice(name = "雞塊", value = "chicken_nuggets"),
    ],
    size = [
        Choice(name = "大", value = 0),
        Choice(name = "中", value = 1),
        Choice(name = "小", value = 2),
    ]
)
async def order(self, interaction: discord.Interaction, meal: Choice[str], size: Choice[int]):
    # 獲取使用指令的使用者名稱
    customer = interaction.user.name
    # 使用者選擇的選項資料，可以使用name或value取值
    meal = meal.value
    size = size.value
    await interaction.response.send_message(f"{customer} 點了 {size} 號 {meal} 餐")

#https://gist.github.com/lykn/bac99b06d45ff8eed34c2220d86b6bf4
#using class as a menu of button
#create with button()

#https://stackoverflow.com/questions/69290541/attributeerror-module-discord-has-no-attribute-ui

bot.run(token)
