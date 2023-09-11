from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import datetime
import time

def get_driver():
    # Set options to make browsing easier
    options = webdriver.EdgeOptions()
    options.use_chromium = True  # Use the Chromium-based version of Edge
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Edge(options=options)
    driver.get('https://www.google.com/search?q=yahoo+finance&oq=yah&aqs=chrome.3.69i57j46i67i131i199i433i465i650j0i67i131i433i650l2j69i60l3j5.2046j0j7&sourceid=chrome&ie=UTF-8')
    return driver

# Rest of your code remains the same
def main():
    driver = get_driver()
    driver.find_element(by="xpath",value="/html/body/div[6]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/a/h3").click()
    time.sleep(2)
    search_bar = driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/form/input[1]")
    search_bar.click()
    search_bar.send_keys('Apple')
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div/form/button[2]").click()
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[7]/div/div/section/div/ul/li[4]/a").click()
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[2]/span[2]/a").click()
    time.sleep(2)
    print('Finally some progress')
    
    
main()
