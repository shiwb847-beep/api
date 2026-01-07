import os

import pytest

if __name__ == "__main__":
    pytest.main()
    # 生成报告
    os.system("allure generate reporters/temp -o reporters/html --clean")
    # 启动报告
    os.system("allure serve reporters/temp")