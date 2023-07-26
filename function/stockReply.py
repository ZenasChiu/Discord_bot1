# -*- coding: UTF-8 -*-
from datetime import datetime, date
import yfinance as yf
import pandas_datareader as pdr
#https://pythonviz.com/finance/yfinance-download-stock-data/
#{Index}             Open          High           Low         Close     Adj Close       Volume <------ Column Name
#Date
#2022-07-26  21361.121094  21361.121094  20776.816406  21239.753906  21239.753906  28624673855
#2022-07-27  21244.169922  22986.529297  21070.806641  22930.548828  22930.548828  31758955233
#2022-07-28  22933.640625  24110.470703  22722.265625  23843.886719  23843.886719  40212386158
#2022-07-29  23845.212891  24294.787109  23481.173828  23804.632812  23804.632812  35887249746
#2022-07-30  23796.818359  24572.580078  23580.507812  23656.207031  23656.207031  28148218301
#getting Date = record.index
#getting other elements = record.{Column Name}


# Download the record from yahoo finance by the yfinance API
def get_stock_record(stock_ID,period,interval): 
    a = yf.download(stock_ID,period=period,interval=interval)
    #print(a)
    return a 

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

#Gain = True
#Loss = False
def getdailyGL(record,num): #Definding daily Gain or Loss
    if(record.Open[num] > record.Close[num]):
        return False
    else:
        return True
    
def getSell_Statement(inp,sell_P,record,num,required_date):
    floatpoint2inP = "%.2f" % inp
    floatpoint2sellP = "%.2f" % sell_P
    return f"Buy in price {floatpoint2inP} Date {record.index[num]} After {required_date} days, Sell on {record.index[num+required_date]} : {floatpoint2sellP}"


#comparing price
#	--> win = x % (adjustment)
#	--> loss = 10 days above(each loss , average loss) --> mainpoint how cut loss
#	--> Total gain / Loss 


 # simulate the winRate in coming days (can sell out or not) By history
def getwinRate(record, num):
    sell_flag = False
    sell_RequireDays = 1
    #sell_statement=""
    inP = record.Close[num]
    targetP = inP * 1.01
    while(sell_flag == False):
        if(sell_RequireDays < 10):
            #print(f"{inP}  : {targetP}")
            next_data = num+sell_RequireDays
            if(next_data < len(record)):
                if(getdailyGL(record,num)):
                    if(targetP < record.Close[next_data]):
                        sell_P = record.Close[next_data]
                        #print("win")
                        #print(f"{targetP} vs {sell_P}")
                        #sell_statement += f"{getSell_Statement(inP,sell_P,record,num,sell_RequireDays)}"
                        print( f"Win :{getSell_Statement(inP,sell_P,record,num,sell_RequireDays)}")
                        sell_flag = True
                        print("1")
                        return True

                else:
                    if(targetP < record.Open[next_data]):
                        sell_P = record.Open[next_data]
                        #print(f"{targetP} vs {sell_P}")
                        #print("win")
                        #sell_statement += f"{getSell_Statement(inP,sell_P,record,num,sell_RequireDays)}"
                        print( f"Win :{getSell_Statement(inP,sell_P,record,num,sell_RequireDays)}")
                        sell_flag = True
                        print("2")
                        return True
                sell_RequireDays+=1
            else:
                #print("Loss")
                #sell_statement += f"Loss :{getSell_Statement(inP,sell_P,record,num,sell_RequireDays)}"
                print( f"Not yet sell")
                sell_flag = True
                print("5")
                return False

        elif(sell_RequireDays >= 10):
            sell_P = record.Close[next_data]
            #print("Loss")
            #sell_statement += f"Loss :{getSell_Statement(inP,sell_P,record,num,sell_RequireDays)}"
            print( f"Loss :{getSell_Statement(inP,sell_P,record,num,sell_RequireDays)}")
            sell_flag = True
            print("4")
            return False
    
    #return sell_statement

#Get the daily {?}MA number
def getSMA(current,record,average): 
    sum = 0
    for i in range(0,average):
        temp_current = current - i
        #print(temp_current)
        sum += record.Close[temp_current]
    sma = sum / average 
    #print(f"On {record.index[current]}:{average}MA = {sma}")
    return sma

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

#Comparing the  1 year of all {?}MA vs {?}MA
def comparing_MA(record, a_average,b_average):
    cross_list = []
    flag = False
    AV = getAverageV(record)
    for x in range(0,len(record.index)-b_average):
        #print(x)
        current_data = x + b_average-1
        #print(current_data)
        if (getSMA(current_data,record,a_average) > getSMA(current_data,record,b_average)):
            if(flag == False):
                cross_list.append(current_data)
                #cross_list.append(f"{record.index[current_data].to_pydatetime()} : PriceIn {record.Close[current_data]}: PriceOut : Volumn {comparerP(record.Volume[current_data],AV)} ")
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
    
#Getting Text message of record
def getRecordInf(record, num):
    return f"{record.index[num].to_pydatetime()} : PriceIn {record.Close[num]}"

#[OutFunciton] [testing]
#Getting the cross by comparing MA and Volume where show win rate also
def get_cross_data(stock_ID, aMA, bMA):
    record = get_stock_record(stock_ID,"1y","1d")
    inList = comparing_MA(record,aMA,bMA)
    AV = getAverageV(record)
    countLarge = 0
    countsmall = 0
    normal_winrate = 0
    #print(inList)
    print(f"Total : {len(inList)} : {inList}")
    for i in inList:
        if(getwinRate(record,i)):
            normal_winrate +=1

        if( getAveragePeriod(i, record,aMA) > AV):
            #if( getAveragePeriod(i, record,bMA) > AV):
            if(getwinRate(record,i)):
                countLarge +=1

        if( getAveragePeriod(i, record,aMA) < AV):
            #if( getAveragePeriod(i, record,bMA) < AV):
            if(getwinRate(record,i)):
                countsmall +=1
            
            #checklist.append(f"{getRecordInf(record,i) + Volume}")
    
    print(f"\nif count volume larger {countLarge}: {countLarge/len(inList)*100}\nif count volume smaller {countsmall} : {countsmall/len(inList)*100}\n Normal winRate {normal_winrate} : {normal_winrate/len(inList)*100}")
 
    return inList

    #text = f"Date where {aMA}MA is larger than{bMA}MA\n"
    #for x in comparing_MA(record,aMA,bMA):
    #    text += f"{x}\n"
    #return text


def main():
    print(get_cross_data("intc", 5, 10))

main()