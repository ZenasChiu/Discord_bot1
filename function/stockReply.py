# -*- coding: UTF-8 -*-
import math
from datetime import datetime, date
import yfinance as yf
import pandas_datareader as pdr
#https://pythonviz.com/finance/yfinance-download-stock-data/
#{Index}             Open          High           Low         Close     Adj Close       Volume          <------ Column Name
#Date
#2022-07-26  21361.121094  21361.121094  20776.816406  21239.753906  21239.753906  28624673855
#2022-07-27  21244.169922  22986.529297  21070.806641  22930.548828  22930.548828  31758955233
#2022-07-28  22933.640625  24110.470703  22722.265625  23843.886719  23843.886719  40212386158
#2022-07-29  23845.212891  24294.787109  23481.173828  23804.632812  23804.632812  35887249746
#2022-07-30  23796.818359  24572.580078  23580.507812  23656.207031  23656.207031  28148218301
#getting Date = record.index
#getting other elements = record.{Column Name}

#Find the Highest point in the period
def each_High(records,num_value):  
    a = records
    num = num_value
    higest_High = 0
    for x in range(num):
        temp_h = a.High[x]
        if float(temp_h) > higest_High:
            higest_High = temp_h
    return higest_High
    
#Find the Lowest point in the period    
def each_Low(records,num_value):   
    a = records
    num = num_value
    lowest_Low  = 99999999
    for x in range(num):
        temp_l = a.Low[x]
        if float(temp_l) < lowest_Low:
            lowest_Low = temp_l    
    return lowest_Low

#[OutFunciton]
#Getting all History record with Highest /Lowest Point
def get_all_history(stock_ID):
    Period = ["1d","1wk","1mo", "3mo", "1y", "3y", "5y"]
    Intervals = ["1d","1d","1d","1d","1d","1wk","1wk"]
    text = f"Stock ID: {stock_ID}\n"
    for x in range(len(Period)) : 
        text+= get_stock_detail(stock_ID,period=Period[x],interval= Intervals[x])
        return text

#[OutFunciton]
#Getting User input period
def get_stock_detail(stock_ID,period,interval):
    text = ""
    try:
        a = get_stock_record(stock_ID,period,interval)
        high = each_High(a,a.index)
        low = each_Low(a,a.index)
        per_change = ((high - low)/low )%100
        text += f"Period :{period}\n Higest_high :{high}\n Lowest_Low:{low}\nChange: {per_change}\n\n"
        return text
    except:
        text = "Please reply correct Stock ID!"
        return text


#Gain = True
#Loss = False
def getdailyGL(record,num): #Definding daily Gain or Loss
    if(record.Open[num] > record.Close[num]):
        return False
    else:
        return True

def getamount(price, budget):
    amount = math.floor(budget/price)
    leave = budget - price * amount
    return amount,leave


def getSMA(current,record,average):     #{s}MA
    sum = 0
    for i in range(0,average):
        temp_current = current - i
        sum += record.Close[temp_current]
    sma = sum / average 
    return sma

def getRSI(record, num,range_num):
    gain = 0 
    lose = 0
    for i in range(range_num,1,-1):
        current_num = num - i
        comparing = record.Close[current_num] - record.Close[current_num+1]
        if(comparing > 0):
            gain = gain + abs(comparing)
            
        else:
            lose = lose + abs(comparing)

    RSI = 100 - (100 / ( 1 + ( (gain/range_num) / (lose/range_num) ) ) ) 
    return RSI

def getATR(record, num,range_num):
    TR = []
    for i in range(range_num,-1,-1):
        current_num = num-i
        High,Low,Close = record.High[current_num], record.Low[current_num], record.Close[current_num-1]
        HL = abs(High - Low)
        HCp = abs(High - Close)
        LCp = abs(Low - Close)
        if (current_num == num):
            yTR = max(HL,HCp,LCp)
            break
        else:
            TR.append(max(HL,HCp,LCp))
    
    if(len(TR) != 0):
        P_ATR = sum(TR)/len(TR)
        ATR = (P_ATR * (range_num - 1) * (yTR) / range_num) 
    else :
        ATR = 0
    return ATR

#Get the Total average volumn 
def getAverageV(record):    
    sum = 0
    for i in range(0,len(record)):
        sum += record.Volume[i]
    return sum/len(record)

#Get the Period average volumn for testing
def getAveragePeriod(current,record,iMA): # 
    sum = 0 
    for i in range(0,iMA):
        data = current-i
        sum += record.Volume[data]
    return sum / i

#Get percentage of A in B
def comparerP(a,b):
    percentage = (a - b)/ b *100
    return percentage

def sellable(targetP,record,next_data):
    if(targetP < record.High[next_data]):
        return True
    else:
        return False

def cutlose(losevalue,record,next_data):
    if(losevalue > record.High[next_data]):
        return True
    else:
        if(losevalue > record.Low[next_data]):
            if (getdailyGL(record,next_data)):
                if(losevalue < record.Open[next_data]):
                    return  True
            else:
                if(losevalue < record.Close[next_data]):
                    return True
        else:            
            return False
        

#Comparing the  1 year of all {?}MA vs {?}MA
def comparing_MA(record, a_average,b_average):
    cross_list = []
    flag = False
    AV = getAverageV(record)
    for x in range(0,len(record.index)-b_average):
        current_data = x + b_average-1
        if (getSMA(current_data,record,a_average) > getSMA(current_data,record,b_average)):
            if(flag == False):
                cross_list.append(current_data)
                flag = True
        else:
            flag = False
        
    return cross_list

#Compare the daily {?}MA vs {?}MA
def comparing_MA_today(record, a_average,b_average):
    cross = False
    current_data = 364 - b_average
    if (getSMA(current_data,record,a_average) > getSMA(current_data,record,b_average)):
            cross = True
    return cross




def getSell_Statement(record,num,required_date,price):
    rSI = "%.2f" % (getRSI(record,num, 14))
    sell_date = num+required_date
    change = "%.2f" % ((price-record.Close[num])/record.Close[num] * 100)
    return f" Risk [ {rSI} ] Date Needed:{required_date} = {record.index[sell_date]} :{record.High[sell_date]} < {price} < {record.Low[sell_date]} change : {change}"


# simulate the trading in coming days (can sell out or not) By history updated from simlation
def simlation(record, num, next_num, amount):
    sell_flag = False
    sell_RequireDays = 1
    inP = record.Close[num]
    aTR = getATR(record, num,14)

    #------------------------------------------------------------------------------------#
    #-----------------------------Please change you risk Here----------------------------#
    #------------------------------------------------------------------------------------#
    #Set Risk dependent on stock can adjust the risk level of 
    if(aTR > inP * 1.03):
        targetP = inP + aTR
        losevalue = inP - aTR*1.3
    else:
        targetP = inP * 1.03
        losevalue = inP * 0.97
    #------------------------------------------------------------------------------------#
    #------------------------------------------------------------------------------------#
    #------------------------------------------------------------------------------------#

    while(sell_flag == False):
        next_data = num + sell_RequireDays
        if(next_data < len(record)):
            if(next_data < next_num ):
                #-------------------------------------------------#
                # Holding time management
                #-------------------------------------------------#
                if(sell_RequireDays >= 5):
                    targetP = inP + getATR(record, next_data,14)*0.5
                    losevalue = inP - getATR(record, next_data,14)
                if(sell_RequireDays >= 10):
                    targetP = inP + getATR(record, next_data,14)*0.1
                    losevalue = inP - getATR(record, next_data,14)
                #-------------------------------------------------#

                if(sellable(targetP,record,next_data)):
                    earning = targetP * amount
                    sell_flag = True
                    print(f"[ Win ] {getSell_Statement(record,num,sell_RequireDays,targetP)}")
                    return True,earning
                else:
                    if(cutlose(losevalue,record,next_data)):
                        earning = losevalue * amount
                        sell_flag = True
                        print(f"[Lose ] {getSell_Statement(record,num,sell_RequireDays,losevalue)}")
                        
                        return False,earning
                    else:
                        sell_RequireDays+=1
            else:
                earning = record.Open[next_data]*amount #not yet sell
                sell_flag = True
                print(f"[Hold ] T:{targetP} > In:{inP} > CurrentClose:{record.Close[next_data-1]} > Lose:{losevalue} ")
                return True, earning
        else:
            earning = record.Close[next_data-1]*amount #not yet sell
            sell_flag = True
            print(f"[Hold ] T:{targetP} > In:{inP} > CurrentClose:{record.Close[next_data-1]} > Lose:{losevalue} ")
            return True, earning

#[OutFunciton] [testing]
#Getting the cross by comparing MA and Volume where show win rate also
def get_cross_data(stock_ID, aMA, bMA,butget):
    #----------------------------------------------------------------#
    record = get_stock_record(stock_ID,"1y","1d") 
    #period = [
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
    #----------------------------------------------------------------#
    inList = comparing_MA(record,aMA,bMA)
    AV = getAverageV(record)
    countLarge = 0
    countsmall = 0
    normal_winrate = 0
    lose =0
    earning = butget
    leave = 0

    print(f"Total : {len(inList)} : {inList} ")
    inList.append(len(record)+1)
    for i in range(len(inList)-1):
        earning = earning + leave
        amount,leave = getamount(record.Close[inList[i]], earning)
        #print(f"{amount} / {earning}")
        win, earning = simlation(record,inList[i],inList[i+1],amount)
        #print(f"{inList[i]} : new {earning}")
        if(win):
            normal_winrate +=1
            if( getAveragePeriod(inList[i], record,aMA) > AV):
                    countLarge +=1
            if( getAveragePeriod(inList[i], record,aMA) < AV):
                    countsmall +=1
        else:
            lose += 1

    VL = "%.2f" % (countLarge/(len(inList)-1)*100)
    VS = "%.2f" % (countsmall/(len(inList)-1)*100)
    Nor = "%.2f" % (normal_winrate/(len(inList)-1)*100)
    gainLoss = "%.2f" % ((earning+leave-butget)/butget*100)
    
    print(f"Total change ${earning+leave} : {gainLoss}% \nVolume larger {countLarge}: {VL}%\nVolume smaller {countsmall} : {VS}%\nNormal winRate {normal_winrate} : {Nor} %")
 
    return inList[:-1]

# Download the record from yahoo finance by the yfinance API
def get_stock_record(stock_ID,period,interval): 
    a = yf.download(stock_ID,period=period,interval=interval)
    #print(a)                      # <----------------------------------------- if you want to doing some test 
    return a 

def main():
    StockID = "aapl"
    # Please aMA should be smaller than bMA
    aMA = 5
    bMA = 10
    Budget = 2000

    print(f"{StockID} Simlation of using {aMA}MA compare {bMA}MA")
    print(get_cross_data(StockID, aMA, bMA,Budget))

main()




#Data from yahoo finance where is 
    #Not real time

#Similation tool for testing your tactics

#There are some relationship find
#Changing MA should also change Time Holding risk
#Change Risk need to depend on the 基本面 of stock

