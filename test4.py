#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
import time

print("Start vDisplay")
# Set screen resolution to 1366 x 768 like most 15" laptops
display = Display(visible=0, size=(1000, 1000))
display.start()
print("vDisplay started")

# now Firefox will run in a virtual display.
print("Get size")
browser = webdriver.Firefox()
browser.set_window_size(1900, 1080)
browser.get("https://dodocontrol.ru/checks")

# set timeouts
#browser.set_script_timeout(30)
#browser.set_page_load_timeout(30) # seconds
print("Waiting 30 seconds")
time.sleep(30)
total_height = browser.execute_script("return document.body.parentNode.scrollHeight")
browser.quit()

# now Firefox will run in a virtual display.
print("Open window with new size")
browser = webdriver.Firefox()
browser.set_window_size(1000, 3000)
browser.get("https://dodocontrol.ru/checks")
#el = browser.find_element_by_xpath('//*[@id="anketa"]/div[1]/div[2]/div[2]/div/button')
inputElement = browser.find_element_by_xpath('//*[@id="socialNetworkLink"]')
inputElement.send_keys('https://vk.com/id12867863')


my_choice=browser.find_element_by_xpath('//*[@id="anketa"]/div[1]/div[2]/div[2]/div/button')
my_choice.click()

#rint(el.text)

# Take screenshot
print("Take screenshot")
browser.save_screenshot("dodo.png")

# quit browser
browser.quit()

# quit Xvfb display
display.stop()
