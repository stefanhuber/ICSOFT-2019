import subprocess
import helpers as h

class Gfxinfo:

    def __init__(self, package, filename):
        self.__package = package
        self.__filename = filename

    def __call__(self):
        subprocess.call("adb shell dumpsys gfxinfo {} > /data/local/tmp/{}".format(self.__package, self.__filename), shell=False)

    def pull_data(self, target_folder='./data/'):
        h.pull_data("/data/local/tmp/" + self.__filename, target_folder)
