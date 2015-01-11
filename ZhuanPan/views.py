# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from ZhuanPan.models import *
from ZhuanPan.method import *
import datetime
import simplejson
# Create your views here.

def first(req):
    return render_to_response('verify.html')

def verify(req):
    content = ''
    rewardlist = None
    consum = None
    if req.method == 'GET':
        phone = req.GET['phone']
        res = getConsumList(phone)
        # print res
        jsonres = simplejson.loads(res)
        status = str(jsonres['status'])
        if status == '0':
            rewardlist = Reward.objects.all().order_by('-time')
            data = simplejson.loads(jsonres['data'])
            for itm in data:
                cid = str(itm['BillNumber'])
                ifhave = Consume.objects.filter(c_id = cid)
                if ifhave.count() > 0:
                    continue
                newconsum = Consume()
                newconsum.c_id = cid
                newconsum.phone = phone
                newconsum.total = float(itm['TotalPaid'])
                yutt = time.strptime(str(itm['OperateTime']), "%Y-%m-%d %H:%M:%S")
                yudatetime = datetime.datetime(*yutt[:6])
                newconsum.consume_time = yudatetime
                newconsum.save()
        else:
            raise Http404
        req.session['phone'] = phone
        consum_list = Consume.objects.filter(phone = str(phone)).order_by('-consume_time')
        now = datetime.datetime.now()
        if consum_list.count() > 0:
            i = 0
            for itm in consum_list:
                if itm.if_play is False and itm.consume_time.year == now.year and itm.consume_time.month == now.month and itm.consume_time.day == now.day:
                    consum = consum_list[i]
                    # print i
                    break
                i += 1
            if consum is not None:
                money = consum.total
                # print money
                if money < 51:
                    content = '''[{"id":0,"prize":"大奖降临：TCL32寸智能液晶电视","v":0.0},{"id":1,"prize":"一等奖：30元百业汇消费券","v":0.0},{"id":2,"prize":"二等奖：10元百业汇消费券","v":0.0},{"id":3,"prize":"三等奖：5元百业汇消费券","v":1.0},{"id":4,"prize":"幸运奖：3角移动话费","v":19.0}]'''
                elif money >= 51 and money < 201:
                    content = '''[{"id":0,"prize":"大奖降临：TCL32寸智能液晶电视","v":0.0},{"id":1,"prize":"一等奖：30元百业汇消费券","v":0.0},{"id":2,"prize":"二等奖：10元百业汇消费券","v":0.0},{"id":3,"prize":"三等奖：5元百业汇消费券","v":8.0},{"id":4,"prize":"幸运奖：3角移动话费","v":7.0}]'''
                elif money >=201 and money < 501:
                    content = '''[{"id":0,"prize":"大奖降临：TCL32寸智能液晶电视","v":0.0},{"id":1,"prize":"一等奖：30元百业汇消费券","v":0.0},{"id":2,"prize":"二等奖：10元百业汇消费券","v":6.0},{"id":3,"prize":"三等奖：5元百业汇消费券","v":5.0},{"id":4,"prize":"幸运奖：3角移动话费","v":4.0}]'''
                elif money >=501 and money < 2001:
                    content = '''[{"id":0,"prize":"大奖降临：TCL32寸智能液晶电视","v":0.0},{"id":1,"prize":"一等奖：30元百业汇消费券","v":6.0},{"id":2,"prize":"二等奖：10元百业汇消费券","v":5.0},{"id":3,"prize":"三等奖：5元百业汇消费券","v":2.0},{"id":4,"prize":"幸运奖：3角移动话费","v":2.0}]'''
                elif money >=2001:
                    content = '''[{"id":0,"prize":"大奖降临：TCL32寸智能液晶电视","v":1.0},{"id":1,"prize":"一等奖：30元百业汇消费券","v":8.0},{"id":2,"prize":"二等奖：10元百业汇消费券","v":5.0},{"id":3,"prize":"三等奖：5元百业汇消费券","v":1.0},{"id":4,"prize":"幸运奖：3角移动话费","v":0.0}]'''
                else:
                    content = '''[{"id":0,"prize":"大奖降临：TCL32寸智能液晶电视","v":0.0},{"id":1,"prize":"一等奖：30元百业汇消费券","v":0.0},{"id":2,"prize":"二等奖：10元百业汇消费券","v":0.0},{"id":3,"prize":"三等奖：5元百业汇消费券","v":0.0},{"id":4,"prize":"幸运奖：3角移动话费","v":0.0}]'''
                return render_to_response('index.html', {'content': content, 'status': '1', 'reward_list': rewardlist})
            else:
                return render_to_response('index.html', {'content': content, 'status': '0', 'reward_list': rewardlist})
        else:
            return render_to_response('index.html', {'content': content, 'status': '0', 'reward_list': rewardlist})


def index(req):
    flag = False
    if req.method == 'GET':
        if not req.session.get('phone'):
            raise Http404
        else:
            phone = req.session['phone']
            consum_list = Consume.objects.filter(phone = phone).order_by('-consume_time')
            now = datetime.datetime.now()
            for itm in consum_list:
                if itm.if_play is False and itm.consume_time.year == now.year and itm.consume_time.month == now.month and itm.consume_time.day == now.day:
                    flag = True
                    itm.if_play = True
                    itm.save()
                    break
            content = str(req.GET['rtype'])
            if content != '-1' and flag:
                reward = ['百业汇公司0.3元手机话费抵用券', '百业汇联盟商家30元通用消费券', '百业汇联盟商家10元通用消费券', '百业汇联盟商家5元通用消费券']
                newreward = Reward()
                newreward.phone = phone
                if content != '10':
                    newreward.content = reward[int(content)]
                else:
                    newreward.content = 'big ward'
                res = sendEleQuan(phone, content)
                newreward.fail_message = res
                newreward.time = datetime.datetime.now()
                newreward.save()
            return render_to_response('index.html', {'content': content, 'status': '0'})
    else:
        raise Http404