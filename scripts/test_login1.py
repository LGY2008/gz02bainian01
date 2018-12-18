"""
    目标：百年奥莱登录 业务层实现
    操作：
        1. setup_class
                1). 实例化 统一入口类
                2). 获取登录页面对象
        2. teardown_class
                1). 关闭 driver
        3. test_login
                1). 根据业务流程
"""
import os
import sys
sys.path.append(os.getcwd())

import allure
from base.read_yaml import ReadYaml
import pytest
from page.page_in import PageIn


# 获取参数化格式函数
def get_data():
    # 定义空列表
    arrs = []
    # 遍历 拿取每一条用例数据
    for data in ReadYaml("login_data.yaml").read_yaml().values():
        # 将拿取出来的组装添加到列表，列表内嵌套元组
        arrs.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
    return arrs


# 建类
class TestLogin():
    # setup_class
    def setup_class(self):
        # 实例化 统一入口类
        self.login = PageIn().page_get_pagelogin()
        # 点击 我
        self.login.page_click_me()
        # 点击 已有账号，去登录
        self.login.page_click_username_link()

    # teardown_class
    def teardown_class(self):
        self.login.driver.quit()

    # test_login
    @pytest.mark.parametrize("username,password,expect_result,expect_toast", get_data())
    @allure.step("开始执行登录测试")
    def test_login(self, username, password, expect_result,expect_toast):
        login = self.login
        if expect_result:
            try:
                # 输入用户名
                # allure.attach("正在输入用户名:",username)
                login.page_input_username(username)
                # 输入密码
                # allure.attach("正在输入密码:", password)
                login.page_input_pwd(password)
                # 点击登录
                # allure.attach("点击登录按钮"," ")
                login.page_click_login_btn()
                # 获取昵称 + 断言
                # allure.attach("开始断言：", expect_result+"是否等于"+"获取的结果")
                assert expect_result in login.page_get_nickname()
                # 点击设置
                login.page_click_setting()
                # 点击退出
                login.page_logout()
                # 点击 我
                login.page_click_me()
                # 点击 已有账号，去登录
                login.page_click_username_link()
            except AssertionError:
                # 截图
                login.base_get_image()
                # 打开图片
                with open("./image/faild.png", "rb") as f:
                    # 写入报告
                    allure.attach("失败原因",f.read(),allure.attach_type.PNG)
        else:
            try:
                # 输入用户名
                login.page_input_username(username)
                # 输入密码
                login.page_input_pwd(password)
                # 点击登录
                login.page_click_login_btn()
                # 断言
                assert expect_toast in login.base_get_toast(expect_toast)
                # 以下断言为 调试写入报告使用
                # assert "登录密码错误1" in login.base_get_toast(expect_toast)
            except AssertionError:
                # 截图
                login.base_get_image()
                # 打开图片
                with open("./image/faild.png", "rb") as f:
                    # 写入报告
                    allure.attach("失败原因",f.read(),allure.attach_type.PNG)