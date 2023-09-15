from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import random
import os

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)
time.sleep(3)
driver.get("https://play.google.com/store/apps?hl=en&gl=US")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="kO001e"]/header/nav/div/div[1]').click() #click on search icon
time.sleep(2)
search_box = driver.find_element_by_xpath('//*[@id="kO001e"]/header/nav/c-wiz/div/div/label/input') 
search_box.send_keys("Files Go") #replace with your app name
search_box.send_keys(Keys.RETURN)
time.sleep(3)
search_box = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[3]/div/div/c-wiz/c-wiz[1]/c-wiz/section/div/div').click() #click on text element
time.sleep(5)
driver.find_element_by_css_selector("#yDmH0d > c-wiz:nth-child(9) > div > div > div.tU8Y5c > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > div > div.H6372c > div.bkJP6e > div > div > button > span").click() #write on review
time.sleep(3)
driver.find_element_by_css_selector("#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div > div:nth-child(3) > div:nth-child(3) > div.DfQkVd > div:nth-child(1) > div.mxqmcd > div > span:nth-child(5)").click() #click on 5 star
time.sleep(3)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[5]/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div/span[5]').click() #click on 5 star
time.sleep(4)
driver.find_element_by_css_selector("#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div > div:nth-child(3) > div:nth-child(2) > div > label").send_keys("files go very rare app without ads") #describe your experience(replace with your needed text)
time.sleep(3)
driver.find_element_by_css_selector('#yDmH0d > div.VfPpkd-Sx9Kwc.cC1eCc.UDxLd.PzCPDd.HQdjr.VfPpkd-Sx9Kwc-OWXEXe-FNFY6c > div.VfPpkd-wzTsW > div > div > div > div > div:nth-child(3) > div > div > div > button > span').click() #submit button
time.sleep(6)
#just created code For Where Its Run Or Not That It..
