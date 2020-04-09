#!/usr/bin/python3
# Fabric script (based on the file 2-do_deploy_web_static.py)
# that creates and distributes an archive to your web
# servers, using the function deploy

from fabric.api import env, put, run, local
from fabric import decorators
from datetime import datetime
import os

env.hosts = ['18.234.214.65', '107.20.99.54']
env.key_filename = "~/.ssh/holberton"
env.user = "ubuntu"


@decorators.runs_once
def do_pack():
    """ Creates folder versions with tgz static_files"""
    now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path_file = "versions/web_static_{}.tgz".format(now)
    compress_command = "tar -cvzf {} web_static/".format(path_file)
    local("mkdir -p versions")
    res = local(compress_command)
    if res.failed:
        return None
    return path_file


def do_deploy(archive_path):
    if os.path.isfile(archive_path) is False:
        return False
    # Upload archive_path to /tmp folder
    put(archive_path, "/tmp")
    file_split = archive_path.split('/')
    file_with_ext = file_split[1]
    file_without_ext = file_split[1].split('.')[0]
    if run("mkdir -p /data/web_static/releases/{}/".format(
            file_without_ext)).failed is True:
        return False
    print("Release folder created")
    if run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
            file_without_ext, file_without_ext)).failed is True:
        return False
    print("Uncompress the archive inside the folder releases done")
    if run("rm /tmp/{}".format(file_with_ext)).failed is True:
        return False
    print("Delete the archive from the web server done")
    if run("mv /data/web_static/releases/{}/web_static/*"
           " /data/web_static/releases/{}/".format(
            file_without_ext, file_without_ext)).failed is True:
        return False
    print("Move all the files and folders to one directory before")
    if run("rm -rf /data/web_static/releases/{}/web_static".format(
            file_without_ext)).failed is True:
        return False
    print("Deleted empty folder web_static")
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    print("Delete the symbolic link done")
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_without_ext)).failed is True:
        return False
    print("Created new symbolic link /data/web_static/current")
    print("New version deployed!")
    return True


def deploy():
    """Full deploy of web static files"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
