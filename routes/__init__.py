from utils.auth import Authorization
# TokenData
auth = Authorization(
    token_param_name="token_data",
    role_param_name="roles",
    permission_param_name="permissions",
    role_extractor=lambda x: x["role_id"],
    permission_extractor=lambda x: x["permission_id"]
)