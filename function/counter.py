from function.stockReply import get_all_history
from function.stockReply import get_stock_detail
from function.stockReply import get_cross_data
from function.youtubePic import searchpic


def message_reply(input, fun):
    if input == None:
        te = "Don't input Nothing"
    else:
        if fun == 1:
            text = get_all_history(input)
        elif fun == 2:
            text = searchpic(input)
    return text

def message_reply(input, input2, input3, fun):
    if input == None:
        te = "Don't input Nothing"
    else:
        if fun == 1:
            text = get_stock_detail(input,input2,input3)
        elif fun == 2:
            text = get_cross_data(input,input2,input3)
    return text