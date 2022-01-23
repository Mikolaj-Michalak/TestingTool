from selenium.webdriver.common.by import By
import time

def open_next_rules_page(driver):
    canvas = driver.find_element(By.TAG_NAME, "body")
    canvas.send_keys("i")
    time.sleep(0.5)

def wait_for_game_load(driver):
    for i in range(30):
        time.sleep(1)
        if(driver.execute_script("return window.debugAPI.isGameLoaded")):
            break
    
    time.sleep(2)