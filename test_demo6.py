import allure
import pytest


class Test_allure:
    def setup(self):
        pass

    def teardown(self):
        pass

    @allure.step('我是测试步骤001')
    @allure.testcase('http://www.baidu.com')
    @allure.issue('http://www.baidu.com')
    def test_al(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 0
