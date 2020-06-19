from chaoslib.discovery import discover as disco
from st2common.runners.base_action import Action


class Discover(Action):

    def run(self, extension):
        discovery = disco(
            package_name=extension, discover_system=True,
            download_and_install=True)
        return discovery