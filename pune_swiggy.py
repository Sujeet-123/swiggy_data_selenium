from ast import IsNot
from unicodedata import name
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import google_sheet_api

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.swiggy.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(6)










# s = Service("/home/zec/Downloads/chromedriver")
# driver = webdriver.Chrome(service=s)

# driver.get("https://www.swiggy.com/")
# time.sleep(5)
# driver.maximize_window()
# time.sleep(6)

var = "Pune, Maharashtra, India"
driver.find_element(By.ID,'location').send_keys(var)
time.sleep(5)
driver.find_element(By.CLASS_NAME,'_2W-T9').click()
time.sleep(8)

links_list = []

time.sleep(5)
# driver.execute_script('scrollTo(0,500)')

# time.sleep(8)




def get_links():
    a = 0
    b = 400
    for i in range(1000):
        print("loop => ",i)
        driver.execute_script(f'scrollTo({a},{b})')
        time.sleep(3)
        a = b
        b = b+150
     

    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
    time.sleep(10)


    links = driver.find_elements(By.CLASS_NAME,'_3XX_A a')
    print(len(links))
    n = 1
    for i in links:
        link = i.get_attribute("href")
        links_list.append(link)
        print("Number of links = ",n)
        n = n+1 

        time.sleep(1)
        
        print(link)
    print(len(links_list))



def Data():

    try:
        name = driver.find_element(By.CLASS_NAME,'_3aqeL').text
        print("Name => ",name)
    except:
        name = None
    

    try:
        address = driver.find_element(By.CLASS_NAME,'Gf2NS._2Y6HW._2x0-U').text
        print("Address name => ",address)
    except:
        address = None

    try:
        ratings = driver.find_element(By.CLASS_NAME,'_2l3H5')
        rating = ratings.find_element(By.TAG_NAME,'span').text
        print("Rating => ",rating)
    except:
        rating = None

    try:
        delivery_time = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/div[1]/span').text
        print("delivery_time => ",delivery_time)
    except:
        delivery_time = None


    m=[]
    D_Name = []
    divs = driver.find_elements(By.CLASS_NAME,'styles_detailsContainer__22vh8')
    for div in divs:
        Down_list = []
        try:
            Dname = div.find_element(By.CLASS_NAME,'styles_itemNameText__3ZmZZ').text
            Down_list.append(Dname)
            print("Dname => ",Dname)
        except:
            Dname = None
            Down_list.append(Dname)

        try:
            DDprice = div.find_element(By.CLASS_NAME,'styles_price__2xrhD.styles_itemPrice__1Nrpd.styles_s__66zLz')
            Dprice = DDprice.find_element(By.TAG_NAME,'span').text

            Down_list.append(Dprice)
            print("Dprice => ",Dprice)
        except:
            Dprice = None
            Down_list.append(Dprice)

        try:
            Ddiscrib = div.find_element(By.CLASS_NAME,'styles_itemDesc__3vhM0').text
            Down_list.append(Ddiscrib)
            print("Ddiscrib => ",Ddiscrib)
        except:
            Ddiscrib = None
            Down_list.append(Ddiscrib)


        try:
            bestseller  = div.find_element(By.CLASS_NAME,'styles_ribbon__3tZ21.styles_itemRibbon__353Fy').text
            Down_list.append(bestseller)
            print("votes => ",bestseller)
        except:
            bestseller = None
            Down_list.append(bestseller)


        
        D_Name.append(Down_list)


    for i, n in enumerate(D_Name):
        if n not in m:
            m.append(n)

    f_D_data = []

    f_D_data.append(m)
    print("lenth of m => ",len(m))
    print("lenth of D_name => ",len(D_Name))  
    # print(m)  
    value1 = [name, address,rating, delivery_time, str(f_D_data)]
    google_sheet_api.append_googlesheet2(value1)



def click():
    for i in links_list:
        driver.get(i)
        time.sleep(15)
       
        
        Data()


get_links()
click()