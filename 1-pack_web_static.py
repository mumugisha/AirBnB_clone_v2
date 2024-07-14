#!/usr/bin/env python3
# Fabric script that generates a .tgz archive from
# The contents of the web_static folder of your
# AirBnB Clone repo, using the function

from fabric.api import local
from time import strftime
from datetime import date

def do_pack():
    file_final_name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(file_final_name))
        return "versions/web_static_{}.tgz".format(file_final_name)
    except Exception as e:
        return None
