from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
WEBSITE="https://appbrewery.github.io/gym/"
ACC_EMAIL="abc@test.com"
ACC_PW="Enter_your_password_here"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(WEBSITE)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
Login_btn= driver.find_element(By.ID,value="login-button")
driver.implicitly_wait(2)
Login_btn.click()
email = driver.find_element(By.ID,value="email-input")
pw= driver.find_element(By.ID, value="password-input")
email.send_keys(ACC_EMAIL)
pw.send_keys(ACC_PW)
driver.implicitly_wait(3)
second_pg_login = driver.find_element(By.ID,value="submit-button")
second_pg_login.click()
