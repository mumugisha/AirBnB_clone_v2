#!/usr/bin/env python
# Fabric script (based on the file 3-deploy_web_static.py)
# That deletes out-of-date archives, using the function do_clean

from fabric.api import run, env, local, cd, lcd, settings

env.user = 'ubuntu'
env.hosts = ['54.197.89.140', '100.26.142.100']
env.key_filename = '~/.ssh/school'

def do_clean(number=0):
    number = int(number)
    try:
        with lcd('versions/'):
            versions = local('ls -t', capture=True).split()
            versions_to_delete = versions[1:] if number <= 1 else versions[number:]
            for v in versions_to_delete:
                local(f'rm -rf {v}')

        with cd('/data/web_static/releases'):
            if number <= 1:
                number_to_keep = 2
            else:
                number_to_keep = number + 1
            with settings(warn_only=True):  # Suppress errors to continue execution
                run(f'ls -t | tail +{number_to_keep} | xargs rm -rf')

    except Exception as e:
        print(f"An error occurred: {e}")
