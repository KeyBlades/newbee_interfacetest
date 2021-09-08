import logging
from common.base.get_config import cf

logger = logging.getLogger()
logger.setLevel(logging.INFO)

log_format = logging.Formatter('%(asctime)s%(filename)s[line:%(lineno)d]%(levelname)s:%(message)s')

fh = logging.FileHandler(filename=cf.log_dir_path, mode='a', encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(log_format)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(log_format)
logger.addHandler(ch)
