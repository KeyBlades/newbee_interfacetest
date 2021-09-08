from data.test_data import pre_requests_id
import requests


class Test_Pre_Requests:
    def test_pre_requests(self, handler, login):
        method, url, data, header, expect = handler.get_params(pre_requests_id)
        header.update({"token": login})
        req_txt = requests.request(method, url, data=data, headers=header)
        expect_value = expect
        try:
            assert expect_value in req_txt.text
            print("测试成功")
            handler.write(pre_requests_id, 'Passed')
        except AssertionError:
            print("测试失败")
            handler.write(pre_requests_id, 'Failed')
