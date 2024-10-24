import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()


def get_access_token(app_id, app_secret):
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(app_id, app_secret)
    access_token = requests.get(url).json()
    return access_token
    # result = {
    #     'access_token': '85_ViqN0G_4kI2S_nBkqW2VaDQmcKusj5sc4c49OaQcFxDTu0yy4qqSagEp4Q7qFNT6pMQavlY6RawNlhb6LG-6Qy0AOFrpoVXZstTOEOj1q12st0EQvt1E1k369x0ERVfACAVIM',
    #     'expires_in': 7200
    # }


def get_stable_access_token(app_id:str, app_secret:str, force_refresh:bool = False):
    url = "https://api.weixin.qq.com/cgi-bin/stable_token"
    data = {
        "grant_type": "client_credential",
        "appid": app_id,
        "secret": app_secret,
        "force_refresh": force_refresh
    }
    access_token = requests.post(url, data=json.dumps(data)).json()
    return access_token


if __name__ == '__main__':
    # get_access_token(os.getenv("WECHAT_APP_ID"), os.getenv("WECHAT_SECRET"))
    get_stable_access_token(os.getenv("WECHAT_APP_ID"), os.getenv("WECHAT_SECRET"))
