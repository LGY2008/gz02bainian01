from selenium.webdriver.common.by import By

"""
    百年奥莱-登录页面配置数据
"""
# 点击我
login_click_me = By.ID, "com.yunmall.lc:id/tab_me"
# 点击已有账号，去登录
login_username_link = By.ID, "com.yunmall.lc:id/textView1"
# 输入用户名
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
login_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 设置
login_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 消息推送
login_msg_send = By.ID, "com.yunmall.lc:id/setting_notification"
# 修改密码
login_update_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 点击退出
login_click_logout = By.ID, "com.yunmall.lc:id/setting_logout"
# 确认退出
login_logout_ok = By.ID, "com.yunmall.lc:id/ymdialog_right_button"


"""以下数据为 地址管理配置数据"""
# 地址管理
address_manage = By.ID,"com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_add_new_btn = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name = By.ID , "com.yunmall.lc:id/address_receipt_name"
# 电话
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 所在区域
address_area = By.ID, "com.yunmall.lc:id/address_province"
# 省  id重复 只能使用text
shi_kuang = By.CLASS_NAME, "android.widget.RelativeLayout"
# 市  class = "android.widget.RelativeLayout"
shi = By.ID ,"com.yunmall.lc:id/area_title"
# 区 使用 text

# 输入详细地址
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 输入邮编
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_save = By.ID, "com.yunmall.lc:id/button_send"
# 收件人+电话
address_name_and_phone = By.ID, "com.yunmall.lc:id/receipt_name"
# 确认删除
address_delete_ok = By.ID, "com.yunmall.lc:id/ymdialog_left_button"