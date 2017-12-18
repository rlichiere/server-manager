
from servermanager import settings
import shell

class DockerCompose(object):
    def __init__(self, application, environment):
        self._app = application
        self._env = environment
        self._path_old = '%s/projects/%s/%s' % (settings.config.get('base_dir'), environment.name, application.name)
        self._path = '%s/%s/%s' % (settings.config.get('projects_dir'), environment.name, application.name)
        self._host_fqdn = settings.config.get('host_fqdn')

    def up(self):
        self._send_cmd('docker-compose up -d')

    def down(self):
        self._send_cmd('docker-compose down')

    def build(self):
        self._send_cmd('docker-compose build')

    def start(self):
        self._send_cmd('docker-compose start')

    def stop(self):
        self._send_cmd('docker-compose stop')


    def _send_cmd(self, command):
        print 'DockerCompose._send_cmd: command : %s' % command
        print 'DockerCompose._send_cmd: self._path_old : %s' % self._path_old
        print 'DockerCompose._send_cmd: self._path : %s' % self._path
        shell.execute_cmd(command, working_dir=self._path, host_fqdn=self._host_fqdn)
