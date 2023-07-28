import numpy as np
from stock import Stock
from simulator import get_cross_data, comparing_MA
from stock_record import get_stock_record

stocks = []

stock_ID = "aapl"
# Please aMA should be smaller than bMA
#aMA = 5
#bMA = 15
budget = 10000
period_num = 4
#[0:"1d",1:"1wk",2:"1mo",3: "3mo",4: "1y",5: "3y",6: "5y"]
interval_num = 4
 #[0: "1m",1: "2m",2: "5m",3: "15m",4: "60m",5: "90m",6: "1d",7: "1wk",8: "3mo"]
rsi_range= 14
atr_range = 14
rsi_getATR_E_range= 0.9
day_getATR_E_range= 0.6

#========================
p_earning_range = 1.02
cut_lose = 0.97
earning = 0 
#stock_ID, aMA, bMA, budget,period_num,interval_num,p_earning_range,cut_lose_1,cut_lose_2,cut_lose_3,rsi_range,atr_range,rsi_getATR_E_range,day_getATR_E_range,earning

p_earning_range_range = np.arange(1.01,1.2,0.01)
cut_lose_range= np.arange(0.97,0.92,-0.01)

best_stock = None
performance = None
best_performance = None

#Find Best MA cross
def calculate_performance(stock,inList):
    stock.earning = get_cross_data(stock.record,inList,stock.budget,stock.p_earning_range,stock.cut_lose_1,stock.cut_lose_2,stock.cut_lose_3,stock.rsi_range,stock.atr_range,stock.rsi_getATR_E_range,stock.day_getATR_E_range)
    #stocks.append(stock)
    change = "%.2f" % stock.earning
    print(f"{len(inList)} : {change}%")
    return stock.earning

#period = ["1d","1wk","1mo","3mo","1y","3y","5y"]
#[0:"1d",1:"1wk",2:"1mo",3: "3mo",4: "1y",5: "3y",6: "5y"]
#intervals = ["1m","2m","5m","15m","60m","90m","1d","1wk","3mo"]
#[0: "1m",1: "2m",2: "5m",3: "15m",4: "60m",5: "90m",6: "1d",7: "1wk",8: "3mo"]
record = get_stock_record(stock_ID,"1y","1d")
for aMA in range(5,100,5):
    for bMA in range(5,200,15):
        print(f"{aMA} : {bMA}")
        stock = Stock(stock_ID, record,aMA,bMA,budget,p_earning_range,cut_lose,cut_lose,cut_lose,rsi_range,atr_range,rsi_getATR_E_range,day_getATR_E_range,earning)   
        for p_earning_range  in p_earning_range_range:
            if(aMA > bMA):
                break
            else:
                for cut_lose in cut_lose_range:
                    stock.p_earning_range = p_earning_range
                    stock.cut_lose_1 = cut_lose
                    stock.cut_lose_2 = cut_lose
                    stock.cut_lose_3 = cut_lose
                    inList = comparing_MA(record,aMA,bMA)
                    if(len(inList)<10):
                        break
                    else:
                        performance = calculate_performance(stock,inList)
        
                if best_performance is None or performance > best_performance:
                    best_stock = stock
                    best_performance = performance

print(f"aMA : {best_stock.aMA},bMA : {best_stock.bMA}, p_C : {best_stock.p_earning_range},cut : {best_stock.cut_lose_1}")
print(best_performance)