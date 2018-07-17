
import logging

log = logging.getLogger(__name__)

def _runcmd(cmd, fail=True, capture=False):
    from subprocess import PIPE, Popen
    from alchemy import engine

    p = Popen(cmd, shell=True, stdout = PIPE, stderr=PIPE)
    p.wait()

    if not capture:
        for line in p.stdout:
            log.info("   1: %s", line.rstrip())

    if p.returncode != 0:
        if not capture:
            for line in p.stderr:
                log.info("   2: %s", line.rstrip())

        if fail:
            raise Exception("Command %s failed with rc = %s" % (cmd, p.returncode))
            
    return {
        'shell_stdout': p.stdout,
        'shell_stderr': p.stderr,
        'shell_rc': p.returncode
    }

def runcmd(ctx, cmd, fail=True, capture=False):
    cmd = cmd.format(**ctx.values)

    return _runcmd(cmd, fail=fail, capture=capture)


def local_mkdir(dirpath, create_all=True, fail=True):
    if create_all:
        cmd = "mkdir -p " + dirpath
    else:
        cmd = "mkdir " + dirpath

    return _runcmd(cmd, fail = fail)

def umount(mount_path, options="", fail=True):
    cmd = "umount {0} {1}".format(mount_path, options)
    return _runcmd(cmd, fail=fail)


def local_nfs_mount(nfs_host, nfs_share, mount_path, options="", create_mount_path=True):
    if len(options) > 0:
        options = "-o " + options

    if create_mount_path:
        local_mkdir(mount_path)

    cmd = "mount -t nfs {0}:{1} {2} {3}".format(nfs_host, nfs_share, mount_path, options)
    return _runcmd(cmd)
