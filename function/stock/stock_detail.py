from stock_record import get_stock_record
from stock_detail_DTO import Stock

def each_High(record):  
    higest_High = 0
    for x in range(len(record)):
        temp_h = record.High[x]
        if float(temp_h) > higest_High:
            higest_High = temp_h
    return higest_High
    
#Find the Lowest point in the period    
def each_Low(record):   
    lowest_Low  = 99999999
    for x in range(len(record)):
        temp_l = record.Low[x]
        if float(temp_l) < lowest_Low:
            lowest_Low = temp_l    
    return lowest_Low

def showvalue(stocks):
    text = ""
    for i in stocks:
        per_change = ((i.high - i.Low)/i.low)*100
        text += f"Period : {i.period}\nHigest High \t: ${i.high}\nLowest Low \t: ${i.low}\nChange \t\t: {per_change}%\n\n"

    return text

def getAveragePercentageChange(stocks):
    sum = 0 
    for i in stocks:
        print(((i.high - i.low)/i.low)*100)
        sum += ((i.high - i.low)/i.low)*100

    return sum /len(stocks)


#[OutFunciton]
#Getting User input period
def get_stock_detail(stock_ID,period,interval):
    try:
        a = get_stock_record(stock_ID,period,interval)
        #print(a)
        #print(each_High(a))
        #print(each_Low(a))
        stock = Stock(stock_ID,each_High(a),each_Low(a),period,interval)
        #print(stock)
        return stock
    except:
        stock = Stock(stock_ID,50,50,period,interval)
        return stock


#[OutFunciton]
#Getting all History record with Highest /Lowest Point
def get_all_history(stock_ID):
    Period = ["1d","1wk","1mo", "3mo", "1y", "3y", "5y"]
    Intervals = ["1d","1d","1d","1d","1d","1wk","1wk"]

    Stocks = []
    for x in range(len(Period)) : 
        stock = get_stock_detail(stock_ID,period=Period[x],interval= Intervals[x])
        Stocks.append(stock)
    print(Stocks)
    return  Stocks
    


def test():
    stock_ID = "t"
    print(getAveragePercentageChange(get_all_history(stock_ID)))
    #print(get_all_history(stock_ID))

test()
    