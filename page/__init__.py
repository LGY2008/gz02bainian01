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
