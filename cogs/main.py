import discord
import time, discord, datetime
from discord.ext import tasks, commands
# 導入core資料夾中的自寫模組

from core.classes import Cog_Extension

# 繼承Cog_Extension的self.bot物件
class Main(Cog_Extension):  # 每日十二點發送 
    # 臺灣時區 UTC+8
    print("done")
    tz = datetime.timezone(datetime.timedelta(hours = 8))
    # 設定每日十二點執行一次函式
    everyday_time = datetime.time(hour = 0, minute = 0, tzinfo = tz)
    
    def __init__(self, bot):
        super().__init__(bot)
        self.everyday.start()
    
    # 每日十二點發送 "晚安!瑪卡巴卡!" 訊息
    @tasks.loop(time = everyday_time)
    async def everyday(self):
        # 設定發送訊息的頻道ID
        channel_id = 960834155082567691
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            title = "🛏 早晨！",
            description = f"🕛 現在時間 {datetime.date.today()} 00:00\n",
            color = discord.Color.orange()
        )
        await channel.send(embed = embed)


# 載入cog中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))