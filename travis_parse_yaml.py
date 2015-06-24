#!/usr/bin/env python

import os
import fnmatch
import yaml
import linecache
import sys
from subprocess import Popen, PIPE


def execute_process(cmd_line):
    try:
        process = Popen(cmd_line, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        output, err = process.communicate()
        return_code = process.returncode
        return output, err, return_code
    except Exception as e:
        sys.exit(1)


def main():
    argv = sys.argv[1:]
    failure = False

    for arg in argv:
        cmd_line = "ansible-playbook --syntax-check %s" % arg
        print "Running: %s " % cmd_line
        output, err, return_code = execute_process(cmd_line)
        print output, err

        if return_code != 0:
            failure = True

    path = os.getcwd()
    yamlfiles = [os.path.join(dirpath, f)
             for dirpath, dirnames, files in os.walk(path)
             for f in fnmatch.filter(files, '*.yml')]

    for yml in yamlfiles:
        caret = " " * 100
        try:
            stream = open(yml, 'r')
            config = yaml.load(stream)
        except yaml.YAMLError, exc:
	    failure = True 
            print "%s %s %s\n" % ("#"*10, exc.problem, "#"*10)
            print "File: %s" % yml

            if hasattr(exc, 'context_mark'):
                if exc.context_mark is not None:
                    print "BEGIN: line: %d, column: %d" % (exc.context_mark.line,exc.context_mark.column)
            if hasattr(exc, 'problem_mark'):
                print "END: line:%d, column: %d\n" % (exc.problem_mark.line,exc.problem_mark.column)
                print "%s" % linecache.getline(yml, exc.problem_mark.line+1)
                print caret[:exc.problem_mark.column] + "^" + caret[exc.problem_mark.column+1:]
        finally:
            stream.close()
    if failure:
        sys.exit(1)

if __name__ == '__main__':
    main()


