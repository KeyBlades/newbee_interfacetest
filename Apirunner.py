import pytest
import subprocess
from common.base.get_config import cf
test_result_dir = cf.json_dir_path
test_report_dir = cf.html_dir_path


if __name__ == '__main__':
    args = ['-s', '-q', '--setup-show', '--alluredir', test_result_dir]
    pytest.main(args)
    subprocess.call('allure generate %s -o %s --clean' % (test_result_dir, test_report_dir), shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 9999 %s' % test_report_dir, shell=True)
