from urllib import request
from selenium import webdriver
import cv2
import random
import time
import pyautogui

driver = webdriver.Chrome()

# 京东
driver.get("https://www.jd.com")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id = 'key' and @type = 'text']").send_keys("电脑")
driver.find_element_by_xpath("//*[@class = 'button' and @aria-label='搜索']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[2]/div").click()

data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]").click()
driver.find_element_by_xpath("//*[@id = 'loginname' and @type = 'text']").send_keys("13131215003")
driver.find_element_by_xpath("//*[@id = 'nloginpwd' and @type = 'password']").send_keys("cyz1999828456789")
driver.find_element_by_xpath("//*[@id = 'loginsubmit']").click()

