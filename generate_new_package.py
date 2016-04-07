# coding: utf-8
'''This is a blank python package.
   This script will clone this package with new names everywhere (and skipping this script)'''

import os
import sys

PT = 'package_template'

def split_list_on_condition(l, cond):
    '''Split list "l" based on condition "cond" which can be:
          * a function returning booleans
          * an iterable of booleans
          * a single boolean'''
    if hasattr(cond, '__call__'):
        pass
    elif hasattr(cond, '__iter__'):
        g = (i for i in cond)
        cond = lambda x: g.next()
    else:
        cond = lambda x: cond
    
    true_list, false_list = [], []
    for i in l:
        (true_list if cond(i) else false_list).append(i)
    return true_list, false_list

def walk(directory, new_directory, new_name):
    if not os.path.exists(new_directory):
        os.mkdir(new_directory)
    contents = os.listdir(directory)
    for f in contents:
        print f
        old_f = os.path.join(directory, f)
        new_f = os.path.join(new_directory, f.replace(PT, new_name))
        if os.path.isdir(old_f):
            if f not in ['.git']: # always skip the .git folder :)
                walk(old_f, new_f, new_name)
        elif (not f not in ['generate_new_package.py'] and     # always skip this script ;)
              os.path.splitext(f)[1] not in ['.pyc', '.pyo']): # and these extensions
                with open(old_f) as fid:
                    r = fid.read()
                with open(new_f, 'w') as fid:
                    fid.write(r.replace(PT, new_name))
                print ''
    print ''

if __name__ == '__main__':
    thisdirectory = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) > 2:
        new_directory = sys.argv[2] # assume this was called with python generate_package_template.py new_name [optional_name]
        new_name = sys.argv[3] if len(sys.argv) > 3 else new_directory
    else:
        print 'Enter your new package name:',
        new_name = new_directory = raw_input()
        #new_name = new_directory = 'wacky_utils'

    # if we are in this directory and a relative path is passed, place it in the parent directory of this file
    if (not os.path.isabs(new_directory) and
        os.path.abspath(os.getcwd()) == os.path.abspath(thisdirectory)):
        new_directory = os.path.join(os.path.dirname(thisdirectory), new_directory)
    walk(thisdirectory, new_directory, new_name)
