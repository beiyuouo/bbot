# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/8 13:04
# Description:

import pytz
import os
from awesome_bot.config.config import config

TIME_ZONE_CN = pytz.timezone('Asia/Shanghai')
GOCQ_PATH = config.gocq_path
IMAGE_DIR = config.image_dir
TWQD_DIR_NAME = config.twqd_dir_name

SERVER_DIR_SCREENSHOT = os.path.join(GOCQ_PATH, IMAGE_DIR, TWQD_DIR_NAME)


CODE_SUCCESS = 200
CODE_FAILED = 102
CODE_PERMISSION_ERROR = 101

CODE_TWQD_SUCCESS = 300
CODE_TWQD_UNFINISHED = []
CODE_TWQD_FAILED = []

CODE_ADDUSER_ACCOUNT_EXIST = 100
CODE_ADDUSER_ACCOUNT_ERROR = 101
CODE_ADDUSER_EMAIL_ERROR = 102
CODE_ADDUSER_TOKEN_ERROR = 103
CODE_ADDUSER_EMAIL_SEND_ERROR = 104
CODE_ADDUSER_SID_ERROR = 105
CODE_ADDUSER_SUCCESS = 200
CODE_ADDUSER_EMAIL_SEND = 300

ENABLE_PRIVATE = False

PRIVATE_PROMPT = "别偷偷给我发消息呦~"
ARGS_PROMPT = "后面要加一个学号哟~"
ARGS2_PROMPT = "后面要加学号和密码哟~"
NULL_PROMPT = "接口异常"
SUCCESS_PROMPT = "签到成功啦！"
FAILED_PROMPT = "签到失败啦！"
PERMISSION_ERROR_PROMPT = "目前还没有你的数据哟，请先联系管理员~"
NOT_EXIST_PROMPT = "目前OSS还没有存你的数据哟~"
DOWNLOAD_FAILED_PROMPT = "签到成功~"
TWQD_ARGS_ERROR_PROMPT = "请输入正确的学号~"

ADDUSER_ARGS_PROMPT = "[学号，密码，邮箱]"
ADDUSER_SID_PROMPT = "请查看邮箱输入SID"
ADDUSER_ACCOUNT_EXIST_PROMPT = "用户已存在"
ADDUSER_ACCOUNT_ERROR_PROMPT = "用户名或密码错误"
ADDUSER_EMAIL_ERROR_PROMPT = "email错误"
ADDUSER_TOKEN_ERROR_PROMPT = "token错误"
ADDUSER_EMAIL_SEND_ERROR_PROMPT = "邮件发送错误"
ADDUSER_SUCCESS_PROMPT = "添加成功"
ADDUSER_SID_ERROR_PROMPT = "SID错误"

TWQDALL_SUCCESS_PROMPT = "签到完成啦！"
TWQDALL_RUNNING_PROMPT = "正在为您签到"
TWQDALL_NOT_IN_DATASET_PROMPT = "目前数据库没有你的数据哟"
TEQDALL_STUNUM_PROMPT = "你的学号是"

QUERY_ARGS_PROMPT = "学号 {}, 或 QQ {}"
QUERY_NO_DATA_PROMPT = "未查询到该用户"
QUERY_DATA_FORMAT = "学号:{}, QQ:{}"
QUERY_NO_SUCH_TYPE_PROMPT = "没有该类型数据"

ADD_ARGS_PROMPT = "[QQ, 学号]"

SEND_LOG = False
EXCEPTION_ADMIN = config.EXCEPTION_ADMIN

osh_status_code = {
    # 应立即结束任务
    900: '任务劫持。该用户今日签到数据已在库',
    901: '任务待提交。今日签到任务已出现，但未抵达签到开始时间。',

    # 应直接在当前列表调用截图上传模块
    902: '任务已提交。任务状态显示用户已签到。',

    # 调用主程序完成签到任务
    903: '任务待提交。任务出现并抵达开始签到时间。',
    904: '',

    # 任务句柄
    300: '任务提交成功。通过OSH签到成功。',
    301: '任务提交失败。出现未知错误。',
    302: '任务提交失败。重试次数超过阈值',
    303: '任务提交失败。Selenium操作超时',
    304: '任务提交失败。该用户不使用网服大厅进行签到。具体表现为日期范围内的打卡任务全为空。',
    305: '任务提交失败。T_STU_TEMP_REPORT_MODIFY 返回值为0。',

    306: '任务解析异常。Response解析json时抛出的JSONDecodeError错误，根本原因为返回的datas为空。可能原因为：接口变动，网络超时，接口参数变动等。',
    310: '任务重置成功。使用Response越权操作，重置当前签到任务。',

    400: '刷新成功。成功获取Superuser Cookie!',
    401: '登录失败。AdminCookie stale! 超级用户COOKIE过时/错误/文件不在目标路径。',
    402: '登录失败。OSH_IP 可能已被封禁！',
    403: '更新失败。MOD_AMP_AUTH获取异常，可能原因为登陆成功但未获取关键包',

    500: '体温截图上传成功。',
    501: '体温截图获取失败。可能原因为上传环节异常或登录超时（账号有误，操作超时）'
}
