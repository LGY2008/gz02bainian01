"""
    目标：实现地址管理 页面对象
    核心：
        1. 每一步为一个操作方法
        2. 继承 Base
"""
import allure

import page
from base.base import Base


# 建类
class PageAddress(Base):
    # 点击 地址管理
    @allure.step("点击 地址管理")
    def page_click_address_manage(self):
        self.base_click(page.address_manage)

    # 点击 新增地址
    @allure.step("点击 新增地址")
    def page_click_new_address(self):
        self.base_click(page.address_add_new_btn)

    # 收件人
    @allure.step("输入 收件人")
    def page_input_receipt_name(self, name):
        self.base_input(page.address_receipt_name, name)

    # 电话
    @allure.step("输入 电话")
    def page_input_phone(self, phone):
        self.base_input(page.address_add_phone, phone)

    # 点击 区域 非直辖市
    @allure.step("点击 区域")
    def page_click_address_area(self, province, city, area):
        # 点击 区域
        self.base_click(page.address_area)
        # 省 非直辖市
        self.base_text_click(province)
        # 市
        self.base_text_click(city)
        # 区
        self.base_text_click(area)

    # 点击 区域 直辖市  测试
    # def page_click_address_area2(self, province, city, area):
    #     # 点击 区域
    #     self.base_click(page.address_area)
    #     # 省 非直辖市
    #     self.base_text_click(province)
    #     # 点击 市的外框
    #     self.base_click(page.shi_kuang)
    #     # 市
    #     self.base_click(page.shi)
    #     # 区
    #     self.base_text_click(area)

    # 输入 详细地址
    @allure.step("输入详细地址")
    def page_input_detail_address(self, address_info):
        self.base_input(page.address_detail_addr_info, address_info)

    # 输入 邮编
    @allure.step("输入 邮编")
    def page_input_post_code(self, code):
        self.base_input(page.address_post_code, code)

    # 点击 设为默认地址
    @allure.step("点击 设为默认地址")
    def page_click_default_address(self):
        self.base_click(page.address_default)

    # 点击 保存
    @allure.step("点击 保存")
    def page_click_save_btn(self):
        self.base_click(page.address_save)

    # 获取地址列表内所有的收件和电话
    @allure.step("获取 地址列表内所有的收件和电话")
    def page_get_list_name_phone(self):
        # 获取当前地址列表内 所有的收件人和电话
        els = self.base_find_elements(page.address_name_and_phone)
        # 使用行内循环 返回格式： ["张三  18600001111", "李四  18611112222"]
        return [el.text for el in els]

    # 点击编辑
    @allure.step("点击 编辑")
    def page_click_edit_btn(self, text="编辑"):
        self.base_text_click(text)

    # 点击修改 默认点击第一个修改元素
    @allure.step("点击 点击修改")
    def page_click_update_btn(self, name, phone, province, city, area, address_info, code):
        # 点击修改
        self.base_click_elements("修改")
        # 输入收件人
        self.page_input_receipt_name(name)
        # 输入电话
        self.page_input_phone(phone)
        # 点击区域
        self.page_click_address_area(province, city, area)
        # 输入详细地址
        self.page_input_detail_address(address_info)
        # 输入邮编
        self.page_input_post_code(code)
        # 点击保存
        self.page_click_save_btn()

    # 确认删除
    @allure.step("点击 确认删除")
    def page_click_delete_ok(self):
        self.base_click(page.address_delete_ok)

    # 删除地址
    @allure.step("执行删除地址操作")
    def page_delete_address(self):
        # 获取地址列表长度
        for i in range(len(self.page_get_list_name_phone())):
            # 点击编辑
            self.page_click_edit_btn()
            # 获取删除 并点击
            self.base_click_elements("删除")
            # 确认删除
            self.page_click_delete_ok()

    # 判断是否 删除干净
    @allure.step("判断 是否删除干净")
    def page_is_delete(self):
        try:
            self.base_find_elements(page.address_name_and_phone,timeout=3)
            # 返回 False 说明未删除干净
            allure.attach("未删除干净", "")
            return False
        except:
            # 返回 True说明 删除成功！
            allure.attach("删除干净！","")
            return True