
import yaml
import os

import core.utils as core_utils


class Config(object):

    def __init__(self):
        self._config = dict()
        self._load_complete_configuration()

    def get(self, path, default=None):
        if path not in self._config:
            return default
        if not self._config[path]:
            return default
        return self._config[path]

    @property
    def get_config(self):
        return self._config

    def get_basic_configuration(self):
        print('Config.get_basic_configuration...')
        conf = dict()
        conf['debug'] = False
        conf['base_dir'] = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).replace('\\','/')
        conf['static_root'] = '%s/static/' % conf['base_dir']
        conf['db_type'] = 'sqlite'
        print('Config.get_basic_configuration.')
        return conf

    def get_environment_configuration(self):
        print('Config.get_environment_configuration...')
        conf = dict()

        _base_dir = os.environ.get('BASE_DIR', None)
        if _base_dir:
            conf['base_dir'] = _base_dir

        _debug = os.environ.get('DEBUG', None)
        if _debug:
            conf['debug'] = _debug

        _static_root = os.environ.get('STATIC_ROOT', None)
        if _static_root:
            conf['static_root'] = _static_root

        _secret_key = os.environ.get('SECRET_KEY', None)
        if _secret_key:
            conf['secret_key'] = _secret_key

        _db_type = os.environ.get('DB_TYPE', None)
        if _db_type:
            conf['db_type'] = _db_type

        _db_host = os.environ.get('DB_HOST', None)
        if _db_host:
            conf['db_host'] = _db_host

        _db_port = os.environ.get('DB_PORT', None)
        if _db_port:
            conf['db_port'] = _db_port

        _db_user = os.environ.get('DB_USER', None)
        if _db_user:
            conf['db_user'] = _db_user

        _db_pass = os.environ.get('DB_PASS', None)
        if _db_pass:
            conf['db_pass'] = _db_pass

        _db_name = os.environ.get('DB_NAME', None)
        if _db_name:
            conf['db_name'] = _db_name

        print('Config.get_environment_configuration.')
        return conf

    def get_file_configuration(self, file_path):
        print('Config.get_file_configuration...')
        conf = yaml.load(open(file_path))
        print('Config.get_file_configuration.')
        return conf

    def get_files_configuration(self):
        print('Config.get_files_configuration...')
        conf = dict()
        for conf_file in self.get_config_file_list:
            conf.update(self.get_file_configuration(conf_file['path']))
        print('Config.get_files_configuration.')
        return conf

    def get_database_configuration(self):
        return dict()

    def _load_complete_configuration(self):
        self._config.update(self.get_basic_configuration())
        self._config.update(self.get_environment_configuration())
        self._config.update(self.get_files_configuration())
        self._config.update(self.get_database_configuration())

        if 'secret_key' not in self._config:
            self._config['secret_key'] = core_utils.generate_secret_key()

    @property
    def get_config_file_list(self):
        return [
            {'key': 'config',         'path': '%s/core/config/config.yml'    % self._config['base_dir']},
            {'key': 'config_private', 'path': '%s/config/config_private.yml' % self._config['base_dir']},
        ]
