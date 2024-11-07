from fastapi import APIRouter, Form, UploadFile, Depends
from sqlalchemy.orm import Session
from services.common import verify_user_request, get_db, get_shop_service
from models.common import APIResponse, TokenData
from utils.logger import LoguruLogger

shop_router = APIRouter(
    tags=["shop"],
    include_in_schema=True
)


@shop_router.get("/shop/wechat/get_shop_profile")
def get_shop_profile(user_id: str, db: Session = Depends(get_db), token_data: TokenData = Depends(verify_user_request)):
    logger = LoguruLogger.get_logger()
    logger.info("wechat get_tasks..., params - user_id: {}".format(user_id))
    return get_shop_service(db).get_shop_profile(user_id)

