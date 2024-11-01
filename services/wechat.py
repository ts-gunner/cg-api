import requests
import os
from models.common import APIResponse
import json


class WeChatService:
    @staticmethod
    def we_login(code: str):
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(
            os.environ["WECHAT_APP_ID"], os.environ["WECHAT_SECRET"], code
        )
        response = requests.get(url).json()

        return response

    @staticmethod
    def get_stable_access_token(app_id: str, app_secret: str, force_refresh: bool = False):
        url = "https://api.weixin.qq.com/cgi-bin/stable_token"
        data = {
            "grant_type": "client_credential",
            "appid": app_id,
            "secret": app_secret,
            "force_refresh": force_refresh
        }
        return requests.post(url, data=json.dumps(data)).json()
