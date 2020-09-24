"""
This code is written by
AMAN KAZI
"""

from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver.exe')
for x in range(20):
	browser.get('https://www.facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar')

	number=browser.find_element_by_xpath('//*[@id="identify_email"]')

	did_submit=browser.find_element_by_name('did_submit')

	number.send_keys('Enter mobile number here')
	did_submit.click()
	time.sleep(5)
	submit=browser.find_element_by_xpath('//*[@id="initiate_interstitial"]/div[3]/div/div[1]/button')
	submit.click()
	time.sleep(3)