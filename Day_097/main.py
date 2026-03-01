from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://chromedino.com/")

time.sleep(2)
canvas = driver.find_element("tag name", "canvas")
canvas.click()

driver.execute_script("""
    document.dispatchEvent(new KeyboardEvent('keydown', {keyCode: 32}));
""")
driver.execute_script("document.body.style.overflow = 'hidden';")

while True:
    game_state = driver.execute_script("""
        if (Runner.instance_ && Runner.instance_.horizon.obstacles.length > 0) {
            const obstacle = Runner.instance_.horizon.obstacles[0];
            return {
                xPos: obstacle.xPos,
                yPos: obstacle.yPos,
                width: obstacle.width,
                speed: Runner.instance_.currentSpeed,
                type: obstacle.typeConfig.type
            };
        }
        return null;
    """)

    if game_state:
        x_pos = game_state['xPos']
        y_pos = game_state['yPos']
        speed = game_state['speed']

        jump_threshold = speed * 15

        if x_pos < jump_threshold:
            if game_state['type'] == 'PTERODACTYL' and y_pos < 80:
                driver.execute_script("""
                    document.dispatchEvent(new KeyboardEvent('keydown', {keyCode: 40}));
                """)
                time.sleep(0.2)
                driver.execute_script("""
                    document.dispatchEvent(new KeyboardEvent('keyup', {keyCode: 40}));
                """)
            else:
                driver.execute_script("""
                    document.dispatchEvent(new KeyboardEvent('keydown', {keyCode: 32}));
                """)

    time.sleep(0.005)