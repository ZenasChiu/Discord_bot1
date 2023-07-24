#helpfguide


def guide():
 function_name = ['Youtube thumbnail graper','Stock Checker ']
 function_code = ["Ypic"+" {"+"youtube link"+"}","Stock"+" {"+"Stock ID"+"}"]
 function_ex= ["Ypic https://youtu.be/xxxxxxxxxxxx", "Stock aapl"]
 function_desc = ['Funciton for getting full size youtube thumbnail','Function for checking the stock highest high/Lowest Low in different Period']
 text = "\t\(O~O) Welcome to sharky help (O~O)/\n  Following comment is provide for you to use :\n"
 for i in range(0,len(function_name)):
    text += "\n\t@Function number {num} - {name} @\t\nComment :\t{code} \nExample :\t{ex}\nDescribe : {desc}\n\n".format(num = i+1,code = function_code[i], name = function_name[i],ex = function_ex[i],desc = function_desc[i]) 

 return text

#print(guide())