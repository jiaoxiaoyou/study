"""
@Author : jiaojie
@Time : 2020/3/23 21:57
@Desc : 
"""

class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')