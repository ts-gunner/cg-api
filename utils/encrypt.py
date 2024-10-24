import hashlib
import hmac

# wechat only support hmac sha256
def hmac_sha256(key, word=""):
    return hmac.new(key.encode("utf-8"), word.encode("utf-8"), hashlib.sha256).hexdigest()
