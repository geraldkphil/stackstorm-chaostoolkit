#!/usr/bin/env python

from st2common.runners.base_action import Action
import os
import sys
import subprocess
import json

class ChaostoolkitAction(Action):

    def run(self, **kwargs):
        sub_command = kwargs['sub_command']
#        full_cmd = ['chaos'] + sub_command.split(' ')
        full_cmd = ['chaos'] + ['--version']
        process = subprocess.Popen(full_cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(full_cmd)
#    return_code = process.poll()
        if stderr:
            output = stderr
        return (output.decode('utf-8'))
