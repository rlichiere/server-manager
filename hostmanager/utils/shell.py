import os
import subprocess

from servermanager import settings


def get_free_memory():
    cmd = 'free -m'
    if settings.config.get('use_windows_host_profile'):
        cmd = 'wmic os get freephysicalmemory /format:value'
    try:
        return execute_cmd(cmd)
    except Exception as e:
        print 'get_free_memory: ERROR : %s' % e.message
        return 'ERROR %s' % e.message


def execute_cmd(command, working_dir=None, host_fqdn=None, host_port=None):
    print '_exec_cmd: command : %s' % command

    if host_fqdn:
        if not host_port:
            host_port = settings.config.get('host_port', 22)
        os.environ['DOCKER_HOST'] = "%s:%s" % (host_fqdn, host_port)

    if working_dir:
        print '_exec_cmd: working_dir : %s' % working_dir
        p = subprocess.Popen(command, cwd=working_dir, stdout=subprocess.PIPE, shell=True)
    else:
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    result_status = p.wait()
    print '_exec_cmd: result_status : %s' % result_status

    result_err = None
    result_out = None
    if result_status == 1:
        print '_exec_cmd: *** error found'
        if p.stderr:
            result_err = p.stderr.readlines()
        if p.stdout:
            result_out = p.stdout.readlines()
    elif result_status == 0:
        if p.stdout:
            result_out = p.stdout.readlines()
    else:
        print '_exec_cmd: *** warning : unknown status : %s' % result_out

    if result_err:
        print '_exec_cmd: error :'
        print '_exec_cmd: result_err : %s' % result_err
        print '_exec_cmd: result_out : %s' % result_out
    else:
        print '_exec_cmd: *** ok : (result_err : %s)' % result_err
        print '_exec_cmd: result_out : %s' % result_out

    return result_out
