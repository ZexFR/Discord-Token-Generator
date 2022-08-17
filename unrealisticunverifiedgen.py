import os                                                         
from dhooks.client import Webhook
from discord_webhook import DiscordWebhook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options                            
import time
from datetime import date, datetime
import json
import math
import base64
import urllib
import hashlib
import random
import string
import requests
import colorama
from colorama import Fore, init
import pyautogui

init()

# Sorry for the auto auth not working ATM. This is because Discord changed their systems the last time I did this. Thanks


def random_username():         # defines the random username gen    
 with open("MyFile.txt", "r") as file:                  
  allText = file.read()
  words = list(map(str, allText.split()))




def get_random_string(length):       # defines the random string to make the email etc
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def runwindow():
    username = str(input(Fore.BLUE + "Write what name you want » "+ Fore.RESET)) # asks what username you want
    password = str(input(Fore.GREEN + "Write what password you want » " + Fore.RESET)) # asks what password you want
    while True:
        proxy = random.choice(open("proxies.txt").readlines()) # opens the proxies file to gather the proxies
        print(Fore.GREEN + 'Using proxy ' + proxy + '.') # prints which proxy it's using
        driver = webdriver.Chrome(executable_path='chromedriver.exe') # opens chromedriver
        options = webdriver.ChromeOptions() 
        options.add_argument("--incognito") # turns on incognito mode
        options.add_argument("start-maximized") # minimises the screen
        options.add_argument('--proxy-server=%s' % proxy) # starts the proxy server
        driver = webdriver.Chrome(chrome_options=options) 
        driver.get("https://discord.com/register") # Opens Discord Register System
        time.sleep(1)
        email = get_random_string(8) + str(random.randint(1234, 9876)) + "@gmail.com" # Creates a random email with @gmail.com at the end
        user = get_random_string(6 ) + str(random.randint(1234, 9876)) + " | Zex" # Creates a random amount of letters/numbers for the username 
        driver.find_element("xpath", '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/div[1]/div/input').send_keys(email)       #Writes the email in the box
        time.sleep(0.1)
        driver.find_element("xpath", '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/div[2]/div/input').send_keys(get_random_string(3) + str(random.randint(1234, 9876)) +  " | " + username) # Writes the username in the box
        time.sleep(0.1)
        driver.find_element("xpath", '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/div[3]/div/input').send_keys(    # Writes the password in the box
            password) 
        time.sleep(0.1)
        driver.find_element("xpath", '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/form/div/div/div[5]/label/input').click()  # Verifies the button
        time.sleep(0.3)
        actions = ActionChains(driver)
        time.sleep(.2)
        driver.find_elements(By.CLASS_NAME, 'css-1hwfws3')[0].click() # Line 71 - 80 is the date writing
        actions.send_keys(str(random.randint(1, 12)))
        actions.send_keys(Keys.ENTER)
        actions.send_keys(str(random.randint(1, 28)))
        actions.send_keys(Keys.ENTER)
        actions.send_keys(str(random.randint(1990, 2001)))
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(3)
        
        actions.perform()
        time.sleep(7)
        os.system("cls")
        print("Please do the Auth")
        input("Press Enter to when you have done the puzzle :)") # Waits for you to do the auth
        time.sleep(3)
        driver.switch_to.default_content()
        print(Fore.RESET + ' ')
        time.sleep(3)
 
        token = driver.execute_script(
            "let popup; popup = window.open('', '', `width=1,height=1`); if(!popup || !popup.document || !popup.document.write) console.log('Please allow popups'); window.dispatchEvent(new Event('beforeunload')); token = popup.localStorage.token.slice(1, -1); popup.close(); return token") # Gets the token of the account

        hook = "Enter A Webhook Here OR Delete Lines 94-98" 
        r = requests.post(hook, json={
            "content": token
        })
        print(f'Sent webhook post request. Status = {r.status_code} ~ {r.reason}') # Sends the token to your specified webhook
        print(f"{token}")
        with open('tokens.txt', 'a') as f:   # Writes the token in the folder "tokens.txt"
            f.write(token)
            f.write('\n')
        driver.quit()
        time.sleep(1)



runwindow()
