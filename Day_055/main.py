from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article = driver.find_elements(By.CSS_SELECTOR, value="#articlecount ul li a")
l1=[]
for items in article:
    l1.append(items.text)
num_of_articles = l1[1]
print("Article Count: ",num_of_articles)
driver.close()

