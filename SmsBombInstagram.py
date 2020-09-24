"""
This code is written by
AMAN KAZI
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 
import time


chrome_options = Options()
# chrome_options.add_argument("headless")
browser = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
for x in range(100):
	browser.get("https://www.instagram.com/accounts/password/reset/")
	element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "cppEmailOrUsername")))
	
	number = browser.find_element_by_name('cppEmailOrUsername')
	send = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div[2]/div/div/div[5]/button')
	number.send_keys("enter the phone number here")
	print(x)
	send.click()
	time.sleep(1)