from urllib import request
from selenium import webdriver
import cv2
import random
import time
import pyautogui

driver = webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("电脑")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[10]/div/ul/li[1]/div/div/div[2]/div[2]/a").click()
time.sleep(1)
data = driver.window_handles
driver.switch_to.window(data[1])
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div[13]/a[3]").click()
time.sleep(2)
driver.quit()
