from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.taobao.com/")
driver.find_element_by_xpath("//*[@id='q' and @name='q']").send_keys("电脑")
driver.find_element_by_xpath("//*[@class='btn-search tb-bg' and @type='submit']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='fm-login-id' and @type='text']").send_keys("13131215003")
driver.find_element_by_xpath("//*[@id='fm-login-password' and @type='password']").send_keys("cyz1999828456789")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='q' and @name='q']").send_keys("电脑")
driver.find_element_by_xpath("//*[@class='btn-search tb-bg' and @type='submit']").click()


























