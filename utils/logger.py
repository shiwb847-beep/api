# utils/logger.py
import logging
import os
from datetime import datetime

def setup_logger(name='api_test', log_file=None, level=logging.INFO):
    """
    设置日志记录器
    :param name: logger名称
    :param log_file: 日志文件路径
    :param level: 日志级别
    :return: logger实例
    """
    if not log_file:
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, f"api_test_{datetime.now().strftime('%Y%m%d')}.log")

    # 创建logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 避免重复添加handler
    if not logger.handlers:
        # 创建文件handler
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(level)

        # 创建控制台handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # 设置日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 添加handler到logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
