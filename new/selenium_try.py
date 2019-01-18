#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
import time
from bs4 import BeautifulSoup as BS
import datetime
import requests

default_width = 1900
default_height = 1080

print(">> Start in... "+datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

# Set screen resolution to 1366 x 768 like most 15" laptops
display = Display(visible=0, size=(default_width, default_height))
display.start()

# now Firefox will run in a virtual display.
browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
browser.set_window_size(default_width, default_height)
browser.get("https://dodocontrol.ru/checks")

inputElement = browser.find_element_by_xpath('//*[@id="socialNetworkLink"]')
inputElement.send_keys('https://vk.com/id')

my_choice=browser.find_element_by_xpath('//*[@id="anketa"]/div[1]/div[2]/div[2]/div/button')
my_choice.click()

# set timeouts
print("Waiting 20 seconds")
time.sleep(20)
total_height = browser.execute_script("return document.body.parentNode.scrollHeight")
browser.quit()

# now Firefox will run in a virtual display.
print("Open window with new size")
browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
browser.set_window_size(default_width, total_height)
browser.get("https://dodocontrol.ru/checks")

#el = browser.find_element_by_xpath('//*[@id="anketa"]/div[1]/div[2]/div[2]/div/button')
inputElement = browser.find_element_by_xpath('//*[@id="socialNetworkLink"]')
inputElement.send_keys('https://vk.com/id')

my_choice=browser.find_element_by_xpath('//*[@id="anketa"]/div[1]/div[2]/div[2]/div/button')
my_choice.click()

html = browser.page_source
filename = "/home/toptop/git/selenium/dodo_body/dodo_"+datetime.datetime.now().strftime("%d-%m-%Y_%H%M")+".html"

with open(filename, 'w') as out_file:
    out_file.write(html)
soup = BS(html, 'html.parser')
for cell in soup.find("div",{"id":"delivery_calendar"}).findAll("td"):
    if cell.get("class")[0] not in ("blocked-day","inactive-day"):
        url = 'https://sms.ru/sms/send'
        data = ({'api_id':'id', 'to':'phone_number', 'msg':'Available day in operations!!!!'})
        r = requests.post(url, data=data)

browser.quit()
display.stop()

print(">> End in... "+datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
