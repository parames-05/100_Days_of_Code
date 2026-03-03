from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------- CONFIG ----------------
URL = "ENTER_URL_HERE"
MAX_SLOTS = 15
# ----------------------------------------

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get(URL)
    book_button = wait.until(
        EC.element_to_be_clickable((By.ID, "openBookingBtn"))
    )
    book_button.click()
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "calendarCell"))
    )
    date_cells = driver.find_elements(By.CLASS_NAME, "calendarCell")

    booked_count = 0

    for cell in date_cells:
        if cell.text.strip() != "":
            driver.execute_script("arguments[0].scrollIntoView(true);", cell)
            time.sleep(0.2)
            cell.click()
            booked_count += 1

            if booked_count == MAX_SLOTS:
                break

    print(f"{booked_count} slots booked successfully.")
    time.sleep(2)

finally:
    driver.quit()
    print("Driver closed.")