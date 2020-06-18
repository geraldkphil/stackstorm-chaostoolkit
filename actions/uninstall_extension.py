import subprocess
import sys
from subprocess import PIPE, run
import json
from st2common.runners.base_action import Action


class UninstallExtension(Action):

    def run(self, extension):
        command = ["pip", "list", "installed",
                   "--format", "json", "--disable-pip-version-check"]
        result = run(command, stdout=PIPE,
                     stderr=PIPE, universal_newlines=True)
        pip_libraries = json.loads(result.stdout)
        extension_installed = False
        for pip_library in pip_libraries:
            if pip_library['name'] == extension:
                extension_installed = True

        if extension_installed:
            subprocess.check_call([sys.executable, "-m",
                                  "pip", "uninstall", "-y", extension])
        else:
            output = {"status": "extension already uninstalled"}
            return json.dumps(output)
