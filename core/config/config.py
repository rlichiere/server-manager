
import yaml
import os

import core.utils as core_utils


class Config(object):

    def __init__(self):

        self._config = dict()
        self._load_environment_configuration()
        self._load_file_configuration()
        # self._load_dynamic_configuration()

    def get(self, path, default=None):
        if path not in self._config:
            return default
        if not self._config[path]:
            return default
        return self._config[path]

    def _load_environment_configuration(self):

        # load environment configuration
        self._config['base_dir'] = os.environ.get('BASE_DIR',
                                                  os.path.dirname(
                                                          os.path.dirname(
                                                                  os.path.dirname(os.path.abspath(__file__)))))
        self._config['debug'] = True if os.environ.get('DEBUG', 'True') == 'True' else False
        self._config['secret_key'] = os.environ.get('SECRET_KEY', core_utils.generate_secret_key())
        self._config['db_type'] = os.environ.get('DB_TYPE', 'sqlite')
        self._config['db_host'] = os.environ.get('DB_HOST', False)
        self._config['db_port'] = os.environ.get('DB_PORT', False)
        self._config['db_user'] = os.environ.get('DB_USER', False)
        self._config['db_pass'] = os.environ.get('DB_PASS', False)
        self._config['db_name'] = os.environ.get('DB_NAME', False)


    def _load_file_configuration(self):
        print('_load_file_configuration...')
        def _replace_keys_from_file(data, file_path):
            settings = yaml.load(open(file_path))
            data.update(settings)

        public_path = '%s/core/config/config.yml' % self._config['base_dir']
        _replace_keys_from_file(self._config, public_path)

        private_path = '%s/core/config/config_private.yml' % self._config['base_dir']
        _replace_keys_from_file(self._config, private_path)

        print('_load_file_configuration.')

    def _load_dynamic_configuration(self):
        # load configuration file
        with(open('%s/core/config/config.yml' % self._config['app_root'])) as config_file:
            # config = json.loads(config_file.read())
            config = yaml.load(config_file)
            print('config.yml read:')
            print('%s\n' % config)
