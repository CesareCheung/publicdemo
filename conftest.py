import pytest


@pytest.fixture(scope="function", autouse=True, name='login')
def login_ecshop():
    print("登录前")

    yield "登录成功！"
    # yield 之后执行
    print("登录后")

@pytest.fixture(scope="session", autouse=True, name='all')
def all_exe():
    print("all_exe前")

    yield "登录成功！"
    # yield 之后执行
    print("all_exe后")
