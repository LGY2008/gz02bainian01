
"""
    目标：统一入口类实现
    操作：
        需要获取几个对象，封装几个方法
"""
import allure

from base.get_driver import get_driver
from page.page_address import PageAddress
from page.page_login import PageLogin

# 获取driver
driver=get_driver()

# 建类
class PageIn():
    # 获取登录页面对象
    @allure.step("实例化登录页面对象")
    def page_get_pagelogin(self):
        return PageLogin(driver)

    # 获取地址管理页面对象
    @allure.step("实例化地址管理对象")
    def page_get_pageaddress(self):
        return PageAddress(driver)