from typing import List, Any
from fastapi import HTTPException, status
from pydantic import BaseModel
from functools import wraps
from utils.common import HttpResponse


class Authorization:
    """
    根据token解析的数据进行角色和权限的校验

    场景一： 假设需要校验的token是字典或者BaseModel, 并且route层的token参数名字是token_data
    则假设token数据是 token_data = {"roles": [{"roleId": "admin", "roleName": "超级管理员"}], "permission": [{"permissionId": "a:x", "permissionName": "xx"}]}
    那么初始化对应的值是
    token_param_name="token_data"
    role_param_name="roles"
    role_extractor=lambda x:x["roleId"]
    permission_param_name="permission"
    permission_extractor=lambda x:x["permissionId"]
    """

    def __init__(
            self,
            token_param_name: str,
            role_param_name: str,
            permission_param_name: str,
            role_extractor=lambda x: x,
            permission_extractor=lambda x: x
    ):
        self.token_param_name = token_param_name
        self.role_param_name = role_param_name
        self.permission_param_name = permission_param_name
        self.role_extractor = role_extractor
        self.permission_extractor = permission_extractor

    @staticmethod
    def verify_permission(user_permission, require_permission):
        user_chunks = user_permission.split(":")
        require_chunks = require_permission.split(":")
        # 权限层级的比较
        if user_chunks[0] == '*' or require_chunks[0] == '*':
            return True

            # 如果权限完全匹配
        if user_permission == require_permission:
            return True

            # 检查通用权限
        if user_chunks[0] == require_chunks[0] and user_chunks[1] == '*':
            return True

            # 否则返回 False
        return False

    def has_permission(self, require_permissions: List[str]):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                token = kwargs.get(self.token_param_name, {})
                if not token:
                    return HttpResponse(code=status.HTTP_401_UNAUTHORIZED, msg="身份验证失败！！")
                if isinstance(token, BaseModel):
                    token = token.model_dump()
                permission_list: List[object] = token.get(self.permission_param_name, [])
                permission_list: List[str] = [self.permission_extractor(permission) for permission in permission_list]
                is_pass = False
                for permission in permission_list:
                    for require_permission in require_permissions:
                        if self.verify_permission(permission, require_permission):
                            is_pass = True
                            break
                    if is_pass:
                        break
                if not is_pass:
                    return HttpResponse(code=status.HTTP_403_FORBIDDEN, msg="没有权限！")
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def has_role(self, require_roles: List[str]):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                token = kwargs.get(self.token_param_name, {})
                if not token:
                    return HttpResponse(code=status.HTTP_403_FORBIDDEN, msg="身份验证失败！")
                if isinstance(token, BaseModel):
                    token = token.model_dump()
                role_list: list = token.get(self.role_param_name, [])
                role_list = [self.role_extractor(role) for role in role_list]
                is_pass = False
                for role in role_list:
                    if role in require_roles:
                        is_pass = True
                        break
                if not is_pass:
                    return HttpResponse(code=status.HTTP_403_FORBIDDEN, msg="没有权限！")
                return func(*args, **kwargs)

            return wrapper

        return decorator
