import yfinance as yf
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

def get_stock_record(stock_ID,period,interval): 
    return yf.download(stock_ID,period=period,interval=interval)