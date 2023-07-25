import discord
import time, discord, datetime
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
from core.classes import Cog_Extension
from function.counter import message_reply


class Slash(Cog_Extension):
    # name指令名稱，description指令敘述
    @app_commands.command(name = "hello", description = "Hello, world!")
    async def hello(self, interaction: discord.Interaction):
        # 回覆使用者的訊息
        await interaction.response.send_message("Hello, world!")
#1------------------------------------------------------------------------------------------------------#
    # 參數: Optional[資料型態]，參數變成可選，可以限制使用者輸入的內容
    @app_commands.command(name = "say", description = "大聲說出來")
    @app_commands.describe(name = "輸入人名", text = "輸入要說的話")
    async def say(self, interaction: discord.Interaction, name: str, text: Optional[str] = None):
        if text == None:
            text = "。。。"
        await interaction.response.send_message(f"{name} 說 「{text}」")
#2------------------------------------------------------------------------------------------------------#
    
    @app_commands.command(name = "stock", description = "上一日,一星期,一個月,三個月,一年,三年,五年 全歷史高低")
    @app_commands.describe(stock_id = "輸入stock id",)
    async def stock(self, interaction: discord.Interaction, stock_id: Optional[str] = None):
        await interaction.response.send_message(f"{message_reply(stock_id, 1)}")
#3------------------------------------------------------------------------------------------------------#
    @app_commands.command(name = "yt_thrumbnail", description = "幫你拎thrumbnail")
    @app_commands.describe(youtube_link = "Copy the shared like here")
    async def youtube_thrumbnail(self, interaction: discord.Interaction, youtube_link: Optional[str] = None):
        await interaction.response.send_message(f"{message_reply(youtube_link, 2)}")

#5------------------------------------------------------------------------------------------------------#
    @app_commands.command(name = "stock_menu", description = "點歷史高低")
    @app_commands.describe(stock_id = "輸入stock id", period = "選擇Period",intervals= "選擇間隔")
   #@app_commands.choices(
   #    period = [
   #        Choice(name = "上一日", value = "1d"),
   #        Choice(name = "一星期", value = "1wk"),
   #        Choice(name = "一個月", value = "1mo"),
   #        Choice(name = "三個月", value = "3mo"),
   #        Choice(name = "一年", value = "1y"),
   #        Choice(name = "三年", value = "3y"),
   #        Choice(name = "五年", value = "5y"),
   #    ],
   #    intervals = [
   #        Choice(name = "1m", value = "1m"),
   #        Choice(name = "2m", value = "2m"),
   #        Choice(name = "5m", value = "5m"),
   #        Choice(name = "15m", value = "15m"),
   #        Choice(name = "60m", value = "60m"),
   #        Choice(name = "90m", value = "90m"),
   #        Choice(name = "1d", value = "1d"),
   #        Choice(name = "1wk", value = "1wk"),
   #        Choice(name = "3mo", value = "3mo"),
   #    ])
    async def stock_details(self, interaction: discord.Interaction,period:  Optional[str]= None ,intervals :  Optional[str]= None, stock_id: Optional[str]= None):
        await interaction.response.send_message(f"{message_reply(stock_id,period,intervals, 1)}")
    
#6------------------------------------------------------------------------------------------------------#
    @app_commands.command(name = "stock_cross", description = "點餐機")
    @app_commands.describe(stock_id = "輸入stock id", aMA = "選擇First MA", bMA= "選擇Second MA")
    async def stock_cross(self, interaction: discord.Interaction, stock_id: Optional[str]= None, aMA: Optional[int] = None, bMA: Optional[int]=None ):
        await interaction.response.send_message(f"{message_reply(stock_id,aMA,bMA, 2)}")
    
#------------------------------------------------------------------------------------------------------#

async def setup(bot: commands.Bot):
    await bot.add_cog(Slash(bot))