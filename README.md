# **一、使用fixtrue实现部分前后置：**

@pytest.fixture(scope=None.autouse=Falseparams=None,ids=None,name=None)
* scope : 作用域：
 function:在函数之前和之后执行
如果说fixtrue有通过return或yield返回值的，那么可以把这个值传递到测试用例当中,值是通过固件名称传递的
class : 在类之前和之后执行
手动调用的方式是在类的上面加上@pvtestmarkusefixtures("exe database sql")装饰器调用
package/session :在整个项目会话之前和之后执行
一般结合conftest.py文件来实现

* autouse: 自动执行。默认是False
@pytest.fixture(scope-"function",autouseTrue)
def exe_database_sq1():
    print(“执行SQL查询")
    yield

    如果希望在另外一个py文件中调用需要结合contest.py文件使用

* params: 实现参数化
如何把值传到Fixtrue是通过在fixtrue函数的参数里面加入request来接收参数。然后通过request.param来取值。(这里的param没有s)
def read_yaml():
    return ['测试1','测试2','测试3']

@pytest.fixture(scope="function",autouse=False,params=read yaml())
 def exe_database_sql(request):
    print(request.param)
    print(“执行SQL查调")
    yield "success"
    print(”关闭数据库连接”)

* ids：不能单独使用，必须合params一起使用，作用是对参数起别名
@pytest.fixture(scope="function",autouse=False,params=read _yaml(),ids=['c','z','cai'])
 def exe database sql(request):
    print("执行SQL查询”)
    yield requestparam
    print("关闭数据库连接”)

* name ：给fixture起别名
特别注意:一旦使用了别名，那么fixtrue的名称就不能再用了，只能用别名。
@pytest.fixture(scope="function",autouse=False,params=read _yaml(),ids=['c','z','cai'],name='db')
 def exe database sql(request):
    print("执行SQL查询”)
    yield requestparam
    print("关闭数据库连接”)

# **二、fixture结合conftest.py文件使用**

* conftest.py是专门用于存放fixtrue的配置文件，名称是固定的不能变
* 在conftestpy文件里面所有的方法在调用时都不需要导包。
* conftestpy文件可以有多个，并且多个confitestpy文件里面的多个fixtrue且可以被一个用例调用