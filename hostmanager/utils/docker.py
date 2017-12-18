
from servermanager import settings
import shell

class DockerCompose(object):
    def __init__(self, application, environment):
        self._app = application
        self._env = environment
        self._path = '%s/projects/%s/%s' % (settings.config.get('base_dir'), environment.name, application.name)

    def up(self):
        shell.execute_shell_cmd('docker-compose up', working_dir=self._path)

    def down(self):
        shell.execute_shell_cmd('docker-compose down', working_dir=self._path)

    def start(self):
        shell.execute_shell_cmd('docker-compose start', working_dir=self._path)

    def stop(self):
        shell.execute_shell_cmd('docker-compose stop', working_dir=self._path)
