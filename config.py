# config.py
import os

class Config:
    # 基础URL
    BASE_URL = "http://sky.nnzhp.cn"
    #项目根路径
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    # 测试数据路径
    TEST_DATA_PATH = os.path.join(PROJECT_ROOT, "data")
    # 日志配置
    LOG_LEVEL = os.path.join(PROJECT_ROOT, "info")
    LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

    # 测试环境配置
    ENVIRONMENT = os.path.join(PROJECT_ROOT, "test")

    # 请求超时时间
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))


