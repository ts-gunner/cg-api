from models.setting import Setting
from qcloud_cos import CosS3Client


class TencentBucketStorage:
    def __init__(self, setting: Setting):
        self._setting = setting
        self._config = self._setting.settings
        if self._setting.bucket_client and isinstance(self._setting.bucket_client, CosS3Client):
            self._client: CosS3Client = self._setting.bucket_client
        else:
            self._client: CosS3Client = None

    def put_file(self, blob: bytes, object_path: str) -> str:

        res = self._client.put_object(
            Bucket=self._config.bucket_name,  # Bucket 由 BucketName-APPID 组成
            Body=blob,
            Key=self._config.user_store_path + object_path,
            StorageClass='STANDARD',
            ContentType='text/html; charset=utf-8'
        )
        file_path = self._config.store_path + self._config.user_store_path + object_path
        print(file_path)
        return file_path
