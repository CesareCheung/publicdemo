# import time
#
# import pytest

from common.common_util import CommonUtil


class TestApi(CommonUtil):
    def test_gettoken(self,login,um):
        print("获取token"+login,um)
