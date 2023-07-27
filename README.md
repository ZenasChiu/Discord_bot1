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
token = "haha" <------------------------------- change to your token

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

And there are lots of notes in the code
Just read those and find me anythime 
Enjoy


## My notes
MA : [Website](https://www.investopedia.com/terms/m/movingaverage.asp)
    range : x days 
    today to before x days average

RSI : 
Refer : [Website](https://www.wallstreetmojo.com/relative-strength-index/)
    range : x days
        ```
            [ 1, 2, 3, 4, 5]
              a  b
                 a  b
                    a  b
                       a  b
        ```
    where adding all close comparing the 
    a : num             <-----today
    b : num + 1         <-----Tomorrow
    loop range :
        --> a - b = - = adding lose
        --> a - b = + = adding gain
    lose/range
    gain/range

    RSI = 100 - (100 / ( 1 + (gain/lose) ) ) 

    This can be used on check buy or not 
        where if number is over the range ( where not allow the trade )

ATR :              
Refer : [website](https://www.investopedia.com/terms/a/atr.asp)
    range : x days -1 
        ```
            [1, 2, 3, 4, 5]
             c  a
                c  a
                   c  a
                      c  a
        ```
    
    a : num             <-----today
    c : num - 1         <-----Yesterday
    where getting :
    Find TR daily 
   
    - array of TR : []
    - a.High 
    - a.Low
    - c.Close
    H-L  : a.High - a.Low
    H-Cp : a.High - c .Close
    L-Cp : a.Low - c.Close
    if( < range - 1 )
        TR.appead(Max(H-L,H-Cp,L-Cp))
    else ( = yesterday_TR)


    P_ATR = sum(TR)/len(TR)

    ATR = (P_ATR * (range - 1) * (yesterday_TR) / range) 


#Data from yahoo finance where is 
    #Not real time

#Similation tool for testing your tactics

#There are some relationship find
#Changing MA should also change Time Holding risk
#Change Risk need to depend on the 基本面 of stock
  