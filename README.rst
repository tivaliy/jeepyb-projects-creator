=======================
jeepyb-projects-creator
=======================

Tool for generating ``projects.yaml`` file for `Jeepyb <https://github.com/openstack-infra/jeepyb>`_

Usage
-----

**projects-generator.py [-h] [-d DIRECTORY] [-n FILE_NAME] PROJECT_TAG [PROJECT_TAG ...]**

Gerrit projects generator for Jeepyb tools.

positional arguments:
  +----------------------------------------------------+
  | PROJECT_TAG    project tag(s) or file(s) with tags |
  +----------------------------------------------------+

optional arguments:
  -h, --help       show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                   destination directory for the output file.
                   Defaults to the current directory
  -n FILE_NAME, --name FILE_NAME
                   name of file to store Gerrit projects. Defaults to ``projects.yaml``
