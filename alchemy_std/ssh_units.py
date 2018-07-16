
import logging

log = logging.getLogger(__name__)

def init_ssh_connection(host, username = None, password = None, port = 22):
    import paramiko
    from paramiko.client import SSHClient

    ssh_conn = SSHClient()
    ssh_conn.load_system_host_keys()
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_conn.connect(host, username = username, password = password)

    return {'ssh_conn': ssh_conn}

def ssh_runcmd(cmd, hostname = None, ssh_conn = None, username = None, password = None, port = 22, capture = False, fail=True):
    import paramiko
    from paramiko.client import SSHClient

    log.info("SSH CMD: %s", cmd)

    if ssh_conn is None:
        log.info("Creating SSH connection %s@%s", username, hostname)
        val = init_ssh_connection(hostname, username=username, password=password, port=port)
        ssh_conn = val['ssh_conn']

    chan = ssh_conn.get_transport().open_session()
    chan.exec_command(cmd)

    bufsize = -1
    stdout = chan.makefile("r", bufsize)
    stderr = chan.makefile_stderr("r", bufsize)
    rc = chan.recv_exit_status()

    chan.close()

    if not capture:
        for line in stdout:
            log.info("   1: %s", line.rstrip())

    if rc != 0:
        if not capture:
            for line in stderr:
                log.info("   2: %s", line.rstrip())

        if fail:
            raise Exception("SSH Command failed")

    return {'ssh_stdout': stdout, 'ssh_stderr': stderr, 'ssh_rc': rc}


def ssh_mkdir(ssh_conn, dirpath, create_all=True):
    if create_all:
        cmd = "mkdir -p %s" % dirpath
    else:
        cmd = "mkdir %s" % dirpath

    return ssh_runcmd(cmd, ssh_conn = ssh_conn)

def ssh_umount(ssh_conn, dirpath, options=""):
    cmd = "umount %s %s" % (options, dirpath)
    return ssh_runcmd(cmd, ssh_conn = ssh_conn, fail=False)

def ssh_ls(ssh_conn, filepath, list_options=""):
    cmd = "ls {0} {1}".format(list_options, filepath)
    return ssh_runcmd(cmd, ssh_conn = ssh_conn, capture=True)
