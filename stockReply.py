# -*- coding: UTF-8 -*-
import yfinance as yf
import pandas_datareader as pdr


def each_High(records,num_value):
    a = records
    num = num_value
    higest_High = 0
    for x in range(num):
        temp_h = a.High[x]
        if float(temp_h) > higest_High:
            higest_High = temp_h
    return higest_High
    
def each_Low(records,num_value):
    a = records
    num = num_value
    lowest_Low  = 99999999
    for x in range(num):
        temp_l = a.Low[x]
        if float(temp_l) < lowest_Low:
            lowest_Low = temp_l    
    return lowest_Low

def getRecord(stock_ID, period,intervals):
    a = yf.download(stock_ID,period= period ,interval = intervals)
    return a

def get_basic_Details(stock_ID):
    Period_text = ["上一日","一星期","一個月","三個月","一年","三年","五年"]
    Period = ["1d","1wk","1mo", "3mo", "1y", "3y", "5y"]
    Intervals = ["1d","1d","1d","1d","1d","1wk","1wk"]
    stock = stock_ID
    #chat_id = chat_ID
    text = "Stock ID: {}\n".format(stock)
    try:
        for x in range(len(Period)) : 
            a = getRecord(stock_ID,period= Period[x],interval = Intervals[x])
            #print(a)
            num = len(a.index)
            high = each_High(a,num)
            low = each_Low(a,num)
            per_change = ((high - low)/low )%100
            text += "Period :{p}\n Higest_high :{H}\n Lowest_Low:{L}\nChange: {C}\n\n".format(p = Period_text[x], H = high, L = low, C = per_change)
            return text
    except:
        text = "Please reply correct Stock ID!"
        #bot.send_message(chat_id,text)
        return text

def getdailyPrediction(stock_ID):
    Period = "1y"
    Intervals = "1d"
    year_daily_price = getRecord(stock_ID, Period,Intervals)
    return year_daily_price

    

   

