import requests
import os
from models.common import APIResponse


class WeChatService:

    @staticmethod
    def we_login(code: str):
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(
            os.environ["WECHAT_APP_ID"], os.environ["WECHAT_SECRET"], code
        )
        response = requests.get(url).json()

        return APIResponse(data=response)
