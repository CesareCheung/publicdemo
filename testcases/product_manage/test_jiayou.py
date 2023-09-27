import time

import pytest

from common.common_util import CommonUtil


# def read_yaml():
#     return ['测试1', '测试2', '测试3']
#
#
# # 把值传到Fixtrue是通过在fixtrue函数的参数里面加入request来接收参数。然后通过request.param来取值(固定写法)
# @pytest.fixture(scope="function", autouse=False, params=read_yaml(),name="db")
# def exe_database_sql(request):
#     print("链接数据库")
#
#     yield request.param
#     # yield 之后执行
#     print("关闭数据库链接---success")


class Testjiayou(CommonUtil):

    def test_baidu(self):
        # time.sleep(3)
        print("百度测试")
        # raise Exception("百度测试失败")


    def test_alibaba(self):
        # time.sleep(3)
        print("阿里测试")

    @pytest.mark.smoke
    def test_wangyi(self, login):
        # time.sleep(3)
        print("网易测试"+login)

    @pytest.mark.smoke
    def test_sql(self, login):
        print("执行SQL查询"+login)
        # print(exe_database_sql)
