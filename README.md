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


## The Stock Simulator
### function/stockReply.py <------------ this can run Alone with main()
```
> This simulator 
> Base on MA x MA cross to find spot for Buy in 
> Using two way for cut profit and lose
>   --> set % 
>   --> ATR 
```
#### There are mainly three place to change value


##### In line 326 START point
``` 
def main():
    StockID = "aapl"                        <--- Check Stock ID from yahoo finance
    # Please aMA should be smaller than bMA
    aMA = 5                                 <--- First MA line 
    bMA = 10                                <--- Second MA line
    Budget = 2000

    print(f"{StockID} Simlation of using {aMA}MA compare {bMA}MA")
    print(get_cross_data(StockID, aMA, bMA,Budget))

main()
```
##### In line 263
```
    record = get_stock_record(stock_ID,"1y","1d") <---- 
    #Adjust your data set "get_stock_record(stock_ID,{period},{intervals})"
```

##### In line 205 Adjust the Target Price (cut profit) and losevalue (cut lose line) 
```
    if(aTR > inP * 1.03):
        targetP = inP + aTR
        losevalue = inP - aTR*1.3
    else:
        targetP = inP * 1.03
        losevalue = inP * 0.97
```

##### In line 226 Re-Adjust the cuts
###### where can increase the selling chance due with the holding time
```
if(sell_RequireDays >= 5):
    targetP = inP + getATR(record, next_data,14)*0.5
    losevalue = inP - getATR(record, next_data,14)
if(sell_RequireDays >= 10):
    targetP = inP + getATR(record, next_data,14)*0.1
    losevalue = inP - getATR(record, next_data,14)
```

##### Result in Terminal
```
PS C:\Users\zenasc\Downloads\self_Project\Discord_bot> & c:/Users/zenasc/Downloads/self_Project/Discord_bot/discord_venv/Scripts/python.exe c:/Users/zenasc/Downloads/self_Project/Discord_bot/function/stockReply.py       
aapl Simlation of using 3MA compare 5MA
[*********************100%***********************]  1 of 1 completed
Total : 28 : [4, 10, 31, 38, 49, 56, 67, 75, 85, 90, 96, 105, 110, 114, 131, 139, 152, 159, 170, 180, 189, 196, 200, 204, 210, 219, 228, 242]
[ Win ]  Risk [ 76.28 ] Date Needed:1 = 2022-08-03 00:00:00 :166.58999633789062 < 164.81029434204103 < 160.75 change : 3.00
[ Win ]  Risk [ 74.16 ] Date Needed:5 = 2022-08-17 00:00:00 :176.14999389648438 < 174.9803137688123 < 172.57000732421875 change : 3.39
[ Win ]  Risk [ 81.59 ] Date Needed:1 = 2022-09-12 00:00:00 :164.25999450683594 < 162.09109497070312 < 159.3000030517578 change : 3.00
[Lose ]  Risk [ 55.95 ] Date Needed:2 = 2022-09-22 00:00:00 :154.47000122070312 < 152.19299407958985 < 150.91000366210938 change : -3.00
[Lose ]  Risk [ 58.44 ] Date Needed:3 = 2022-10-10 00:00:00 :141.88999938964844 < 142.00799407958985 < 138.57000732421875 change : -3.00
[ Win ]  Risk [ 60.77 ] Date Needed:1 = 2022-10-17 00:00:00 :142.89999389648438 < 142.53140502929688 < 140.27000427246094 change : 3.00
[Lose ]  Risk [ 30.64 ] Date Needed:3 = 2022-11-03 00:00:00 :142.8000030517578 < 148.7397964477539 < 138.75 change : -3.00
[ Win ]  Risk [ 63.29 ] Date Needed:3 = 2022-11-15 00:00:00 :153.58999633789062 < 151.27609497070313 < 148.55999755859375 change : 3.00
[Lose ]  Risk [ 31.26 ] Date Needed:1 = 2022-11-28 00:00:00 :146.63999938964844 < 143.66670059204102 < 143.3800048828125 change : -3.00
[Lose ]  Risk [ 52.29 ] Date Needed:3 = 2022-12-07 00:00:00 :143.3699951171875 < 143.37569763183595 < 140.0 change : -3.00
[ Win ]  Risk [ 59.86 ] Date Needed:1 = 2022-12-13 00:00:00 :149.97000122070312 < 148.824705657959 < 144.24000549316406 change : 3.00
[Lose ]  Risk [ 73.42 ] Date Needed:3 = 2022-12-29 00:00:00 :130.47999572753906 < 127.90420059204101 < 127.7300033569336 change : -3.00
[ Win ]  Risk [ 73.79 ] Date Needed:3 = 2023-01-06 00:00:00 :130.2899932861328 < 128.82209968566895 < 124.88999938964844 change : 3.00
[ Win ]  Risk [ 57.95 ] Date Needed:3 = 2023-01-12 00:00:00 :134.25999450683594 < 134.05449371337892 < 131.44000244140625 change : 3.00
[ Win ]  Risk [ 20.94 ] Date Needed:1 = 2023-02-03 00:00:00 :157.3800048828125 < 155.34460754394533 < 147.8300018310547 change : 3.00
[Hold ] T:154.5982116963605 > In:153.1999969482422 > CurrentClose:151.02999877929688 > Lose:139.21784946705898 
[Hold ] T:159.062248396433 > In:153.8300018310547 > CurrentClose:152.58999633789062 > Lose:143.36550870029808
[ Win ]  Risk [ 44.09 ] Date Needed:3 = 2023-03-20 00:00:00 :157.82000732421875 < 157.57970565795898 < 154.14999389648438 change : 3.00
[Hold ] T:169.7813432041065 > In:162.36000061035156 > CurrentClose:165.55999755859375 > Lose:147.51731542284168
[Hold ] T:168.38630130935618 > In:165.2100067138672 > CurrentClose:163.75999450683594 > Lose:158.85741752288922
[Hold ] T:178.48243016499683 > In:168.41000366210938 > CurrentClose:173.57000732421875 > Lose:148.26515065633444
[Hold ] T:178.705 > In:173.5 > CurrentClose:173.75 > Lose:168.295
[Hold ] T:177.7471075439453 > In:172.57000732421875 > CurrentClose:172.69000244140625 > Lose:167.3929071044922
[Hold ] T:177.7001878732675 > In:175.0500030517578 > CurrentClose:172.99000549316406 > Lose:169.7496334087384
[ Win ]  Risk [ 51.89 ] Date Needed:4 = 2023-06-02 00:00:00 :181.77999877929688 < 180.6928924560547 < 179.25999450683594 change : 3.00
[ Win ]  Risk [ 35.74 ] Date Needed:4 = 2023-06-15 00:00:00 :186.52000427246094 < 186.3888069152832 < 183.77999877929688 change : 3.00
[ Win ]  Risk [ 32.76 ] Date Needed:5 = 2023-06-30 00:00:00 :194.47999572753906 < 192.18398429797452 < 191.25999450683594 change : 2.95
[ Win ]  Risk [ 40.06 ] Date Needed:3 = 2023-07-19 00:00:00 :198.22999572753906 < 196.41070251464845 < 192.64999389648438 change : 3.00
Total change $2565.5570469247336 : 28.28%              
Volume larger 22: 78.57%
Volume smaller 0 : 0.00%
Normal winRate 22 : 78.57 %
[4, 10, 31, 38, 49, 56, 67, 75, 85, 90, 96, 105, 110, 114, 131, 139, 152, 159, 170, 180, 189, 196, 200, 204, 210, 219, 228, 242]
```



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
  