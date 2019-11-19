#!/usr/bin/env python
#-*- coding:utf8 -*-

import os
import sys



def run(cmd, base = './'):
    if not cmd:
        return
    pwd = os.path.abspath(base)
    dirs = os.listdir(base)
    abs_path_list = []
    for d in dirs:
        if d.startswith('.'):
            continue
        abs_path = os.path.join(pwd, d)
        if not os.path.isdir(abs_path):
            continue
        abs_path_list.append(abs_path)

    for path in abs_path_list:
        new_cmd = 'cd {0} && {1} '.format(path, cmd)
        std_print = '\n$ {0}'.format(new_cmd)
        #print("\033[0;31;40m\t{0}\033[0m".format(std_print))
        print("\033[4;32;47m{0}\033[0m".format(std_print))
        #os.system(new_cmd)
        result = os.popen(new_cmd).readlines()
        for r in result:
            if r.endswith('\n'):
                r = r[:-1]
            print(r)


if __name__ == '__main__':
    cmd = 'pwd'
    base = './'
    if len(sys.argv) == 2:
        cmd = sys.argv[1]
    if len(sys.argv) == 3:
        base = sys.argv[1]
        cmd  = sys.argv[2]
    print('base: {0} cmd: {1}'.format(base, cmd))

    run(cmd, base)
