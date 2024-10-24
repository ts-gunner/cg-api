import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_phone_info():
    url = "https://api.weixin.qq.com/wxa/business/getuserphonenumber?access_token=ACCESS_TOKEN"