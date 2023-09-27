import pytest



@pytest.fixture(scope="function", autouse=True,name='um')
def user_manage(request):
    print("用户管理之前")

    yield "用户管理"
    # yield 之后执行
    print("用户管理之后")