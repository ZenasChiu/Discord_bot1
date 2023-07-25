#youtube_Pic
import re

def saySome():
    text = "hello i am from youtubepic"
    return text

def searchpic(keyword):
    str = keyword
    if(re.match('https://youtu.be/', str)):
        str2 = re.sub(r'https://youtu.be/',"", str)
        website = "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(str2)
    #print(str2)
    elif(re.match('https://www.youtube.com/watch\?v=', str)):
        str2 = re.sub(r'https://www.youtube.com/watch\?v=',"", str)
        website = "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(str2)
    elif(re.match('www.youtube.com/watch\?v=', str)):
        str2 = re.sub(r'www.youtube.com/watch\?v=',"", str)
        website = "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(str2)
    #print(str2)
    else: 
        website = "Not unacceptable/unvalid input"

    return website