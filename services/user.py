from sqlalchemy.orm import Session
from db.user_profile import UserProfile, UserProfileBase
from models.common import APIResponse
from utils.encrypt import create_access_token
from utils.logger import LoguruLogger
from models.common import TokenData
from models.setting import Setting
from db.role import UserRoleBase, UserRole, UserRoleMap
from db.group import UserGroupBase, UserGroup, UserGroupMap
from db.permission import UserPermission, RolePermission, AuthPermission, AuthPermissionBase
from typing import List


class UserDataManager:
    def __init__(self, db: Session):
        self.db = db

    def get_user_object(self, openid: str) -> UserProfile:
        return self.db.query(UserProfile).filter(UserProfile.openid == openid).first()

    def create_user_object(self, profile: dict):
        obj = UserProfile(**profile)
        self.db.add(obj)

    def get_user_role_list(self, openid: str) -> List[UserRoleBase]:
        role_list = self.db.query(UserRole).join(UserRoleMap, UserRole.role_id == UserRoleMap.role_id).filter(UserRoleMap.user_id == openid).all()
        return [UserRoleBase.model_validate(role) for role in role_list]

    def get_user_group_list(self, openid: str) -> List[UserGroupBase]:
        group_list = self.db.query(UserGroup).join(UserGroupMap, UserGroup.group_id == UserGroupMap.group_id).filter(
            UserGroupMap.user_id == openid).all()
        return [UserGroupBase.model_validate(group) for group in group_list]

    def get_user_permission_list(self, openid: str) -> List[str]:
        permission_list = self.db.query(UserPermission.permission_id, AuthPermission.permission_name).join(
            AuthPermission, UserPermission.permission_id == AuthPermission.permission_id
        ).filter(UserPermission.user_id == openid).all()
        return [AuthPermissionBase.model_validate(permission) for permission in permission_list]

    def get_role_permission_list(self, role_ids: List[str]) -> List[str]:
        permission_list = self.db.query(RolePermission.permission_id, AuthPermission.permission_name).join(
            AuthPermission, RolePermission.permission_id == AuthPermission.permission_id
        ).filter(RolePermission.role_id.in_(role_ids)).all()
        return [AuthPermissionBase.model_validate(permission) for permission in permission_list]

    def get_all_role_list(self):
        role_list = self.db.query(UserRole).all()
        return [UserRoleBase.model_validate(role) for role in role_list]

    def get_all_permission_list(self):
        permission_list = self.db.query(AuthPermission).all()
        return [AuthPermissionBase.model_validate(permission) for permission in permission_list]


class UserService:
    def __init__(self, setting: Setting, db: Session):
        self.setting = setting.settings
        self.db = db
        self._logger = LoguruLogger.get_logger()
        self._dm = UserDataManager(db)

    def create_user_profile(self, openid: str):
        obj = self._dm.get_user_object(openid)
        if not obj:
            self._dm.create_user_object({"openid": openid})
        self.db.commit()

    def create_or_update_user_profile(self, avatar_url: str, nickname: str, openid: str):
        res_data = {
            "avatar_url": avatar_url,
            "nickname": nickname
        }
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
        return APIResponse(data=res_data)

    def get_user_info(self, openid: str, token: TokenData):
        obj = self._dm.get_user_object(openid)
        return APIResponse(data={
            "profile": UserProfileBase.model_validate(obj) if obj else None,
            "roles": token.roles,
        })

    def user_login(self, openid: str):
        self.create_user_profile(openid)
        role_list = self._dm.get_user_role_list(openid)
        role_ids = [role.role_id for role in role_list]
        token_data = TokenData()
        token_data.user_id = openid
        token_data.groups = self._dm.get_user_group_list(openid)
        token_data.roles = role_list
        token_data.permissions = [*self._dm.get_user_permission_list(openid), *self._dm.get_role_permission_list(role_ids)]
        token = create_access_token(token_data.model_dump(), self.setting.app_secret)
        self._logger.info("token: {}".format(token))
        return token

    def get_all_roles(self):
        return APIResponse(data=self._dm.get_all_role_list())

    def get_all_permissions(self):
        return APIResponse(data=self._dm.get_all_permission_list())

