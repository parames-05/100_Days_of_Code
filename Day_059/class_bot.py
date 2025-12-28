from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        Cookie_ctn = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        Cookie_ctn.click()

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(39)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        print("Loading Results")
        print(self.up)
        print(self.down)
        self.driver.close()



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
