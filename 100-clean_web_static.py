#!/usr/bin/python3
"""
fabric script (based on the file 3-deploy_web_static.py) that
deletes old archive with do_clean
"""
from fabric.operations import *


env.user = "ubuntu"
env.hosts = ['18.233.67.128', '100.25.162.166']


def do_clean(number=0):
    """remove out-of-date archives"""

    num = int(number)

    if num == 0 or num == 1:
        num = 1
    else:
        num += 1
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(num))
    cmd = 'cd /data/web_static/releases'
    run('{}; ls -t | tail -n +{} | xargs rm -rf'.format(cmd, num))
