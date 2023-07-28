class Stock:
    def __init__(self, stock_ID,record, aMA, bMA, budget,p_earning_range,cut_lose_1,cut_lose_2,cut_lose_3,rsi_range,atr_range,rsi_getATR_E_range,day_getATR_E_range,earning):
        self.stock_ID = stock_ID
        self.record = record
        self.aMA = aMA
        self.bMA = bMA
        self.budget = budget
        self.p_earning_range = p_earning_range
        self.cut_lose_1 = cut_lose_1
        self.cut_lose_2 = cut_lose_2
        self.cut_lose_3 = cut_lose_3
        self.rsi_range=rsi_range
        self.atr_range = atr_range
        self.rsi_getATR_E_range= rsi_getATR_E_range
        self.day_getATR_E_range= day_getATR_E_range

        self.earning = earning
    
    @classmethod
    def checkdata(cls):
        print(f"{cls.stock_ID }= stock_ID\n{cls.aMA }= aMA\n{cls.bMA }= bMA\n{cls.budget}= budget\n{cls.period_num }= period_num\n{cls.interval_num }= interval_num\n{cls.rsi_range}= rsi_range\n{cls.atr_range }= atr_range\n{cls.rsi_getATR_E_range}= rsi_getATR_E_range\n{cls.day_getATR_E_range}= day_getATR_E_range\n{cls.p_earning_range }= p_earning_range\n{cls.cut_lose_1 }= cut_lose_1\n{cls.cut_lose_2 }= cut_lose_2\n{cls.cut_lose_3 }= cut_lose_3\n{cls.earning }= earning")
