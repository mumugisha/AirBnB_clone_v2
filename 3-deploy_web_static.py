#!/usr/bin/python3
# Fabric script (based on the file 2-do_deploy_web_static.py)
# That creates and distributes an archive to your web servers,
# using the function deploy

import os.path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['100.26.142.100', '54.197.89.140']

def do_pack():
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    
    return file

def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False
    
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False
    
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed:
        return False
    
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False
    
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file, name)).failed:
        return False
    
    if run("rm /tmp/{}".format(file)).failed:
        return False
    
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed:
        return False
    
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
        return False
    
    if run("rm -rf /data/web_static/current").failed:
        return False
    
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            name)).failed:
        return False
    
    return True

def deploy():
    file = do_pack()
    if file is None:
        return False
    
    return do_deploy(file)
