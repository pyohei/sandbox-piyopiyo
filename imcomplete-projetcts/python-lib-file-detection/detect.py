""" Detect library module files

This module supplies module files which is same name with python's starndard
libraries.

.. Created:
    2016-03-21
"""

import importlib
import os
# import logging

IGNORE_FILE = ['__init__.py']


class Detection(object):

    def __init__(self, target_dirs=None):
        if not target_dirs:
            self.target_dir = os.path.join(os.path.abspath(
                os.path.dirname(__file__)), "demo")
        else:
            self.target_dirs = target_dirs

    def execute(self):
        for (root, _dirs, walk_files) in os.walk(self.target_dir):
            for walk_file in walk_files:
                print "-----"
                print walk_file
                if self.__is_untarget(walk_file):
                    print "Here"
                    continue
                re_file = self.__awk_file(walk_file)
                if self.__can_import(re_file):
                    print "Can import. {}".format(walk_file)

    def __is_untarget(self, file_name):
        if file_name in IGNORE_FILE:
            return False
        if ".py" in file_name:
            return False
        return True

    def __awk_file(self, file_name):
        return file_name.strip('.py')

    def __can_import(self, module):
        try:
            importlib.import_module(module)
            return True
        except ImportError as e:
            return False

if __name__ == '__main__':
    detection = Detection()
    detection.execute()
