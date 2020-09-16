import re
import requests
from urllib import error
from bs4 import BeautifulSoup
import os
from PIL import Image

num = 0
numPicture = 0
file = ''
List = []
 
def Find(url):#找尋照片
    global List
    t = 0
    i = 1
    s = 0
    while t < 1000:
        Url = url + str(t)
        try:
            Result = requests.get(Url, timeout=7)
        except BaseException:
            t = t + 60
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)
            s += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
                List.append(pic_url)
                t = t + 60
    return s
 
def dowmloadPicture(html, keyword):#下載照片
    global num
    # t =0
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    print('正在下載' + keyword + '的圖片')
    for each in pic_url:
        print('第' + str(num + 1) + '張圖片，圖片網址:' + str(each))
        try:
            if each is not None:
                #each為圖片網址，ex:http://www.people.com.cn/mediafile/pic/20150429/29/12133827813414567173.jpg
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            print('無法下載')
            continue
        else:
            string = file + r'\\' + keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')    
            fp.write(pic.content)
            fp.close()
           
            try:
                im = Image.open(string)
                (x,y) = im.size 
                x_s = 150 #更改照片大小
                y_s = 150
                out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality
                out.save(string)
            except :
                continue
            
            num += 1

        if num >= numPicture:
            return
 
 
if __name__ == '__main__':
    word = input("輸入關鍵字: ")
    
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
    tot = Find(url)
    print('%s圖片共有%d張' % (word, tot))
    numPicture = int(input('下載數'))
    file = input('建立的資料夾名')
    y = os.path.exists(file)
    if y == 1:
        print('已存在請重新輸入')
        file = input('建立的資料夾名')
        os.mkdir(file)
    else:
        os.mkdir(file)
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=10)
            print(url)
           
        except error.HTTPError as e:
            print('網路錯誤')
            t = t+60

        else:
            dowmloadPicture(result.text, word)
            t = t + 60
 
    print('done')
	
	