from models.setting import Setting
from qcloud_cos import CosS3Client


class TencentBucketStorage:
    def __init__(self, setting: Setting):
        self._setting = setting
        if self._setting.bucket_client and isinstance(self._setting.bucket_client, CosS3Client):
            self._client: CosS3Client = self._setting.bucket_client
        else:
            self._client: CosS3Client = None

    def put_file(self, blob: bytes, object_path: str) -> str:
        res = self._client.put_object(
            Bucket=self._setting.settings.bucket_name,  # Bucket 由 BucketName-APPID 组成
            Body=blob,
            Key=object_path,
            StorageClass='STANDARD',
            ContentType='text/html; charset=utf-8'
        )
        print(res)
        return self._setting.settings.user_store_path + object_path
