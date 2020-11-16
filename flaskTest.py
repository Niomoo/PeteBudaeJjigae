#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 引入模組
import pymysql
import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import copy
import random
from flask import Flask

app = Flask(__name__)

# 連接資料庫
conn = pymysql.connect("127.0.0.1", port=3306, user="root", passwd="",db="tourism1")
cursor = conn.cursor()

# 抓DB資料存成list或dict
cursor.execute("select * from attraction")
res = cursor.fetchall()
attraction = pd.DataFrame(list(res))
cursor.execute("select * from mrt")
res = cursor.fetchall()
mrt = pd.DataFrame(list(res))
cursor.execute("select * from arelated")
res = cursor.fetchall()
arelated = pd.DataFrame(list(res))
cursor.execute("select * from mrelated")
res = cursor.fetchall()
mrelated = pd.DataFrame(list(res))
cursor.execute("select * from tags")
res = cursor.fetchall()
tags = pd.DataFrame(list(res))

attraction.set_index(attraction[0], drop=True, inplace=True)
attraction = attraction.to_dict(orient='index')
mrt.set_index(mrt[0], drop=True, inplace=True)
mrt = mrt.to_dict(orient='index')
arelated = arelated.values
mrelated = mrelated.values
tags = tags.values

@app.route('/')
def hollo():
    return "hello flask"

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

@app.route('/findAllViewpoint/userInput=<userInput>', methods=['GET'])
def findAllViewpoints(userInput):
    viewList = {}
    cursor.execute("select aId,aName from attraction where aName like '%" + userInput + "%'")
    res = cursor.fetchall()
    for (row1,row2) in res:
        viewList[row1] = row2
    if len(viewList) == 0:
        cursor.execute("select mId from mrt where mName like '%" + userInput + "%'")
        res = cursor.fetchone()
        for i in res:
            cursor.execute("select aId,aName,mrtId,dist from attraction where mrtId = " + str(i))
            res = cursor.fetchall()
            min = 10000
            for (r1,r2,m,d) in res:
                if d < min:
                    min = d
                    aId = int(r1)
                    aName = r2
                    mrtId = m
            viewList[aId] = aName
            checkMrt.append(mrtId)
            checkMrt.append(aId)
    return viewList

@app.route('/findNearestViewpoint/lng=<lng>&lat=<lat>', methods=['GET'])
def findNearestViewpoint(lng, lat):
    minDist = 10000
    minId = 1
    for i in attraction:
        d = haversine(float(lng), float(lat), attraction[i][6], attraction[i][5])
        if d < minDist:
            minDist = d
            minId = i
    return minId

def text(view, attraction, arelated, aList, aWeight, isTag):
    b = 0
    # 非第一個景點，可能需要關聯
    if len(view) > 1: 
        tmp = []
        for i in arelated:
            if int(i[2]) == view[len(view)-1]:
                tmp.append(i[1])
        for i in arelated:
            if (int(i[2]) == view[len(view)-2]) and (i[1] in tmp) and (int(i[3]) in isTag) and (int(i[3]) not in allList) and (int(i[3]) not in view):
                aList[int(i[3])] = i[6]
                b = 1
    if b == 0:
        for i in arelated:
            if (int(i[2]) == view[len(view)-1]) and (int(i[3]) in isTag) and (int(i[3]) not in allList) and (int(i[3]) not in view):
                aList[int(i[3])] = i[6]
    
    # 計算view[0]跟aList景點的距離
    for i in aList:
        dist = haversine(attraction[view[len(view)-1]][6], attraction[view[len(view)-1]][5], attraction[i][6], attraction[i][5])
        if dist != 0:
            aList[i] = (1/dist) * aList[i] * aWeight * attraction[i][9]

def nearby(view, attraction, aList, dWeight, isTag, mList):
    nearMrt = attraction[view[len(view)-1]][7]
    mList.append(nearMrt)
    for i in attraction:
        if (attraction[i][7] == nearMrt) and (i not in allList) and (i not in view)  and (i in isTag):
            dist = haversine(attraction[view[len(view)-1]][6], attraction[view[len(view)-1]][5], attraction[i][6], attraction[i][5])
            if dist != 0:
                if i in aList:
                    aList[i] = aList[i] + (1/dist) * dWeight * attraction[i][9]
                else:
                    aList[i] = (1/dist) * dWeight * attraction[i][9]

def data(view, attraction, mrelated, aList, mWeight, isTag, mList, isMrt):
    b = 0
    nextMrt = {}
    # 前一個景點來自可能三，可能需要關聯
    if len(mList) > 1: 
        tmp = []
        for i in mrelated:
            if i[2] == mList[len(mList)-1]:
                tmp.append(i[1])
        for i in mrelated:
            if (i[2] == mList[0]) and (i[1] in tmp) and (i[3] not in mList):
                nextMrt[int(i[3])] = i[6]
                b = 1
    if b == 0:
        for i in mrelated:
            if (i[2] == mList[len(mList)-1]) and (i[3] not in mList):
                nextMrt[int(i[3])] = i[6]
    
    # 關聯後捷運站的附近景點
    for i in nextMrt:
        for j in attraction:
            if (attraction[j][7] == i) and (j not in allList) and (j not in view) and (j in isTag):
                isMrt[j] = i
                # 景點間的距離用經緯度計算
                dist = haversine(attraction[view[len(view)-1]][6], attraction[view[len(view)-1]][5], attraction[j][6], attraction[j][5])
                # 距離用景點跟捷運站間的距離計算
                # dist = attraction[j][8]
                if dist != 0:
                    if j in aList:
                        aList[j] = aList[j] + (1/dist) * nextMrt[i] * mWeight * attraction[j][9]
                    else:
                        aList[j] = (1/dist) * nextMrt[i] * mWeight * attraction[j][9]

@app.route('/firstRecommend/start=<start>&tag=<tag>', methods=['GET'])
def firstRecommend(start, tag):
    mList = []              #紀錄計算過程中有用到的捷運站
    view = []               #暫存上一個點
    aList = {}              #暫存景點結果（景點id+加權後分數）
    route = []              #回傳所有路線
    start = int(start)
    if len(checkMrt) > 0:
        start = checkMrt[0]
        for i in range(5):
            result[i].append(mrt[start][1])
            resId[i].append(start)
            allList.append(start)
    else:
        for i in range(5):               #第一層景點（使用者輸入的）
            result[i].append(attraction[start][1])
            resId[i].append(start)
            allList.append(start)
    tag = [n for n in inputTags.split()] #記錄所有tag
    if len(tag) != 0:                    #有輸入tag
        for i in tags:
            if i[2] in tag:
                isTag.append(i[1])
    else:                                #沒有指定tag，故所有景點都會考慮
        for i in attraction:
            isTag.append(i)

    # 計算每條路線的第二個點
    view.append(start)
    
    if len(checkMrt) > 0:
        start = checkMrt[1]
    text(view, attraction, arelated, aList, aWeight, isTag)
    nearby(view, attraction, aList, dWeight, isTag, mList)
    data(view, attraction, mrelated, aList, mWeight, isTag, mList, isMrt)
    resList = sorted(aList.items(), key=lambda item: item[1], reverse=True)
    copyOfmList = copy.copy(mList)

    for i in range(5):
        if len(resList) > i:
            result[i].append(attraction[resList[i][0]][1])
            resId[i].append(resList[i][0])
            allList.append(resList[i][0])

        # 計算每條路線的第三個點
        view = []
        aList = {}
        view.append(start)
        if len(resList) > i:
            view.append(resList[i][0])
            mList = copy.copy(copyOfmList)
            if resList[i][0] in isMrt:
                mList.append(isMrt[resList[i][0]])

            text(view, attraction, arelated, aList, aWeight, isTag)
            nearby(view, attraction, aList, dWeight, isTag, mList)
            data(view, attraction, mrelated, aList, mWeight, isTag, mList, isMrt)

        if len(aList) != 0:
            maxScore = max(aList, key=aList.get)
            result[i].append(attraction[maxScore][1])
            resId[i].append(maxScore)
            allList.append(maxScore)
        if len(result[i]) > 1:
            tmpStr = " ".join(result[i])
            route.append(tmpStr)
            print(result[i])
        else:
            route.append("查無景點路線")
            print("查無景點路線")
    
    routeStr = ",".join(route)
    return routeStr

def changeTheSecond(resId, index, view, aList, maxDist):
    # 可能一（文字關聯）
    tmp = []
    tmp1 = []
    for i in arelated:
        if int(i[2]) == view[0]:
            tmp1.append(i[1])
        if (int(i[3]) == view[1]) and (i[1] in tmp1):
            tmp.append(i[1])
    for i in arelated:
        if (i[1] in tmp) and (int(i[2]) in isTag) and (int(i[2]) not in view):
            aList[int(i[2])] = i[6]
    
    for i in aList:
        dist = haversine(attraction[view[0]][6], attraction[view[0]][5], attraction[i][6], attraction[i][5])
        if (dist != 0) and (dist <= maxDist):
            aList[i] = (1/dist) * aList[i] * aWeight * attraction[i][9]
    
    # 可能二（距離最近捷運站附近之景點）
    nearMrt1 = attraction[view[0]][7]
    for i in attraction:
        if (attraction[i][7] == nearMrt1) and (i not in view)  and (i in isTag):
            dist = haversine(attraction[view[0]][6], attraction[view[0]][5], attraction[i][6], attraction[i][5])
            if (dist != 0) and (dist <= maxDist):
                if i in aList:
                    aList[i] = aList[i] + (1/dist) * dWeight * attraction[i][9]
                else:
                    aList[i] = (1/dist) * dWeight * attraction[i][9]
                   
    # 可能三（捷運關聯）
    nearMrt2 = attraction[view[1]][7]
    tmp2 = []
    tmp3 = [] 
    nextMrt = {}
    for i in mrelated:
        if i[2] == nearMrt1:
            tmp2.append(i[1])
        if (i[3] == nearMrt2) and (i[1] in tmp2):
            tmp3.append(i[1])
    for i in mrelated:
        if (i[1] in tmp3) and (i[2] != nearMrt1):
            nextMrt[int(i[2])] = i[6]
    
    for i in nextMrt:
        for j in attraction:
            if (attraction[j][7] == i) and (j not in view) and (j in isTag):
                dist = haversine(attraction[view[0]][6], attraction[view[0]][5], attraction[j][6], attraction[j][5])
                if (dist != 0) and (dist <= maxDist):
                    if j in aList:
                        aList[j] = aList[j] + (1/dist) * nextMrt[i] * mWeight * attraction[j][9]
                    else:
                        aList[j] = (1/dist) * nextMrt[i] * mWeight * attraction[j][9]
    
    # 選擇更換景點
    if resId[index][1] in aList:
        del aList[resId[index][1]]
    if len(aList) == 0:
        print("沒有更好的景點了！")
        print(result[index])
    else:
        aNew, scoreNew = random.choice(list(aList.items()))
        resId[index][1] = aNew                    
        result[index][1] = attraction[aNew][1]
        print(attraction[aNew][1])
        print(result[index])
        
def changeTheLast(resId, index, view, aList, mList):
    text(view, attraction, arelated, aList, aWeight, isTag)
    nearby(view, attraction, aList, dWeight, isTag, mList)
    data(view, attraction, mrelated, aList, mWeight, isTag, mList, isMrt)
    
    if resId[index][2] in aList:
        del aList[resId[index][2]]
    if len(aList) == 0:
        print("沒有更好的景點了！")
        print(result[index])
    else:
        # 隨機取本次計算的值，只會跟上次不一樣，多次嘗試下來可能換到重覆景點
        aNew, scoreNew = random.choice(list(aList.items()))
        resId[index][2] = aNew                  #紀錄新景點id                    
        result[index][2] = attraction[aNew][1]  #紀錄新景點名稱
        print(attraction[aNew][1])              #印出更新後的景點
        print(result[index])                    #印出更新後的該條路線
        
@app.route('/changePoint/changeIndex=<changeIndex>&change=<change>', methods=['GET'])
def changePoint(changeIndex, change):
    index = int(changeIndex)
    change = int(change)
    view = []
    mList = []
    aList = {}
    view.append(resId[index][0])
    if change == 1:
        view.append(resId[index][2])
        maxDist = haversine(attraction[view[0]][6], attraction[view[0]][5], attraction[view[1]][6], attraction[view[1]][5])
        changeTheSecond(resId, index, view, aList, maxDist)
    elif change == 2:
        view.append(resId[index][1])
        changeTheLast(resId, index, view, aList, mList)
    
    resTmp = ",".join(result[index])
    return resTmp

@app.route('/addPoint/addIndex=<addIndex>', methods=['GET'])
def addPoint(addIndex):
    index = int(addIndex)
    mList = []
    aList = {}

    text(resId[index], attraction, arelated, aList, aWeight, isTag)
    nearby(resId[index], attraction, aList, dWeight, isTag, mList)
    data(resId[index], attraction, mrelated, aList, mWeight, isTag, mList, isMrt)

    if len(aList) == 0:
        print("沒有更好的景點了！")
        print(result[index])
    elif len(resId[index]) < 6:
        maxScore = max(aList, key=aList.get)
        result[index].append(attraction[maxScore][1])
        resId[index].append(maxScore)
        print(attraction[maxScore][1])  #輸出本次新增景點
        print(result[index])            #輸出最終路線
    else:
        print("已達景點數上限！")
        print(result[index])
    
    resTmp = ",".join(result[index])
    return resTmp

# 隨輸入更改之參數
userInput = "高雄車站"       #使用者輸入關鍵字找出最近景點
lng = float(125)        #定位使用者經度
lat = float(23)         #定位使用者緯度
start = 1293            #起始景點id
inputTags = "自然風景"   #選擇tag
aWeight = 0.2           #文字關聯權重
dWeight = 0.5           #距離計算權重
mWeight = 0.3           #捷運關聯權重
changeIndex = 0         #以result第1筆作為更改範例
change = 2              #1->替換第二個點；2->替換第三個點
addIndex = 0            #以result第一筆作為更改範例

# 變數宣告
checkMrt =[]                         #判斷使用者是否輸入捷運站作為關鍵字
result = [[] for i in range(5)]      #紀錄最後路線結果
resId = [[] for i in range(5)]       #紀錄最後路線結果id
allList = []                         #記錄景點id（判斷用）
isTag = []                           #紀錄符合tag的景點們
copyOfmList = []                     #紀錄最初捷運站（跑後面的路線會用到）
resList = []                         #暫存排序後的結果
isMrt = {}                           #暫存如果是來自可能三的結果（會影響到mList）

if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




