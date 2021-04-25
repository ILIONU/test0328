from django.shortcuts import render
#from album.models import Album
from django.shortcuts import redirect

from django.core.files.storage import FileSystemStorage
import datetime
import random
import sys, os

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def chart_bar(request):

    context = {}
    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
    else:
        return redirect('/')

    context["member_no"] = memberno
    context["member_name"] = membername

    return render(request, "chart_bar.html", {
    })


def chart_bar2(request):
    

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
        cursor.execute("SELECT yyyymm, sales_amt, sales_predict FROM sales_predict")
        rsSales = cursor.fetchall()

    return render(request, "chart_bar2.html", {
        'title' : '판매 예측',
        'dtitle1' : '실적',
        'dtitle2' : '예측',
        'rsSales' : rsSales
    })


def chart_bar3(request):



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
        cursor.execute("SELECT date, total, paper, can, plastic_etc1 FROM suwontrash_1")
        rsSales = cursor.fetchall()

    return render(request, "chart_bar3.html", {
        'title' : '쓰레기 배출량',
        'dtitle1' : '전체',
        'dtitle2' : '종이',
        'dtitle3' : '캔',
        'dtitle4' : '플라스틱',
        'rsSales' : rsSales
    })

def data_analysis1(request):

    context = {}
    if request.session.has_key('member_no'):
        memberno = request.session['member_no']
        membername = request.session['member_name']
    else:
        return redirect('/')

    context["member_no"] = memberno
    context["member_name"] = membername


    file_path = 'csv_files\drinks.csv'
    drinks = pd.read_csv(file_path)
    corr = drinks[['beer_servings', 'wine_servings']].corr(method = 'pearson')
    print(corr)
    
    context ={ "object" :corr }


    
    return render(request, "data_analysis1.html", context)