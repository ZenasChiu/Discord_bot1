# -*- coding: UTF-8 -*-
from datetime import datetime, date
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

def get_all_history(stock_ID):
    Period = ["1d","1wk","1mo", "3mo", "1y", "3y", "5y"]
    Intervals = ["1d","1d","1d","1d","1d","1wk","1wk"]
    text = f"Stock ID: {stock_ID}\n"
    for x in range(len(Period)) : 
        text+= get_stock_detail(stock_ID,period=Period[x],interval= Intervals[x])
        return text
   

def getSMA(current,record,average):
    sum = 0
    for i in range(0,average):
        temp_current = current - i
        #print(temp_current)
        sum += record.Close[temp_current]
    sma = sum / average 
    #print(f"On {record.index[current]}:{average}MA = {sma}")
    return sma

def comparing_MA(record, a_average,b_average):
    cross_list = []
    flag = False
    for x in range(0,len(record.index)-b_average):
        print(x)
        current_data = x + b_average-1
        #print(current_data)
        if (getSMA(current_data,record,a_average) > getSMA(current_data,record,b_average)):
            if(flag == False):
                cross_list.append(f"{record.index[current_data].to_pydatetime()} : Price {record.Close[current_data]}")
                flag = True
        else:
            flag = False
        
    return cross_list

def comparing_MA_today(record, a_average,b_average):
    cross = False
    current_data = 364 - b_average
    if (getSMA(current_data,record,a_average) > getSMA(current_data,record,b_average)):
            cross = True
    return cross

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

def get_cross_data(stock_ID, aMA, bMA):
    record = get_stock_record(stock_ID,"1y","1d")
    text = f"Date where {aMA}MA is larger than{bMA}MA "
    for x in comparing_MA(record,aMA,bMA):
        text += f"{x}\n"
    return text

def get_stock_record(stock_ID,period,interval):
    a = yf.download(stock_ID,period=period,interval=interval)
    print(a.index[1])
    return a 

def main():
    print(get_cross_data("BTC-USD", 5, 10))

main()