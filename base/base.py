"""
    目标：完成po模式 base基类(工具类封装)
    操作：
        1. 根据业务逻辑梳理出，需要的公共方法
        2. 方法：
            1). 定位
            2). 输入
            3). 点击
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 新建类
class Base():
    def __init__(self, driver):
        self.driver = driver

    # 定位封装
    def base_find_element(self, loc, timeout=30, poll=0.5):
        # 显示等待
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入封装
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清空操作
        el.clear()
        # 输入操作
        el.send_keys(value)

    # 点击封装
    def base_click(self, loc):
        # 获取元素 并 点击
        self.base_find_element(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图
    def base_get_image(self):
        # 注意：使用pytest运行，所以这里要写./ 而非 ../
        self.driver.get_screenshot_as_file("./image/faild.png")

    # 拖拽
    def base_drag_and_drop(self,el1,el2):
        # 从el1 拖拽到 el2
        self.driver.drag_and_drop(el1,el2)

    # 获取toast封装
    def base_get_toast(self,msg):
        loc=By.XPATH,"//*[contains(@text,'"+msg+"')]"
        # 调用 查找元素方法 并返回text
        return self.base_find_element(loc,timeout=3,poll=0.1).text