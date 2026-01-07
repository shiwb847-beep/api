import allure
import pytest

from data.user_login import User


@allure.feature("API测试")
class TestAPI:


    @allure.story("登录")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("data", User.login_data)
    def test_login(self, api_client, data):
        #动态title
        allure.dynamic.title(data["title"])
        with allure.step("发送POST请求进行登录"):
            response = api_client.post("/api/user/login", data=data)
        with allure.step("状态码"):
            assert response.status_code == 200
        with allure.step("响应结果"):
            assert response.json()["msg"] in data["msg"]
