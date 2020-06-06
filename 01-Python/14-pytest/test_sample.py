"""
@Author : jiaojie
@Time : 2020/3/23 21:46
@Desc : 
"""

#import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

# if __name__ == '__main__':
#     pytest.main()