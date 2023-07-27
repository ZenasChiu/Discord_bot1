# Discord_bot1(https://ithelp.ithome.com.tw/articles/10267344)

## python package :
pip install discord.py
pip install regex
pip install yfinance

## Application Structure :
```
Bot 
    --> Main 
        <--> classes.py as(memory)
    --> slash --> counter (menu of funciton) 
                    --> helpguide
                    --> stockReply
                    --> youtubePic
        <--> classes.py as(memory)
    --> task
        <--> classes.py as(memory)
```

## User Guide:
Running --> bot.py as a hold of discordbot *( where change your token )*
```
import os
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)
token = "OTYwODMzMjQ5MzQ3Nzk2OTky.Gyyt9y.g4cc-F7Zm0lnx5zE7QqaLEP7bjF3Qzk4YFPpio" <------------------------------- change to your token

```
##### Learn from https://hackmd.io/@smallshawn95/python_discord_bot_base 


## Test
### function/stockReply.py
```
def main():
    print(get_cross_data("T", 5, 10,2000)) <------------------------------------ rewrite the data you want to test

main()
```
```
> Total change $2048.1499738693237 : 2.41%
> if count volume larger 4: 30.77%
> if count volume smaller 2 : 15.38%
> Normal winRate 6 : 46.15 %
> [14, 51, 59, 85, 87, 95, 108, 125, 142, 164, 217, 233, 249]
```

It should return something like this in Terminal 
