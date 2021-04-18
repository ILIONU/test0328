from django.shortcuts import render
#from album.models import Album
from django.shortcuts import redirect

from django.core.files.storage import FileSystemStorage
import datetime
import random
import sys, os

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

def chart_bar(request):
    
    return render(request, "chart_bar.html", {
    })


def chart_bar2(request):

    import pymysql
    dbCon = pymysql.connect(host='18.221.7.122', user = 'root', password = '1234', db = 'suwon_trash', charset='utf8')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute("SELECT yyyymm, sales_amt, sales_predict FROM sales_predict")
        rsSales = cursor.fetchall()

    return render(request, "chart_bar2.html", {
        'title' : '판매 예측',
        'dtitle1' : '실적',
        'dtitle2' : '예측',
        'rsSales' : rsSales
    })


def chart_bar3(request):

    import pymysql
    dbCon = pymysql.connect(host='18.221.7.122', user = 'root', password = '1234', db = 'suwon_trash', charset='utf8')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute("SELECT date, total, paper, can, plastic_etc1 FROM suwontrash_1")
        rsSales = cursor.fetchall()

    return render(request, "chart_bar3.html", {
        'title' : '쓰레기 배출량',
        'dtitle1' : '전체',
        'dtitle2' : '종이',
        'dtitle2' : '캔',
        'dtitle2' : '플라스틱',
        'rsSales' : rsSales
    })