# coding: utf-8

import time
import json
import random
import requests
import webbrowser
import urllib
import pandas as pd
import numpy as np

import datetime
from wechat_sender import Sender




headers0 = {
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'user-agent': 'okhttp/3.9.0',
    'Connection': 'Keep-Alive',
    'Host': 'phoenix.ziroom.com',
    'Accept-Encoding': 'gzip',
    'Accept': 'application/json;version=3',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }





def get_answer():
    resp = requests.get('http://phoenix.ziroom.com/v7/room/detail.json?network=4G&sign_open=1&app_version=5.4.5&house_id=17512&sign=c879a011deba72d7559a65d4d964938f&imei=861365031181741&id=127033&ip=&uid=0&timestamp=1520475675&city_code=110000&os=android%3A5.0.2&model=Redmi+Note+3%20HTTP/1.1',headers=headers0,timeout=5).json()
    resp_dict = resp
    resp_dict = eval(str(resp))
    if resp_dict['status'] == 'success':
        if resp_dict['data']['status']=='tzpzz':
            print('房屋待释放...')
            sendanswer('房屋待释放...')
        else:
            sendanswer('赶紧上自如APP...')

def sendanswer(answer):
    msg=str(answer)
    Sender(receivers='吴震',port=10002).send(msg)




def main():
    while 1:
        get_answer()
        time.sleep(30+random.random(2))




if __name__ == '__main__':
    main()
