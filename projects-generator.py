#!/usr/bin/env python
# -*- coding:utf8 -*-
#
#    Copyright 2017 Vitalii Kulanov
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
projects-generator.py script is used to create 'projects.yaml' file
(for Jeepyb tools, openstack-infra/jeepyb) with respective projects names
based on input tags, e.g.:

    owner_list.txt content:
        person1
        person2

    projects_list.txt content:
        project1
        project2

    $ projects-generator.py 2017 owner_list.txt vhdl projects_list.txt

    'projects.yaml' content:
        - project: 2017/person1/vhdl/project1
        - project: 2017/person1/vhdl/project2
        - project: 2017/person2/vhdl/project1
        - project: 2017/person2/vhdl/project2
"""

import argparse
import itertools
import os
import sys
import yaml


def retrieve_tags(arg, comment_symbol='#'):
    """Retrieve tag(s) from argument. If argument is file then read all tags
    from it, otherwise convert argument to tag. Tags in files must be putted
    on a separate lines

    :param arg: single tag name or file name that contains tags
    :type arg: str
    :param comment_symbol: skip lines that start with specified symbol
    :type comment_symbol: str
    :return: data as a list of tag(s)
    :rtype: list
    """
    try:
        with open(arg, 'r') as fd:
            # remove empty lines from file
            tags = list(filter(None, (line.rstrip() for line in fd
                                      if not line.startswith(comment_symbol))))
    except (OSError, IOError):
        tags = [arg]
    return tags


def create_yaml(data, dir_path, file_name='projects.yaml'):
    file_path = os.path.join(dir_path, file_name)
    try:
        with open(file_path, 'w') as stream:
            yaml.safe_dump(data, stream, default_flow_style=False)
    except (OSError, IOError) as e:
        msg = "Can't generate '{}' file in '{}': {}\n".format(file_name,
                                                              dir_path,
                                                              e)
        sys.stdout.write(msg)


def main():
    parser = argparse.ArgumentParser(description='Gerrit projects generator '
                                                 'for Jeepyb tools')

    parser.add_argument('projects_tags',
                        metavar='PROJECT_TAG',
                        nargs='+',
                        help="project tag(s) or file(s) with tags")
    parser.add_argument('-d',
                        '--directory',
                        default=os.path.curdir,
                        help="destination directory for the output "
                             "file. Defaults to the current directory")
    parser.add_argument('-n',
                        '--name',
                        metavar='FILE_NAME',
                        default='projects.yaml',
                        help="name of file to store Gerrit projects. "
                             "Defaults to 'projects.yaml'")
    parser.add_argument('--acl-config',
                        metavar='ACL_CONFIG_PATH',
                        required=True,
                        help="path to acl config file")
    args = parser.parse_args()

    retrieved_tags = []
    for project_tag in args.projects_tags:
        retrieved_tags.append(retrieve_tags(project_tag))

    # join tags with '/' delimiter in Gerrit-like format
    projects_names = ['/'.join(x) for x in itertools.product(*retrieved_tags)]

    # projects listed in 'projects.yaml' file must be sorted alphabetically
    projects_names.sort()
    projects = []
    for project_name in projects_names:
        project_item = {'project': project_name,
                        'acl-config': args.acl_config}
        projects.append(project_item)
    create_yaml(projects, args.directory, args.name)
    sys.stdout.write("File '{}' successfully generated in '{}'"
                     "\n".format(args.name, os.path.abspath(args.directory)))


if __name__ == '__main__':
    main()
