import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()


def verify_auth_state(token, signature, openid):
    url = "https://api.weixin.qq.com/wxa/checksession?access_token={}&signature={}&openid={}&sig_method=hmac_sha256".format(
        token, signature, openid
    )
    return requests.get(url).json()

def hmac_sha256(key, word=""):
    import hashlib
    import hmac
    return hmac.new(key.encode("utf-8"), word.encode("utf-8"), hashlib.sha256).hexdigest()


if __name__ == '__main__':
    from wechat_access_token import get_stable_access_token

    openid = "oQ14G47pfy-IvmhB-AvaXqw0xlA8"
    session_key = "u5jEYDDNOm1sZIEZvO9GCw=="
    access_token = get_stable_access_token(os.getenv("WECHAT_APP_ID"), os.getenv("WECHAT_SECRET"))["access_token"]
    result = verify_auth_state(access_token, hmac_sha256(session_key), openid)
    print(result)
