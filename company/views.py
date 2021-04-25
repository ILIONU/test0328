from django.shortcuts import redirect, render

from member.models import Member

from django.shortcuts import redirect

from datetime import datetime

import requests
import json

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def recommand(request):

    context = {}
    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
    else:
        return redirect('/')

    context["member_no"] = memberno
    context["member_name"] = membername

    import pymysql
    dbCon = pymysql.connect(host='18.221.7.122', user = 'root', password = '1234', db = 'testdb', charset='utf8')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute("SELECT *,(6371*acos(cos(radians(37.2777037))*cos(radians(latitude))*cos(radians(longitude)-radians(127.043012))+sin(radians(37.2777037))*sin(radians(latitude)))) AS distance FROM divisionglass ORDER BY distance")
        distance = cursor.fetchall()

    return render(request, "recommand.html", {
        'title' : '거리정보',
        'dtitle1' : '거리',
        'dtitle2' : '예측',
        'distance' : distance,
        
        })

