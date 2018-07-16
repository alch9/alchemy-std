
import logging

log = logging.getLogger(__name__)

def runcmd(ctx, args, fail=True, capture=True):
    from subprocess import PIPE, Popen
    from alchemy import engine

    args = engine.resolve_list(ctx, args)

    p = Popen(args, stdout = PIPE, stderr=PIPE)
    p.wait()

    if not capture:
        for line in p.stdout:
            log.info("   1: %s", line.rstrip())

    if p.returncode != 0:
        if not capture:
            for line in p.stderr:
                log.info("   2: %s", line.rstrip())

        if fail:
            raise Exception("Command %s failed with rc = %s" % (args, p.returncode))
            
    return {
        'shell_stdout': p.stdout,
        'shell_stderr': p.stderr,
        'shell_rc': p.returncode
    }
