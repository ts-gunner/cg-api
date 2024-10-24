from pydantic import BaseModel

class WeChatLoginBody(BaseModel):
    code: str
