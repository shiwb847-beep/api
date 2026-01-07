# utils/http_logger.py
import functools
import json
from .logger import setup_logger

logger = setup_logger()

def log_http_request(func):
    """
    HTTP请求日志装饰器
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 记录请求信息
        method = func.__name__.upper()
        url = args[1] if len(args) > 1 else kwargs.get('url', '')

        logger.info(f"HTTP Request: {method} {url}")
        if 'data' in kwargs:
            logger.info(f"Request Data: {json.dumps(kwargs['data'], ensure_ascii=False, indent=2)}")
        if 'headers' in kwargs:
            logger.info(f"Request Headers: {json.dumps(kwargs['headers'], ensure_ascii=False, indent=2)}")

        # 执行请求
        response = func(*args, **kwargs)

        # 记录响应信息
        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Headers: {json.dumps(dict(response.headers), ensure_ascii=False, indent=2)}")
        logger.info(f"Response Body: {response.text[:500]}...")  # 只记录前500字符

        return response

    return wrapper
