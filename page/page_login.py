"""
    目标：百年奥莱 登录页面封装
    操作：
        1. 点击 我
		2. 点击已有已有账号去登录
		3. 输入用户名
		4. 输入密码
		5. 点击登录
		6. 获取昵称（断言）
"""
import allure
import page
from base.base import Base


# 建类
class PageLogin(Base):
    # 点击我
    @allure.step("点击我")
    def page_click_me(self):
        self.base_click(page.login_click_me)

    # 点击已有账号去登录
    @allure.step("点击已有账号去登录")
    def page_click_username_link(self):
        self.base_click(page.login_username_link)

    # 输入 用户名
    @allure.step("输入 用户名")
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入 密码
    @allure.step("输入 密码")
    def page_input_pwd(self, password):
        self.base_input(page.login_pwd, password)

    # 点击 登录按钮
    @allure.step("点击 登录按钮")
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取昵称
    @allure.step("获取昵称")
    def page_get_nickname(self):
        # 注意：一定要返回文本
        return self.base_get_text(page.login_nickname)

    # 点击 设置
    @allure.step("点击 设置")
    def page_click_setting(self):
        self.base_click(page.login_setting)

    # 拖拽
    @allure.step("执行拖拽--》发送消息 拖拽到 修改密码")
    def page_drag_and_drop(self):
        # 定位 推送消息
        el1 = self.base_find_element(page.login_msg_send)
        # 定位 修改密码
        el2 = self.base_find_element(page.login_update_pwd)
        # 调用 拖拽方法
        self.base_drag_and_drop(el1, el2)

    # 点击退出
    @allure.step("点击 退出")
    def page_click_logout_btn(self):
        self.base_click(page.login_click_logout)

    # 确认退出
    @allure.step("点击 确认退出")
    def page_click_logout_ok(self):
        self.base_click(page.login_logout_ok)

    # 封装整体 退出方法
    def page_logout(self):
        # 拖拽
        self.page_drag_and_drop()
        # 点击 退出
        self.page_click_logout_btn()
        # 确认 退出
        self.page_click_logout_ok()