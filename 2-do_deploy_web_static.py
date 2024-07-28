#!/usr/bin/env python
# Fabric script (based on the file 2-do_deploy_web_static.py)
# That creates and distributes an archive to your web servers,
# using the function deploy

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.26.142.100', '54.197.89.140']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False
    try:
        final_file_name = archive_path.split("/")[-1]
        non_extens = final_file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, non_extens))
        run('tar -xzf /tmp/{} -C {}{}/'.format(final_file_name, path, non_extens))
        run('rm /tmp/{}'.format(final_file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, non_extens))
        run('rm -rf {}{}/web_static'.format(path, non_extens))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, non_extens))
        return True
    except:
        return False 
