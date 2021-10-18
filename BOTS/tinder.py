import ssl
import ast
#from main.models import *
import random
import json

import requests
from bs4 import BeautifulSoup
from django.core.cache import cache
#from .models import *
import time


class Tinder:
    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context

    def get_header(self):

       # persistent_device_id = "1cff5b31-5485-43ea-9644-783c0c23c14d"
       # user_session_id = "524d8886-0823-49dc-acf2-8bf78538bc12"
       # x_auth_token = "2601c394-e9c7-4133-a7ce-662edc247b2c"
        #app_session_id = "756c166c-c572-4a73-8c02-0a4aee132ea5"

        persistent_device_id = "7c29c47f-a32e-47a4-a768-bfd167bd7471"
        user_session_id = "2dd91f76-0066-4dd8-bea7-d6be9a37f16f"
        x_auth_token = "b55a3f6a-5ac4-463f-baaf-02df9d2c2e47"
        app_session_id = "98247460-4fb9-44cb-b303-bf5c10a49188"
        app_version = "1027200"

        headers = {
                'x-supported-image-formats': 'jpeg',
                'persistent-device-id': persistent_device_id,
                'tinder-version': '2.71.0',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
                'user-session-id': user_session_id,
                'Accept': 'application/json',
                'app-session-time-elapsed': '2139',
                'X-Auth-Token': x_auth_token,
                'user-session-time-elapsed': '3330',
                'platform': 'web',
                'app-session-id': app_session_id,
                'app-version': app_version,
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty'
        }

        return headers


    def unlike_action(self, id):
        api ="https://api.gotinder.com/pass/{}?locale=en&user_traveling=1&roomId=undefined".format(id)
        response = requests.request("GET", api, headers=self.get_header(), data={}).json()
        print(response)


    def like_action(self, id):
        api = "https://api.gotinder.com/like/{}?locale=en".format(id)
        response = requests.request("POST", api, headers=self.get_header(), data={"user_tralving":1}).json()
        print(response)

    def get_like_list(self):
        url = "https://api.gotinder.com/v2/recs/core?locale=en"
        response = requests.request("GET", url, headers=self.get_header(), data={}).json()
        return response

    def get_like_actions(self):
        get_like_response = self.get_like_list().get('data').get('results')
        count=0
        print("######## USERRRRR #########")
        print(get_like_response)
        # Tinder
        for like_user in get_like_response:
            if count == 7:
                self.unlike_action(like_user.get('user')["_id"])
            else:
                self.like_action(like_user.get('user')["_id"]) 
            count = count + 1
            time.sleep(1)
              
    def auto_like(self):
        
        while True:
            try:
                self.get_like_actions()
                time.sleep(10)
            except Exception as e:
                print(str(e))
                print("######## EXCEPTIONNN #########")

bot = Tinder()
bot.auto_like()