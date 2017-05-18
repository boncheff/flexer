import os

CONFIG_FILE = os.path.expanduser('~/.flexer.json')
DEFAULT_CMP_URL = 'https://portal.ntt.eu/cmp/basic/api'
DEFAULT_ACCOUNT_YAML = os.path.join(os.getcwd(), "account.yaml")


class Config(object):
    CMP_URL = os.getenv('CMP_URL', 'http://localhost/cmp/api')
    CMP_USERNAME = os.getenv('CMP_USERNAME', '')
    CMP_PASSWORD = os.getenv('CMP_PASSWORD', '')
    CMP_ACCESS_TOKEN = os.getenv('CMP_ACCESS_TOKEN', '')
    NFLEX_CODEDIR = os.getenv('NFLEX_CODEDIR', '/sandbox')
    MODULE_ID = os.getenv('NFLEX_MODULE_ID')


class TestingConfig(Config):
    NFLEX_CODEDIR = '/tmp'
