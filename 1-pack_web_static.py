#!/usr/bin/python3
# Fabric script that generates a .tgz archive from
# the contents of the web_static folder

from fabric.api import local
from datetime import datetime


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
