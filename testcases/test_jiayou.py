import time

import pytest

from common.common_util import CommonUtil


class TestJiayou(CommonUtil):

    def test_baidu1(self):
        # time.sleep(3)
        print("百度测试1")
        # raise Exception("百度测试1失败")

    # @pytest.mark.smoke
    def test_alibaba1(self):
        # time.sleep(3)
        print("阿里1测试")

    # @pytest.mark.smoke
    def test_wangyi1(self):
        # time.sleep(3)
        print("网易1测试")
