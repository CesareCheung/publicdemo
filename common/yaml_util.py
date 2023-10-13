
# 读取yaml文件,需要pip install pyyaml
import os.path

import yaml


#获取项目根路径

def get_obj_path():
    return os.path.dirname(__file__).split('common')[0]


def read_yaml(yamlpath):
    with open(get_obj_path()+yamlpath,"r",encoding='utf-8') as f:
        vaule=yaml.load(stream=f,Loader=yaml.FullLoader)
        return vaule

if __name__ == '__main__':
    # print(get_obj_path())
    print(read_yaml("testcases/user_manage/get_token.yaml"))