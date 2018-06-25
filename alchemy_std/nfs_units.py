

def build_nfs_mount_cmd(host, share_path, local_path, read_only = False):
    if read_only:
        access = ",ro"
    else:
        access = ",rw"

    cmd = "mount -t nfs {0}:{1} {2} -o async{3}".format(host, share_path, local_path, access)

    return {'nfs_mount_cmd': cmd}


def nfs_mount_remote(ssh_session, nfs_host, share_path, local_path, read_only = False):
    """
    input:
        nfs_host: Host name of the nfs server
        ssh_session: Connected SSH Session
        share_path: NFS server share path (as seen in showmount -e command)
        local_path: Dir at which the nfs needs to be mounter
        read_only: (False) Mount to be read_only or not
    output:
        ssh_stdout: STDOUT stream
        ssh_stderr: STDERR stream
        ssh_rc: Return code of the command run
    """

    from alchemy_std import ssh_units

    cmd = build_nfs_mount_cmd(nfs_host, share_path, local_path, read_only)['nfs_mount_cmd']

    print "NFS mount:", cmd
    res = ssh_units.ssh_runcmd(cmd, ssh_conn = ssh_session)
    return res

