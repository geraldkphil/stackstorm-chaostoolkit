#!/usr/bin/env python

from st2common.runners.base_action import Action
import os
import sys
import subprocess
import json

class ChaostoolkitAction(Action):

def run(sub_command):
    full_cmd = ['chaos'] + ['--no-version-check'] + sub_command.split(' ')
    process = subprocess.Popen(full_cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
#    return_code = process.poll()
    if stderr:
        output = stderr
    return (output.decode('utf-8')
