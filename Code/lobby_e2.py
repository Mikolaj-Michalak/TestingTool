import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_username(driver):
    username = driver.find_element(By.ID, "username")
    id = uuid.uuid1()
    username.send_keys(id.hex)

def open_game_by_id(driver, id):
    # wait until the game list is loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "li"))) 
    # try:
    game = driver.find_element(By.XPATH, f'//*[text()="{id}"]')
    # except:
    #     time.sleep(5)
    #     game = driver.find_element(By.XPATH, f"//*[text()='{id}']")
    
    # finally:


    game.click()
    
def open_game(driver, id, language):
    driver.get('https://gs-client.testowaplatforma123.net/online/development/demo/single_run/')

    select = Select(driver.find_element_by_id('locale'))
    select.select_by_value(language)
    fill_username(driver)

    
    
    open_game_by_id(driver, id)
    
def switch_to_iframe(driver):
    # wait until the iframe is loaded
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe"))) 

    driver.switch_to.frame(iframe)