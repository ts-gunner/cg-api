from sqlalchemy.orm import Session
from db.user_profile import UserProfile, UserProfileBase
from models.common import APIResponse

from models.setting import Setting


class UserDataManager:
    def __init__(self, db: Session):
        self.db = db

    def get_user_object(self, openid: str) -> UserProfile:
        return self.db.query(UserProfile).filter(UserProfile.openid == openid).first()

    def create_user_object(self, profile: dict):
        obj = UserProfile(**profile)
        self.db.add(obj)


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self._dm = UserDataManager(db)

    def create_user_profile(self, openid: str):
        obj = self._dm.get_user_object(openid)
        if not obj:
            self._dm.create_user_object({"openid": openid})
        self.db.commit()

    def create_or_update_user_profile(self, avatar_url: str, nickname: str, openid: str):
        obj = self._dm.get_user_object(openid)
        if obj:
            obj.nickname = nickname
            obj.avatar_url = avatar_url
        else:
            self._dm.create_user_object({
                "openid": openid,
                "nickname": nickname,
                "avatar_url": avatar_url
            })
        self.db.commit()
        return APIResponse()

    def get_user_info(self, openid: str):
        obj = self._dm.get_user_object(openid)

        return APIResponse(data=UserProfileBase.model_validate(obj) if obj else None)
