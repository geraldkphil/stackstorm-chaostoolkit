import json
from st2common.runners.base_action import Action
from subprocess import PIPE, run

class ListInstalledExtensions(Action):

    def run(self):
        command = ["pip", "list", "installed", "--format", "json", "--disable-pip-version-check"]
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        pip_libraries = json.loads(result.stdout)
        chaos_extensions = []
        for pip_library in pip_libraries:
            if "chaostoolkit" in pip_library['name'] and not pip_library['name'] == "chaostoolkit-lib":
                 chaos_extensions.append(pip_library)
        return chaos_extensions