
from servermanager import settings
import shell

class DockerCompose(object):
    def __init__(self, application, environment):
        self._app = application
        self._env = environment
        self._path = '%s/projects/%s/%s' % (settings.config.get('base_dir'), environment.name, application.name)

    def up(self):
        self._send_cmd('docker-compose up')

    def down(self):
        self._send_cmd('docker-compose down')

    def start(self):
        self._send_cmd('docker-compose start')

    def stop(self):
        self._send_cmd('docker-compose stop')

    def _send_cmd(self, command):
        shell.execute_cmd(command, working_dir=self._path, host_fqdn=settings.config.get('host_fqdn'))
