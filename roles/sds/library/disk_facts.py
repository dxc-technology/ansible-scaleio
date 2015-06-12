#!/usr/bin/python

from subprocess import Popen, PIPE
import sys


def execute_process(cmd_line):
    try:
        process = Popen(cmd_line, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        output, err = process.communicate()
        return_code = process.returncode
        return output, err, return_code
    except Exception as e:
        sys.exit(1)


def main():

    module = AnsibleModule(argument_spec=dict(),supports_check_mode=False)

    disks = []
    output, err, return_code = execute_process( "lsblk -rno NAME,TYPE" )
    output_lines = output.split('\n')

    for line in output_lines:
        line_array = line.split(" ")
        if 'disk' in line:
            disks.append( "/dev/%s" % line_array[0] )
        if 'part' in line:
            result = ''.join([i for i in line_array[0] if not i.isdigit()])
            try:
                disks.remove( "/dev/%s" % result )
            except:
                continue

    module.exit_json(changed=False, ansible_available_disks=disks)


from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

