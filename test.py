# from main import str_test
from typing import List, Dict
# from utils import Tile, dedup
# from yaku import get_all_yaku, is_kokushi_musou, is_chiitoitsu
# from random import shuffle, sample
import requests
import re
# import sys
import time


import datetime

def getIP():
    url = "http://10.50.255.12/"
    res = requests.get(url=url)
    res.encoding = 'gbk'
    ip = re.search("v46ip=\'([^\']*)\'", res.text).group(1)
    return ip


# def check(ip):
#     url = "http://p.njupt.edu.cn:802/eportal/?c=ACSetting&a=checkScanIP&wlanuserip=%s" % (ip)
#     res = requests.get(url=url)
#     status = re.search('\"result\":\"([^\"]*)\"', res.text).group(1)
#     if (status == 'ok'):
#         account = re.search('\"account\":\"([^\"]*)\"', res.text).group(1)
#         return account
#     else:
#         return False


# 登录，使用post向http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150发送账号密码。
def login(username, password, netType,Location):

    ip = getIP()

    #     if "仙林".__eq__(Location):
    #         wlan_ac_ip="10.255.252.150"
    #     elif "三牌楼".__eq__(Location):
    #         wlan_ac_ip="10.255.253.118"
    #     elif "物联网科技园".__eq__(Location):
    #         wlan_ac_ip="10.255.253.118"





    #
    if "移动".__eq__(netType):
        data = {"DDDDD": ",0,%s@cmcc" % (username), "upass": password}
        url="http://10.50.255.12:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C1%2C"+username+"%40cmcc&user_password="+password+"&wlan_user_ip="+ip+"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=2&lang=zh-cn&v=6055&lang=zh"
    elif "电信".__eq__(netType):
        data = {"DDDDD": ",0,%s@njxy" % (username), "upass": password}
        url="http://10.50.255.12:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C1%2C"+username+"%40telecom&user_password="+password+"&wlan_user_ip="+ip+"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=2&lang=zh-cn&v=8823&lang=zh"
    elif "NJUPT".__eq__(netType):
        data = {"DDDDD": ",0,%s" % (username), "upass": password}
    # url = "https://p.njupt.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C" + username + "%40"+netType+"&user_password=" + password + "&wlan_user_ip=" + ip + "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=XL-BRAS-SR8806-X&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2875&lang=zh"


    #         pass
    #
    #
    #res = requests.post(url=url, data=data)
    res = requests.post(url=url)

    return True


def isNetOK(testserver):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False


def str_test(tiles_str: str) -> List[str]:
    pass

    try:
        input = tiles_str.split(' ')
        # username, password, netType = "1221056113","Mss1003..","CMCC"
        username, password, netType ,Location= input[0], input[1], input[2],input[3]
    except:
        return "登录失败，输入用户名密码格式错误，请关注技术宅学长获取最新程序"

    while True:
        try:
            #ip = getIP()
            # return ip
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            # if now >="2024-01-01 00:00:00 000000":
            #     return "新年新版本发布了，请关注B站：技术宅学长 回复 校园网脚本 获取最新程序"
            # print("现在时间：" + now)
            # print("IP："+ip)
            # print("登录状态：" + check(ip).__str__())
            # time.sleep(2)

            # print("登录中：" + username)
            login(username, password, netType,Location)
            # time.sleep(2)
            return "登录成功，代码=1"
        except:
            pass
            return "登录失败404，请检查账号密码或者网络类型，请关注B站：技术宅学长 回复 校园网脚本 获取最新程序"
        # time.sleep(2)
        return "登录失败405，请检查账号密码或者网络类型，请关注B站：技术宅学长 回复 校园网脚本 获取最新程序"
    return "登录失败406，请检查账号密码或者网络类型，请关注B站：技术宅学长 回复 校园网脚本 获取最新程序"


if __name__ == '__main__':
    # result_str = str_test('1s 2s 3s 7p 8p 9p green green green west west 9p 8p 7p')
    # result_str = 123
    # print(result_str)
    pass
