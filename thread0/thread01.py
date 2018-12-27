import time
#from urllib.request import urlopen
import requests

def get_responses():
    urls = [
        'http://www.baidu.com',
        'http://www.taobao.com',
        'http://www.alibaba.com',
    ]
    start = time.time()
    for url in urls:
        print(url)
        resp = requests.get(url)
        #print(resp.code())   #得到状态码
        print("spent time:%s" % (time.time()-start))

get_responses()
