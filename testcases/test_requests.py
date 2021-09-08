from data.test_data import requests_id
import requests
import pytest


class Test_Requests:
    @pytest.mark.parametrize('case_id', requests_id)
    def test_requests(self, handler, case_id):
        method, url, data, header, expect = handler.get_params(case_id)
        req_txt = requests.request(method, url, data=data, headers=header)
        expect_value = expect
        try:
            assert expect_value in req_txt.text
            print("测试成功")
            handler.write(case_id, 'Passed')
        except AssertionError:
            print("测试失败")
            handler.write(case_id, 'Failed')
