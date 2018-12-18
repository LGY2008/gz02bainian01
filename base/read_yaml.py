"""
    目标：yaml文件读取
    操作：
        1. 导入 yaml
        2. 打开文件
        3. 调用 load方法
"""
import yaml
import os


class ReadYaml():
    def __init__(self,filename):
        self.filename=os.getcwd()+os.sep+"data"+os.sep+filename

    # 以下方法 给pytest使用
    def read_yaml(self):
        # 打开文件
        with open(self.filename, "r", encoding="utf-8")as f:
            # 调用load方法
            return yaml.load(f)


    # 使用固定路径，只能右键调试使用。
    def read_yaml_1(self):
        # 打开文件
        with open("../data/login_data.yaml", "r", encoding="utf-8")as f:
            # 调用load方法
            return yaml.load(f)

if __name__ == '__main__':
    arrs = []
    for data in ReadYaml(" ").read_yaml_1().values():
        arrs.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
    print(arrs)