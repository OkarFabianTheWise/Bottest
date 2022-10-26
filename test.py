import devtools
from selenium import webdriver
import time
import datetime
import telebot

driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\chromium\\chromedriver_win32\\chromedriver.exe")
driver.get("https://coinmarketcap.com/")

def BTC():
    btcname = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[1]/td[3]/div/a').text
    btcprice = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[1]/td[4]').text
    btc24hours = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[1]/td[6]').text
    btc7days =driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div/div[5]/table/tbody/tr[1]/td[7]/span').text
    print(btcname,btcprice,btc24hours,btc7days)

    while True:
        try:
            time.sleep(1)
            BTC()
        except Exception as e:
            driver.quit()   
            break 
