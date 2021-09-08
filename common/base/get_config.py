import os
import configparser
import sys


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
config_file_path = os.path.abspath(os.path.join(BASE_DIR, 'common/config/config.ini'))


class Config:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.json_dir_path = self.read_config('report', 'json_dir_path')
        self.html_dir_path = self.read_config('report', 'html_dir_path')
        self.data_dir_path = self.read_config('data', 'data_dir_path')
        self.log_dir_path = self.read_config('log', 'log_dir_path')

    def read_config(self, field, key):
        try:
            self.cf.read(config_file_path, encoding='utf-8')
            result = self.cf.get(field, key).replace('base_dir', str(BASE_DIR))
            if ':' in result:
                result = result.replace('/', '\\')
        except Exception as e:
            print(e)
            sys.exit(1)
        return result


cf = Config()

if __name__ == '__main__':
    cf = Config()
    print('json_dir_path: ', cf.json_dir_path)
    print('html_dir_path: ', cf.html_dir_path)
    print('data_dir_path: ', cf.data_dir_path)
    print('log_dir_path: ', cf.log_dir_path)
