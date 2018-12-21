"""
    目标：实现地址管理 -新增地址
"""
import os
import sys
sys.path.append(os.getcwd())

from base.read_yaml import ReadYaml
import allure
import pytest
from page.page_in import PageIn


def get_data(data_type):
    # 定义空数组
    arrs = []
    if data_type == "add":
        for data in ReadYaml("address_data.yaml").read_yaml().get("add_address").values():
            (arrs.append(
                        (data.get("name"),data.get("phone"),data.get("province"),
                         data.get("city"),data.get("area"),data.get("address_info"),
                         data.get("code"))
                        )
            )
        return arrs
    elif data_type == "update":
        for data in ReadYaml("address_data.yaml").read_yaml().get("update_address").values():
            (arrs.append(
                        (data.get("name"),data.get("phone"),data.get("province"),
                         data.get("city"),data.get("area"),data.get("address_info"),
                         data.get("code"))
                        )
            )
        return arrs


# 建类


class TestAddress():
    # setup_class
    @allure.step("初始化操作 setup_class")
    def setup_class(self):
        # 获取 统一入口类
        pagein = PageIn()
        # 获取 PageLogin对象 并调用登录方法
        pagein.page_get_pagelogin().page_login()
        # 获取 PageAddress对象
        self.address = pagein.page_get_pageaddress()
        # 点击地址管理
        self.address.page_click_address_manage()

    # teardown_class
    @allure.step("结束操作 teardown_class")
    def teardown_class(self):
        self.address.driver.quit()

    # test_add_address
    @allure.step("测试用例：新增地址")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,phone,province,city,area,address_info,code", get_data("add"))
    def test_add_address(self, name, phone, province, city, area, address_info, code):
        # 由于多次调用，修改变量简易度
        address = self.address
        # 1. 点击 新增地址
        address.page_click_new_address()
        # 2. 输入 收件人
        address.page_input_receipt_name(name)
        # 3. 输入 电话
        address.page_input_phone(phone)
        # 4. 点击 区域 非直辖市(区域、省、市、区)
        address.page_click_address_area(province, city, area)
        # 4. 点击 区域直辖市
        # address.page_click_address_area2(province, city, area)
        # 5. 输入 详细地址
        address.page_input_detail_address(address_info)
        # 6. 输入 邮编
        address.page_input_post_code(code)
        # 7. 点击 设为默认地址
        address.page_click_default_address()
        # 8. 点击保存
        address.page_click_save_btn()
        # 组装 断言所需 预期格式
        expect_result = name + "  " + phone

        # print("组装的预期格式为：", expect_result)
        # print("通过函数获取地址列表内所有的收件人：", address.page_get_list_name_phone())
        try:
            assert expect_result in address.page_get_list_name_phone()
        except AssertionError:
            # 截图
            address.base_get_image()
            # 打开图片
            with open("./image/faild.png", "rb") as f:
                # 写入报告
                allure.attach("失败原因", f.read(), allure.attach_type.PNG)

    @allure.step("测试用例：更新地址")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,phone,province,city,area,address_info,code", get_data("update"))
    def test_update_address(self, name, phone, province, city, area, address_info, code):
        # 点击 编辑
        self.address.page_click_edit_btn()
        # 修改 操作
        self.address.page_click_update_btn(name, phone, province, city, area, address_info, code)
        # 断言
        # 组装 断言所需 预期格式
        expect_result = name + "  " + phone
        try:
            assert expect_result in self.address.page_get_list_name_phone()
        except AssertionError:
            # 截图
            self.address.base_get_image()
            # 打开图片
            with open("./image/faild.png", "rb") as f:
                # 写入报告
                allure.attach("失败原因", f.read(), allure.attach_type.PNG)

    @allure.step("测试用例：删除地址")
    @pytest.mark.run(order=3)
    def test_delete_address(self):
        # 删除地址操作
        self.address.page_delete_address()
        # 断言 是否删除干净
        assert self.address.page_is_delete()