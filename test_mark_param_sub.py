# import pytest
#
#
#
# def f():
#     raise SystemExit(1)
#
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()
#
#
# def myfunc():
#     #引起值错误
#     raise ValueError("返回40013支付错误")
#
#
# def test_match():
#     # 当调用myfunc()
#     # 时出现值错误是正确的，
#     # 值的信息保存到excinfo中，并且可能断言值中的属性value的内容
#
#
#     with pytest.raises(ValueError) as excinfo:
#         myfunc()
#         assert '40013' in str(excinfo.value)
#
# def read_excel():
#     # 从数据库或者 excel 文件中读取设备的信息，这里简化为一个列表
#     for dev in ['dev1', 'dev2', 'dev3']:
#         yield dev
#
#
# @pytest.mark.parametrize('dev', read_excel())
# def test_sample(dev):
#     assert dev
#
# @pytest.mark.parametrize(
#     ('n', 'expected'),
#     [(4, 2),
#     pytest.param(6, 3, marks=pytest.mark.xfail(), id='XPASS')])
# def test_params(n, expected):
#     assert n / 2 == expected #执行结果如下，显示是XPASS。
#
# @pytest.mark.parametrize("test_input,expected",[("3+5",8 ),
#                                                 ("2+5", 7),
#                                                 pytest.param("6*9", 42, marks=pytest.mark.xfail),
#                                                 ])
# def test_eval(test_input, expected):
#     # eval将字符串str当成有效的表达式来求值并返回计算结果
#     assert eval(test_input) == expected