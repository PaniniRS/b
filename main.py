from ast import For
import gzip
import time
import requests
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
import logging
import sqlite3
from var import *

# TODO: CHANGE THIS
userAcc = ["TmrwsAmerica","ClaudeDavisFans", "PatMAGA2024", "FJBTruth", "paninirs@gmail.com", "patriotsworld2022@gmail.com"]
userPw = ["vesti01..", "World2022$"]

LIST_URL = "https://www.gettr.com/user/retirewcashflow/following"
INPUT_EMAIL = userAcc[0]
INPUT_PASSWORD = userPw[0]
FOLLOW = False
FOLLOWFROMLIST = True

#------------------------------------------------------------------
options = {
    'ignore_http_methods': [],
    'suppress_connection_errors': False
}
logging.basicConfig(level=logging.DEBUG)

conn = sqlite3.connect('database.db')
browser = webdriver.Chrome(seleniumwire_options=options) #driver aka selenium object = browser

auth_up = {"content": {"email": "", "pwd": "", "token": ""}}
auth_headers = {"x-app-auth": {"user": "", "token": ""}}
username = ''

# goes to login page 
browser.get(LOGIN_URL)
browser.implicitly_wait(15)
#switches login mode from number to email
loginModeSwitch = browser.find_element(By.CLASS_NAME, "jss49")
print(loginModeSwitch)
loginModeSwitch.click()
time.sleep(4)
#finds email and pw elements
email = browser.find_element(By.ID, "email")
password = browser.find_element(By.ID, "password")
#inputs email and pw
email.send_keys(INPUT_EMAIL)
time.sleep(5)
password.send_keys(INPUT_PASSWORD)
time.sleep(5)
#clicks the login button
login_button = browser.find_element(By.XPATH, "//*[contains(text(),'Log In')]").find_element(By.XPATH, "./..")
login_button.click()
time.sleep(5)
print("Logged in successfully")
time.sleep(15)

#idk what this does ngl
# for request in browser.requests:
#     logging.info("REQUEST: %s", request.path)
#     if request.method == 'POST' and request.path == '/s/auth_up':
#         body = request.body.decode('utf-8')
#         req = json.loads(body)['content']
#         auth_up["content"]["email"] = INPUT_EMAIL
#         auth_up["content"]["pwd"] = INPUT_PASSWORD
#         auth_up["content"]["token"] = req['token']

#         response_object = json.loads(gzip.decompress(request.response.body))
#         auth_headers["x-app-auth"]["user"] = username = response_object["result"]['user']['username']
#         auth_headers["x-app-auth"]["token"] = response_object["result"]["token"]

# if FOLLOW:
#     user_count = 0
#     while user_count < MAX_FOLLOWS_PER_DAY:
#         response = requests.get(SUGGESTIONS_URL, headers=get_headers_from_dict(auth_headers))
#         list_of_users = response.json()["result"]["data"]["list"]
#         for user in list_of_users:
#             logging.info('Following: %s\n', user)
#             response = requests.post(FOLLOW_URL.format(username, user), headers=get_headers_from_dict(auth_headers))
#             user_count += 1

if FOLLOWFROMLIST: 
    user_count = 0
    browser.get(LIST_URL)
    while user_count < MAX_FOLLOWS_PER_DAY:
        followButtons = browser.find_elements(By.CLASS_NAME, "js234") #finds all the follow buttons
        for i in range(MAX_FOLLOWS_PER_DAY):
            followButton = followButtons[i]
            if followButton.text == "Follow":
                followButton.click();
                logging.info("Followed %d person\n",i)
                user_count = user_count + 1
        
