from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
butn = driver.find_element(By.CLASS_NAME, value="btn" )
fname.send_keys("Parames")
lname.send_keys("M V")
email.send_keys("asdfghj@gmail.com")
time.sleep(1.5)

butn.click()
