
import yaml
import os

class Config(object):

    def __init__(self):

        self._config = dict()
        self._load_static_configuration()
        # self._load_dynamic_configuration()

    def get(self, path, default=None):
        if path not in self._config:
            return default
        if not self._config[path]:
            return default
        return self._config[path]

    def _load_static_configuration(self):

        # load environment configuration
        self._config['base_dir'] = os.environ.get('BASE_DIR',
                                                  os.path.dirname(
                                                          os.path.dirname(
                                                                  os.path.dirname(os.path.abspath(__file__)))))
        self._config['debug'] = os.environ.get('DEBUG', True)
        self._config['db_type'] = os.environ.get('DB_TYPE', 'sqlite')
        self._config['db_host'] = os.environ.get('DB_HOST', True)
        self._config['db_port'] = os.environ.get('DB_PORT', True)
        self._config['db_user'] = os.environ.get('DB_USER', True)
        self._config['db_pass'] = os.environ.get('DB_PASS', True)
        self._config['db_name'] = os.environ.get('DB_NAME', True)

    def _load_dynamic_configuration(self):
        # load configuration file
        with(open('%s/core/config/config.yml' % self._config['app_root'])) as config_file:
            # config = json.loads(config_file.read())
            config = yaml.load(config_file)
            print('config.yml read:')
            print('%s\n' % config)
