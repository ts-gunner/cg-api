import hashlib
import hmac
import jwt
from datetime import datetime, timedelta, timezone
from typing import Union
# wechat only support hmac sha256
def hmac_sha256(key, word=""):
    return hmac.new(key.encode("utf-8"), word.encode("utf-8"), hashlib.sha256).hexdigest()


# 创建token
def create_access_token(data: dict, secret_key, expires_delta: Union[timedelta, None] = None):
    if secret_key is None or secret_key == "":
        raise ValueError("缺乏secret_key")
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, secret_key, algorithm="HS256")
    return encode_jwt
