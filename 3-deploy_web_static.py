#!/usr/bin/python3
""" module to defin fabric file"""
from fabric.operations import local, run, put, env
from datetime import datetime
import os

env.hosts = ['18.233.67.128', '100.25.162.166']


def do_pack():
    """ Fabric script that generates a .tgz archive from the contents of the
    ...web_static folder """
    try:
        local("sudo mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(date)
        result = local("sudo tar -cvzf {} web_static".format(filename))
        if result.succeeded:
            return filename
    except Exception as error:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return(False)
    try:
        put(archive_path, '/tmp/')
        tar_filename = archive_path.split("/")[-1]
        filename = tar_filename.split(".")[0]
        run('mkdir -p /data/web_static/releases/{}'.format(filename))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format
            (tar_filename, filename))
        run('rm /tmp/{}'.format(tar_filename))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(filename, filename))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename))
        return(True)
    except Exception as error:
        return(False)


def deploy():
    """ deploy all in one command"""
    path_to_tar = do_pack()

    if os.path.exists(path_to_tar) is False:
        return (False)
    return do_deploy(path_to_tar)
