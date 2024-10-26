# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import os
import logging
from dotenv import load_dotenv

load_dotenv()
# 正常情况日志级别使用 INFO，需要定位时可以修改为 DEBUG，此时 SDK 会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = os.environ[
    'TENCENT_SECRET_ID']  # 用户的 SecretId，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
secret_key = os.environ[
    'TENCENT_SECRET_KEY']  # 用户的 SecretKey，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参见 https://cloud.tencent.com/document/product/598/37140
region = 'ap-guangzhou'  # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
# COS 支持的所有 region 列表参见https://cloud.tencent.com/document/product/436/6224
scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填


def put_file():
    file_path = r"C:\Users\TS-Runner\Downloads\wechat-add.png"
    # bucket_name = "forty-store-1305170185"
    bucket_name = "forty-bucket-1305170185"
    # 小程序附件目录
    dir_name = 'wechat/applet/'
    file_name = os.path.basename(file_path)
    object_key = dir_name + file_name
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Scheme=scheme)
    client = CosS3Client(config)
    with open(file_path, 'rb') as fp:
        response = client.put_object(
            Bucket=bucket_name,  # Bucket 由 BucketName-APPID 组成
            Body=fp,
            Key=object_key,
            StorageClass='STANDARD',
            ContentType='text/html; charset=utf-8'
        )
        print(response)
    return f"https://{bucket_name}.cos.ap-guangzhou.myqcloud.com/{object_key}"
    """
    INFO:qcloud_cos.cos_client:generate built-in connection pool success. maxsize=10,10
    INFO:qcloud_cos.cos_client:bound built-in connection pool when new client. maxsize=10,10
    INFO:qcloud_cos.cos_client:put object, url=:https://forty-bucket-1305170185.cos.ap-guangzhou.myqcloud.com/wechat/appletwechat-add.png ,headers=:{'x-cos-storage-class': 'STANDARD', 'Content-Type': 'text/html; charset=utf-8'}
    {'Content-Length': '0', 'Connection': 'keep-alive', 'Date': 'Fri, 25 Oct 2024 17:43:50 GMT', 'ETag': '"94e06fb7e31fcc2e01e6bc403b6a0a7a"', 'Server': 'tencent-cos', 'x-cos-hash-crc64ecma': '3039184064247558398', 'x-cos-request-id': 'NjcxYmQ4ZDZfOGMwZDdiMGJfMTNmMWFfNTllNjYzYw==', 'x-cos-storage-class': 'STANDARD'}
    """


if __name__ == '__main__':
    put_file()
