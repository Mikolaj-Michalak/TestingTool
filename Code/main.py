from selenium import webdriver  
from selenium.webdriver.common.by import By 
import lobby_e2
import game_e2
import image_manipulation
import os
import time
import cv2
import math
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")

with open("Configs\config.json") as json_data_file:
    data = json.load(json_data_file)

game_names = data['game_names']
languages = data['languages']
# game_names = [
#     # "Mad Men and Nuclear War",
#     "Stunning Hot 20 Deluxe"

# ]
# # languages = ["el", "en", "sr"]
# languages = ["en", "pl", "sr", "ro", "de", "eo", "fr", "nl", "zh", "lv", "et", "ru", "it", "lt", "th", "tr", "hu", "hr", "sk", "pt", "bg", "el"]

driver = webdriver.Chrome('D:/Optimo/TestingTool/chromedriver.exe', chrome_options=chrome_options)

driver.maximize_window()

action = webdriver.ActionChains(driver)

for game_name in game_names:
    for language in languages: 
        lobby_e2.open_game(driver, game_name, language)

        lobby_e2.switch_to_iframe(driver)

        game_e2.wait_for_game_load(driver)
     
        if not os.path.exists("Output/" + game_name):
            os.makedirs("Output/" + game_name)

        rules_length = driver.execute_script("return window.debugAPI.rulesLength()")

        images = []

        folder_path = "Output/" + game_name + "/"

        for i in range(rules_length):
            game_e2.open_next_rules_page(driver)
            path = folder_path + str(i) + '.png'
            driver.save_screenshot(path)
            img = cv2.imread(path)
            images.append(img)

        rows = []

        screens_per_row = 3
        if rules_length % 3 == 1:
            screens_per_row = 2
        
        for i in range (math.ceil(rules_length / screens_per_row)):
            row = cv2.hconcat(images[i*screens_per_row:i*screens_per_row+screens_per_row  ])
            rows.append(row)

        resized_rows = image_manipulation.vconcat_resize(rows)

        final_path = folder_path + language + ".png" 

        cv2.imwrite(final_path, resized_rows)

        for i in range(rules_length):
            path = folder_path + str(i) + ".png"
            if(os.path.exists(path)):
                os.remove(path)



driver.close()