
def init_ssh_connection(host, username = None, password = None, port = 22):
    ssh_conn = SSHClient()
    ssh_conn.load_system_host_keys()
    ssh_conn.connect(hostname, username = username, password = password)

    return {'ssh_conn': ssh_conn}

def ssh_runcmd(hostname, cmd, ssh_conn = None, username = None, password = None, port = 22):
    from paramiko.client import SSHClient

    if ssh_conn is None:
        ssh_conn = SSHClient()
        ssh_conn.load_system_host_keys()
        ssh_conn.connect(hostname, username = username, password = password)

    chan = ssh_conn.get_transport().open_session()
    chan.exec_command(cmd)

    bufsize = -1
    stdout = chan.makefile("r", bufsize)
    stderr = chan.makefile_stderr("r", bufsize)
    rc = chan.recv_exit_status()

    chan.close()

    return {'ssh_stdout': stdout, 'ssh_stderr': stderr, 'ssh_rc': rc}

