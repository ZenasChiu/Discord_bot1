import math
from stock_record import get_stock_record

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
    current_data = len(record) - b_average
    if (getSMA(current_data,record,a_average) > getSMA(current_data,record,b_average)):
            cross = True
    return cross


def getSell_Statement(record,num,required_date,price):
    rSI = "%.2f" % (getRSI(record,num, 14))
    sell_date = num+required_date
    change = "%.2f" % ((price-record.Close[num])/record.Close[num] * 100)
    return f" Risk [ {rSI} ] Date Needed:{required_date} = {record.index[sell_date]} :{record.High[sell_date]} < {price} < {record.Low[sell_date]} change : {change}"


# simulate the trading in coming days (can sell out or not) By history updated from simlation
def simlation(record, num, next_num, amount,p_earning_range,cut_lose_1,cut_lose_2,cut_lose_3,rsi_range,atr_range,rsi_getATR_E_range,day_getATR_E_range):
    sell_flag = False
    sell_RequireDays = 1
    inP = record.Close[num]
   
    while(sell_flag == False):
        next_data = num + sell_RequireDays
        if(next_data < len(record)):
            if(next_data < next_num ):
                rsi = getRSI(record, next_data,rsi_range)
                targetP = inP *1.1
                losevalue = 0
                #-------------------------------------------------#
                # Holding time management
                #-------------------------------------------------#
                if(rsi >= 70 or rsi <= 30):
                    targetP = inP + getATR(record, next_data,atr_range)*rsi_getATR_E_range
                    losevalue = inP *cut_lose_1
                else:
                   if(sell_RequireDays > 5):
                       targetP = inP + getATR(record, next_data,atr_range)*day_getATR_E_range
                       losevalue = inP * cut_lose_2
                   else:
                       targetP = inP * p_earning_range
                       losevalue = inP * cut_lose_3

                    #losevalue = inP - getATR(record, next_data,14)
                #-------------------------------------------------#

                if(sellable(targetP,record,next_data)):
                    earning = targetP * amount
                    sell_flag = True
                    #print(f"[ Win ] {getSell_Statement(record,num,sell_RequireDays,targetP)}")
                    return earning
                else:
                    if(cutlose(losevalue,record,next_data)):
                        earning = losevalue * amount
                        sell_flag = True
                        #print(f"[Lose ] {getSell_Statement(record,num,sell_RequireDays,losevalue)}")
                        
                        return earning
                    else:
                        sell_RequireDays+=1
            else:
                earning = record.Open[next_data]*amount #not yet sell
                sell_flag = True
                #print(f"[Hold ] T:{targetP} > In:{inP} > CurrentClose:{record.Close[next_data-1]} > Lose:{losevalue} ")
                return earning
        else:
            earning = record.Close[next_data-1]*amount #not yet sell
            sell_flag = True
            #print(f"[Hold ] T:{targetP} > In:{inP} > CurrentClose:{record.Close[next_data-1]} > Lose:{losevalue} ")
            return earning

#[OutFunciton] [testing]
#Getting the cross by comparing MA and Volume where show win rate also
def get_cross_data(record,inList,budget,p_earning_range,cut_lose_1,cut_lose_2,cut_lose_3,rsi_range,atr_range,rsi_getATR_E_range,day_getATR_E_range):
    #print (inList)
    earning = budget
    leave = 0
    inList.append(len(record)+1)
    for i in range(len(inList)-1):
        earning = earning + leave
        amount,leave = getamount(record.Close[inList[i]], earning)
        earning = simlation(record,inList[i],inList[i+1],amount,p_earning_range,cut_lose_1,cut_lose_2,cut_lose_3,rsi_range,atr_range,rsi_getATR_E_range,day_getATR_E_range)
        
    total_change = (earning+leave-budget)/budget*100
    
    return total_change

