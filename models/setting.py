from enum import Enum
import os
# metastore
from sqlalchemy import create_engine, Engine
import pymysql
from models.common import SettingBase
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

pymysql.install_as_MySQLdb()


class MetaStoreType(str, Enum):
    MYSQL = "mysql"
    SQLITE = "sqlite"


class BucketStoreType(str, Enum):
    TENCENT = "tencent"


class Setting:

    def __init__(self):
        self._settings: SettingBase = SettingBase()
        self._metastore: Engine = None
        self._bucket_client = None
        self._set_metastore()
        self._set_bucket_store()
        self._set_configuration()

    def _set_metastore(self):
        storage_type = os.environ["DB_TYPE"]
        connection_str = os.environ["DB_CONNECTION_STRING"]
        if storage_type == MetaStoreType.MYSQL:
            self._metastore = create_engine(connection_str, pool_recycle=1500, pool_timeout=3600)
        elif storage_type == MetaStoreType.SQLITE:
            self._metastore = create_engine(connection_str, connect_args={"check_same_thread": False})

    def _set_bucket_store(self):
        self._settings.bucket_store_type = os.environ["BUCKET_STORE_TYPE"]
        self._settings.store_path = os.environ["BUCKET_STORE_PATH"]
        self._settings.user_store_path = os.environ["USER_ATTACHMENT_PATH"]
        self._settings.bucket_name = os.environ["BUCKET_STORE_NAME"]
        if self._settings.bucket_store_type == BucketStoreType.TENCENT:
            secret_id = os.environ['TENCENT_SECRET_ID']
            secret_key = os.environ['TENCENT_SECRET_KEY']
            region = os.environ["TENCENT_BUCKET_REGION"]
            config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
            self._bucket_client = CosS3Client(config)

    def _set_configuration(self):
        pass

    @property
    def metastore(self):
        return self._metastore

    @property
    def settings(self):
        return self._settings

    @property
    def bucket_client(self):
        return self._bucket_client
