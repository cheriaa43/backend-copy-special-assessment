#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits

__author__ = "Cheria Artis with Chris Warren, Chris E, Brandi, Piero"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""

    path_list = [
        os.path.abspath(os.path.join(dirname, f))
        for f in (os.listdir(dirname))
        if re.search(r'__(\w+)__', f)
        ]
    return path_list


def copy_to(path_list, dest_dir):
    print(path_list)
    print(dest_dir)
    try:
        os.makedirs(dest_dir)
    except OSError as e:
        print(e)
        exit(1)
    for path in path_list:
        file_name = os.path.basename(path)
        cur_path = os.path.dirname(path)
        abs_path = os.path.join(cur_path, dest_dir, file_name)
        shutil.copyfile(path, abs_path)
    return


def zip_to(path_list, dest_zip):
    """Zips the files in the path list to the destination zip file."""
    file_list = ''
    for path in path_list:
        file_list += path + ' '
    print("Command I'm going to do:")
    print('zip -j', dest_zip, file_list)
    try:
        subprocess.call(['zip', '-j', dest_zip] + path_list)
    except OSError as e:
        print(e)
        exit(1)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory to search for files')
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    special_paths = get_special_paths(ns.from_dir)
    if ns.todir:
        copy_to(special_paths, ns.todir)
    if ns.tozip:
        zip_to(special_paths, ns.tozip)
    if not ns.todir and not ns.tozip:
        print('\n'.join(special_paths))


if __name__ == "__main__":
    main(sys.argv[1:])
