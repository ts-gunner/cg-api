from fastapi import Header, status, HTTPException, Depends
from functools import lru_cache
from utils.logger import LoguruLogger
from models.setting import Setting, BucketStoreType
from models.common import TokenData, APIResponse
from sqlalchemy.orm import sessionmaker, Session
from services.storage import TencentBucketStorage
from services.user import UserService
from services.task import TaskService
import jwt

@lru_cache
def get_init_settings():
    return Setting()


def get_db():
    logger = LoguruLogger.get_logger()
    settings: Setting = get_init_settings()
    _session = sessionmaker(bind=settings.metastore)
    session: Session = _session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        logger.info("db操作异常，已回滚!")
        raise
    finally:
        session.close()
        logger.info("db close")


def get_storage_service():
    setting = get_init_settings()
    if setting.settings.bucket_store_type == BucketStoreType.TENCENT:
        return TencentBucketStorage(setting)


def get_user_service(db: Session):
    return UserService(setting=get_init_settings(), db=db)


def verify_user_request(auth_token: str = Header()) -> TokenData:
    setting = get_init_settings().settings
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(auth_token, setting.app_secret, algorithms=["HS256"])
        token_data = TokenData()
        token_data.user_id = payload["user_id"]
        token_data.roles = payload["roles"]
        token_data.permissions = payload["permissions"]
        token_data.groups = payload["groups"]

        return token_data
    except Exception as err:
        raise credential_exception

def get_task_service(db:Session):
    return TaskService(db)
