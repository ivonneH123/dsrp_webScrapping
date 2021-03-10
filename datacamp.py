from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import ActionChains

#import beautifulsoup

PATH= "D:/Ivonne/Downloads/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(executable_path=PATH)

driver.get("https://www.datacamp.com")

element = WebDriverWait(driver, 20).until( 
        EC.presence_of_element_located((By.LINK_TEXT,'Sign In' )))
element.click()