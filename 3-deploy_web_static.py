#!/usr/bin/env python
# Fabric script (based on the file 2-do_deploy_web_static.py)
# That creates and distributes an archive to your web servers,
# using the function deploy

def deploy():
    """Full deployment webserver"""
    # Importing the functions dynamically inside the function to comply with best practices.
    do_pack = __import__('1-pack_web_static').do_pack
    do_deploy = __import__('2-do_deploy_web_static').do_deploy
    
    arch_path = do_pack()
    if not arch_path:
        return False
    return do_deploy(arch_path)

if __name__ == "__main__":
    deploy()
