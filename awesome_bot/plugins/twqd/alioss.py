# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/8 21:22
# Description:

from .prompt import *
import oss2
from datetime import datetime


class AliyunOSS(object):
    def __init__(self):
        AccessKeyId = config.accesskeyid
        AccessKeySecret = config.accesskeysecret
        auth = oss2.Auth(AccessKeyId, AccessKeySecret)
        bucket_name = config.bucket_name
        self.bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', bucket_name)

        self.osh_day = str(datetime.now(TIME_ZONE_CN)).split(" ")[0]
        self.root_obj = f'cpds/api/stu_snp/{self.osh_day}/'

    def upload_base64(self, content: str, username: str):
        result = self.bucket.put_object(f'{self.root_obj}/{self.osh_day}/{username}.txt', content)

        # # HTTP返回码。
        # print('http status: {0}'.format(result.status))
        # # 请求ID。请求ID是请求的唯一标识，强烈建议在程序日志中添加此参数。
        # print('request_id: {0}'.format(result.request_id))
        # # ETag是put_object方法返回值特有的属性，用于标识一个Object的内容。
        # print('ETag: {0}'.format(result.etag))
        # # HTTP响应头部。
        # print('date: {0}'.format(result.headers['date']))

    def snp_exist(self, username):
        return self.bucket.object_exists(f'{self.root_obj}{username}.txt')

    async def download_snp(self, username):
        if self.snp_exist(username):
            self.bucket.get_object_to_file(f'{self.root_obj}{username}.txt', SERVER_DIR_SCREENSHOT + f'/{username}.txt')
            return True
        else:
            return False