"""
This code is written by
AMAN KAZI
"""

from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver.exe')
for x in range(20):
	browser.get('https://twitter.com/account/begin_password_reset')

	email=browser.find_element_by_xpath('/html/body/div[2]/div/form/input[2]')

	did_submit=browser.find_element_by_xpath('/html/body/div[2]/div/form/input[3]')

	email.send_keys('Enter email address here')
	did_submit.click()
	time.sleep(5)
	submit=browser.find_element_by_xpath('/html/body/div[2]/div/form/input[2]')
	submit.click()
	time.sleep(3)