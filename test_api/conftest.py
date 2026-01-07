# conftest.py
import pytest
import allure
from utils.api_client import APIClient
from config import Config

@pytest.fixture(scope="session")
def api_client():
    """API客户端fixture"""
    client = APIClient(base_url=Config.BASE_URL)
    yield client

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """为失败的测试用例添加截图"""
    if call.when == "call":
        if call.excinfo is not None:
            # 添加失败信息到allure报告
            allure.attach(
                str(call.excinfo.value),
                name="Exception Info",
                attachment_type=allure.attachment_type.TEXT
            )
