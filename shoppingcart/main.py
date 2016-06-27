
# coding: utf-8

import math
import time
import productit
from productit import *
# 紀錄商品項目

data={}              #存放節日折扣資訊
productList=[]       #存放產品資訊
total=0              #計算金額

dic={"ipad":"電子",
     "iphone":"電子",
     "螢幕":"電子",
     "顯示器":"電子",
     "筆記型電腦":"電子",
     "鍵盤":"電子",
     "麵包":"食品",
     "面包":"食品",
     "餅乾":"食品",
     "蛋糕":"食品",
     "牛肉":"食品",
     "魚":"食品",
     "蔬菜":"食品",
     "餐巾紙":"日用品",
     "收納箱":"日用品",
     "咖啡杯":"日用品",
     "雨傘":"日用品",
     "啤酒":"酒類",
     "白酒":"酒類",
     "伏特加":"酒類",
     
    }

#dic["ipad"]


def salesInformation_(salesInformation):    #將輸入進來的資訊存入字典 (時間,類別):折扣
    try:
        date, discount, category = salesInformation.split("|")
        data[(date,category)] = float(discount)
    except:
        print "Format Error"  
            
def productit_(product):                      #存放購物車資訊

        quantity, product= product.split("*")
        product,price = product.split(":")
        #print product
        productList.append(productit(product,quantity,price,dic[product]))


def date_(date):                            #存放日期(必須輸入)
    if date == '':
        print "Enter Dates"
        verifyDate_(date)
    else:
        try:
            shoppingDay = time.strptime(date, "%Y.%m.%d")
            return shoppingDay
        except:
            print "Format Error" 
            verifyDate_(date)
        
def verifyDate_(date):                     #日期格式出錯時執行
    date = raw_input().strip()
    date_(date)   
    
 


 
#print "請輸入日期|折扣|產品品類，完成後輸入空白鍵結束"
while True: 
    salesInformation = raw_input().strip().decode("big5").encode("utf-8") #輸入資訊
    if salesInformation == '': #空格離開
        break
    else:
        salesInformation_(salesInformation)
            
#print "請輸入：數量*商品:單價，完成後輸入空白鍵結束"
while True:  
    product = raw_input().strip().decode("big5").encode("utf-8") #輸入購物車
    if product == '':   #空格離開
        break
    else:
        productit_(product)



#print "輸入日期"
while True:  
    date = raw_input().strip()  #輸入日期
    shoppingDay = date_(date)
    break
    

#print "輸入優惠卷結束日期與折扣，格式為:日期 滿額 折扣金額" 
while True:  
    discount = raw_input().strip().decode("big5").encode("utf-8")  #輸入優惠卷
    if discount == '':
		cost = "0"
		discountDay =  time.strptime("1000.1.1", "%Y.%m.%d")		
		break
    else:
        try:
            dateDiscount, cost, offerCost  = discount.split()
            discountDay =  time.strptime(dateDiscount, "%Y.%m.%d")
            break
        except:
            print "Format Error"   
        
        
    
for i in productList:                                #計算總金額
    if (date,i.category) in data:
        s = i.totalPrice*data[(date,i.category)]
        total=total+s
    else:
        total=total+i.totalPrice

if shoppingDay <= discountDay:                        #比對優惠卷是否過期
    if total>int(cost):                                    #比對是否符合條件
        print "total:", round(total,2)-int(offerCost)
    else:
        print "total:",round(total,2)
else:
        print "total:",round(total,2)




