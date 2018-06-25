

def build_nfs_mount_cmd(host, share_path, local_path, read_only = False):
    if read_only:
        access = ",ro"
    else:
        access = ",rw"

    cmd = "mount -t nfs {0}:{1} {2} -o async{3}".format(host, share_path, local_path, access)

    return {'nfs_mount_cmd': cmd}


def nfs_mount_remote(ssh_session, host, share_path, local_path, read_only = False):
    from alchemy_std.ssh_units

    cmd = build_nfs_mount_cmd(host, share_path, local_path, read_only)

    return ssh_units.ssh_runcmd(None, cmd, ssh_conn = ssh_session)

