#!/usr/bin/python3
"""
fabric script (based on the file 3-deploy_web_static.py) that
deletes old archive with do_clean
"""
from fabric.operations import *


env.hosts = ['18.233.67.128', '100.25.162.166']


def do_clean(number=0):
    """remove out-of-date archives"""

    ls_files = local("ls -1t versions", capture=True).split("\n")

    num = int(number)
    if num == 0 or num == 1:
        num = 1
    for File in ls_files[num:]:
        local("rm versions/{}".format(File))
    ls_dir_remote = run("ls -1t /data/web_static/releases").split("\n")
    for Dir in ls_dir_remote[num:]:
        if Dir == 'test':
            continue
        run("rm -rf /data/web_static/releases/{}"
            .format(Dir))
