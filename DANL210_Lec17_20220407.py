#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 23:27:29 2022

@author: byeong-hakchoe
"""


# for-loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
for x in range(5):
  print(x)
  
for x in range(1, 5):
  print(x)

# while-loop
i = 1
while i < 6:
  print(i)
  i = i + 1
  
# if-conditional
a = 33; b = 200
if b > a:
  print("b is greater than a")
  
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# finding web elements
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep

driver = webdriver.Chrome("/Users/byeong-hakchoe/Downloads/chromedriver")

url = "https://qavbox.github.io/demo/webtable/"
driver.get(url)

# html code
html = driver.page_source

# find by id
form = driver.find_element_by_id('form1')
form.text

# find by class name
home_button = driver.find_element_by_class_name('homebtn')
home_button.click()
driver.back()
# driver.forward()

# find by name
home_button2 = driver.find_element_by_name('home')
home_button2.text


# find by css selector
home_button3 = driver.find_element_by_css_selector("body > div > a > input")
home_button3.click()
driver.back()


# find by tag name
table01 = driver.find_element_by_id("table01")
thead = table01.find_element_by_tag_name("thead")
thead.text



# find by link text
selenium_link = driver.find_element_by_link_text("Selenium")
selenium_link.click()


# find by partial link text
selen_links = driver.find_elements_by_partial_link_text("Selen")
print(len(selenium_links))



# find by xpath
elt = driver.find_element_by_xpath('//*[@id="table02"]/tbody/tr[1]/td[1]')
elt.text



# table by xpath
nrows = driver.find_elements_by_xpath('//*[@id="table02"]/tbody/tr')
nrows = len(nrows)

df = pd.DataFrame()
for i in range(1, nrows+1):
    name = driver.find_element_by_xpath('//*[@id="table02"]/tbody/tr['+str(i)+']/td[1]').text
    name = pd.DataFrame([name])
    # name.columns = ['name']  
    position = driver.find_element_by_xpath('//*[@id="table02"]/tbody/tr['+str(i)+']/td[2]').text
    position = pd.DataFrame([position])
    office = driver.find_element_by_xpath('//*[@id="table02"]/tbody/tr['+str(i)+']/td[3]').text
    office = pd.DataFrame([office])
    age = driver.find_element_by_xpath('//*[@id="table02"]/tbody/tr['+str(i)+']/td[4]').text
    age = pd.DataFrame([age])
    start_date = driver.find_element_by_xpath('//*[@id="table02"]/tbody/tr['+str(i)+']/td[5]').text
    start_date = pd.DataFrame([start_date])
    salary = driver.find_element_by_xpath('//*[@id="table02"]/tbody/tr['+str(i)+']/td[6]').text
    salary = pd.DataFrame([salary])
    data = pd.concat([name, position, office, age, start_date, salary], axis=1) 
    df = df.append(data)


# table header by xpath
ncols = driver.find_elements_by_xpath('//*[@id="table02"]/thead/tr/th')
ncols = len(ncols)

header = []
for i in range(1, ncols+1):
    head = driver.find_element_by_xpath('//*[@id="table02"]/thead/tr/th['+str(i)+']').text
    header.append(head)

df.columns = header
df.to_csv("/Users/byeong-hakchoe/Google Drive/SUNY_Geneseo/teaching-materials/lecture_data/table_example_20220407.csv")     

