=======================
jeepyb-projects-creator
=======================

Tool for generating ``projects.yaml`` file for `Jeepyb <https://github.com/openstack-infra/jeepyb>`_

Usage
-----

**projects-generator.py [-h] [-d DIRECTORY] [-n FILE_NAME] --acl-config ACL_CONFIG_PATH PROJECT_TAG [PROJECT_TAG ...]**

Gerrit projects generator for Jeepyb tools.

positional arguments:
  :kbd:`PROJECT_TAG`    project tag(s) or file(s) with tags

optional arguments:
  -h, --help       show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                   destination directory for the output file.
                   Defaults to the current directory
  -n FILE_NAME, --name FILE_NAME
                   name of file to store Gerrit projects. Defaults to ``projects.yaml``
  --acl-config ACL_CONFIG_PATH
                   path to acl config file

Example
```````
``owner_list.txt`` file content:
::

   person1
   person2

``projects_list.txt`` file content:
::

   project1
   project2

``$ projects-generator.py 2017 owner_list.txt vhdl projects_list.txt --acl-config acls/vhdl/vhdl.config``

Command execution result (``projects.yaml``):

.. code:: yaml

    - project: 2017/person1/vhdl/project1
      acl-config: acls/vhdl/vhdl.config
    - project: 2017/person1/vhdl/project2
      acl-config: acls/vhdl/vhdl.config
    - project: 2017/person2/vhdl/project1
      acl-config: acls/vhdl/vhdl.config
    - project: 2017/person2/vhdl/project2
      acl-config: acls/vhdl/vhdl.config