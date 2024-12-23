from fastapi import APIRouter, Form, UploadFile, Depends
from sqlalchemy.orm import Session
from utils.logger import LoguruLogger
from services.common import get_storage_service, get_db, get_user_service, verify_user_request
from models.common import APIResponse, TokenData
from services.wechat import WeChatService

user_router = APIRouter(
    tags=["user"],
    include_in_schema=True
)


@user_router.get("/user/wechat/login")
def wechat_login(code: str, db: Session = Depends(get_db)):
    logger = LoguruLogger.get_logger()
    logger.info("wechat login...")
    logger.info("wechat login parameter - code: {}".format(code))
    res = WeChatService.we_login(code)
    response = get_user_service(db).user_login(res["openid"])
    res.update(response)
    logger.info("wechat login successfully!!")
    logger.info(res)
    return APIResponse(data=res)


@user_router.post("/user/wechat/save_profile")
async def save_profile(
        avatar_blob: UploadFile,
        nickname: str = Form(...),
        openid: str = Form(...),
        db: Session = Depends(get_db)
):
    logger = LoguruLogger.get_logger()
    logger.info("save_profile...")
    storage = get_storage_service()
    file_content = await avatar_blob.read()
    bucket_remote_path = storage.put_file(file_content, f"/{openid}/{avatar_blob.filename}")
    res = get_user_service(db).create_or_update_user_profile(bucket_remote_path, nickname, openid)
    return res


@user_router.get("/user/wechat/get_user_info")
def get_user_profile(openid: str, db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("get_user_profile...")
    logger.info(token_data)
    res = get_user_service(db).get_user_info(openid, token_data)
    return res


@user_router.get("/user/wechat/get_all_roles")
def get_all_roles(db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("get_all_roles...")
    return get_user_service(db).get_all_roles()


@user_router.get("/user/wechat/get_permission_roles")
def get_all_permissions(db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("get_all_permissions...")
    return get_user_service(db).get_all_permissions()


