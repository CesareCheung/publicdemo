import pytest
@pytest.fixture(scope='function',autouse=True,name='pm')
def product_manage():
    print("商品管理之前")
    yield "商品管理"
    print("商品管理之后")






# import pytest
# def read_yaml():
#     return ['测试1', '测试2', '测试3']
#
#
# # 把值传到Fixtrue是通过在fixtrue函数的参数里面加入request来接收参数。然后通过request.param来取值(固定写法)
# @pytest.fixture(scope="function", autouse=False, params=read_yaml(),name='dbs')
# def exe_database_sql(request):
#     print("链接数据库")
#
#     yield request.param
#     # yield 之后执行
#     print("关闭数据库链接---success")