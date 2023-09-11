#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import datetime
import time


"""Need to work on this"""

service = Service

def get_driver():
    #set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/')
    return driver

'''def clean_text(text):
    #Only get the digits
    output = float(text.split(': ')[1])
    return str(output)'''
    

def main():
    driver = get_driver()
    time.sleep(2)
    #google--> search for facebook and entering
    driver.find_element(by="xpath",value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("facebook" + Keys.RETURN)
    time.sleep(2)
    #clicking on facebook link on google
    driver.find_element(by="xpath",value="/html/body/div[6]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3").click()
    time.sleep(2)
    #filling in email
    driver.find_element(by='id', value="email").send_keys("XXXXXXX@hotmail.com")
    time.sleep(2)
    #filling in pw
    driver.find_element(by='id', value="pass").send_keys("XXXXXX" + Keys.RETURN)
    time.sleep(2)
    #writing something and posting it
    driver.find_element(by='xpath',value="/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span").click()
    time.sleep(2)
    #choosing who can see message
    #driver.find_element(by='xpath',value="/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[4]/div/div[1]/div[2]/div[1]/div/div/div/span").click()
    #time.sleep(2)
    #typing message
    driver.find_element(by="xpath",value="/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div").send_keys("testing")
    time.sleep(2)
    #clicking post 
    driver.find_element(by='xpath',value="/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div").click()
    time.sleep(2)
    
    time.sleep(5)
    
    # Rest of your script
    
    #return clean_text(element.text)
    
main()

    