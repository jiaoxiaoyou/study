"""
@Author : jiaojie
@Time : 2020/4/4 21:02
@Desc : 
"""

import pytest

@pytest.fixture
def error_fixture():
    assert 0

def test_ok():
    print("ok")

def test_fail():
    assert 0

def test_error(error_fixture):
    pass

def test_skip():
    pytest.skip("skipping this test")

def test_xfail():
    pytest.xfail("xfailing this test")

@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass