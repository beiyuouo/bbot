# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/22 12:44
# Description:

from awesome_bot.config.config import config

ALKAID_HOST = config.alkaid_twqd_host

ALKAID_TWQD_API = ALKAID_HOST + '/cpds/api/stu_twqd'
ALKAID_TWQD_PLUS_API = ALKAID_HOST + '/cpds/api/stu_twqd2'

ADDUSER_API = ALKAID_HOST + '/cpdaily/api/item'
ADDUSER_QUICKSTART_API = ADDUSER_API + '/quick_start'
ADDUESR_VERITY_EMAIL_API = ADDUSER_API + '/verity_email_passable'
ADDUSER_VERITY_EXIST_API = ADDUSER_API + '/verity_account_exist'
ADDUESR_VERITY_ACCOUNT_API = ADDUSER_API + '/verity_cpdaily_account'
ADDUSER_VERITY_CODE_API = ADDUSER_API + '/send_verify_code'
ADDUSER_ADDUSER_API = ADDUSER_API + '/add_user'
