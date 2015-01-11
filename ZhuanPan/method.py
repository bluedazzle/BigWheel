# -*- coding: utf-8 -*-
from ZhuanPan.NetSpider import *
import hashlib
import simplejson
import time

OPEN_ID = 'B34B72EB12F9434FB1363E329CFB7DA5'
SECRET = 'PTYELD'
HOST = 'http://openapi.1card1.cn'

def Sig(timestamp, data):
    sig = hashlib.md5(OPEN_ID + SECRET + str(timestamp) + data).hexdigest().upper()
    return sig


def getConsumList(phone=None):
    httpr = NetSpider()
    httpr.Host = 'openapi.1card1.cn'
    postdata = {}
    postdata['userAccount'] = "10003"
    if phone is None:
        postdata['where'] = '1=1'
    else:
        postdata['where'] = "1=1 and cardId='" + str(phone) + "'"
    postdata['pageIndex'] = 0
    postdata['pageSize'] = 10
    postdata['orderBy'] = 'operateTime desc'
    postjson = simplejson.dumps(postdata)
    now = str(time.time())
    sig = Sig(now, postjson)
    postdic = {}
    postdic['data'] = postjson
    requrl = 'https://openapi.1card1.cn/OpenApi/Get_ConsumeNotePaged?openId=' + OPEN_ID + '&signature=' + sig + '&timestamp=' + str(now)
    res = httpr.GetResFromRequest('POST', requrl, 'utf-8', postdic)
    return res

def getEleQuan():
    httpr = NetSpider()
    httpr.Host = 'openapi.1card1.cn'
    postdata = {}
    postdata['userAccount'] = "10003"
    postdata['where'] = '1=1'
    postdata['pageIndex'] = 0
    postdata['pageSize'] = 10
    postdata['orderBy'] = 'CreateTime desc'
    postjson = simplejson.dumps(postdata)
    now = str(time.time())
    sig = Sig(now, postjson)
    postdic = {}
    postdic['data'] = postjson
    requrl = 'https://openapi.1card1.cn/OpenApi/Get_CouponPaged?openId=' + OPEN_ID + '&signature=' + sig + '&timestamp=' + str(now)
    res = httpr.GetResFromRequest('POST', requrl, 'utf-8', postdic)
    # print res
    return res

def sendEleQuan(phone, type):
    httpr = NetSpider()
    httpr.Host = 'openapi.1card1.cn'
    guid = ['dad4cf91-2497-e411-b70a-90b11c47b4da', 'e591147c-2b97-e411-b70a-90b11c47b4da', 'a005ee51-2b97-e411-b70a-90b11c47b4da', '4579c9b8-2a97-e411-b70a-90b11c47b4da']
    postdata = {}
    postdata['userAccount'] = '10003'
    postdata['mobiles'] = str(phone)
    postdata['sendCount'] = 1
    postdata['couponGuid'] = guid[int(type)]
    postjson = simplejson.dumps(postdata)
    now = str(time.time())
    sig = Sig(now, postjson)
    postdic = {}
    postdic['data'] = postjson
    requrl = 'https://openapi.1card1.cn/OpenApi/SendCoupon?openId=' + OPEN_ID + '&signature=' + sig + '&timestamp=' + str(now)
    res = httpr.GetResFromRequest('POST', requrl, 'utf-8', postdic)
    return res

def test():
    httpr = NetSpider()
    httpr.Host = 'openapi.1card1.cn'
    postdata = {}
    postdata['cardId'] = '18215606355'
    postdata['password'] = '888888'
    postjson = simplejson.dumps(postdata)
    # postjson = '''{"password":"888888","cardId":"18215606355"}'''
    now = str(time.time())
    sig = Sig(now, postjson)
    postdic = {}
    postdic['data'] = postjson
    requrl = 'https://openapi.1card1.cn/OpenApi/MemberLogin?openId=' + OPEN_ID + '&signature=' + sig + '&timestamp=' + str(now)
    # print requrl
    res = httpr.GetResFromRequest('POST', requrl, 'utf-8', postdic)
    print res

