import os
from functools import lru_cache
from pathlib import Path
from utils.logger import LoguruLogger
from models.setting import Setting, BucketStoreType
from sqlalchemy.orm import sessionmaker, Session
from services.storage import TencentBucketStorage
from services.user import UserService


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
    return UserService(db)
