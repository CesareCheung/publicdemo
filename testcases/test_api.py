import time

import pytest

from common.common_util import CommonUtil


def read_yaml():
    return ['测试1', '测试2', '测试3']


# 把值传到Fixtrue是通过在fixtrue函数的参数里面加入request来接收参数。然后通过request.param来取值(固定写法)
@pytest.fixture(scope="function", autouse=False, params=read_yaml())
def exe_database_sql(request):
    print("链接数据库")

    yield request.param
    # yield 之后执行
    print("关闭数据库链接---success")


class TestApi(CommonUtil):

    def test_baidu(self):
        # time.sleep(3)
        print("百度测试")
        # raise Exception("百度测试失败")

    @pytest.mark.smoke
    def test_alibaba(self):
        # time.sleep(3)
        print("阿里测试")

    @pytest.mark.smoke
    def test_wangyi(self, exe_database_sql):
        # time.sleep(3)
        print("网易测试"+exe_database_sql)

    @pytest.mark.smoke
    def test_sql(self, exe_database_sql):
        print("执行SQL查询"+exe_database_sql)
        # print(exe_database_sql)
