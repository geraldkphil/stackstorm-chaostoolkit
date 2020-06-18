import subprocess
import sys
from subprocess import PIPE, run
import json
from st2common.runners.base_action import Action


class InstallExtension(Action):

    def run(self, extension):
        command = ["pip", "list", "installed", "--format",
                   "json", "--disable-pip-version-check"]
        result = run(command, stdout=PIPE,
                     stderr=PIPE, universal_newlines=True)
        pip_libraries = json.loads(result.stdout)
        extension_installed = False
        for pip_library in pip_libraries:
            if pip_library['name'] == extension:
                extension_installed = True

        if extension_installed:
            output = {"status": "extension already installed"}
            return json.dumps(output)
        else:
            subprocess.check_call([sys.executable, "-m",
                                   "pip", "install", extension])
