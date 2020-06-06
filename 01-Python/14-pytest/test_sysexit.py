"""
@Author : jiaojie
@Time : 2020/3/23 21:52
@Desc : 
"""

import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()