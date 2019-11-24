import subprocess
import helpers as h

class Vmstat:

    def set_recording_time(self, recording_time):
        assert type(recording_time) == int
        self.__recording_time = recording_time

    def set_filename(self, filename):
        assert type(filename) == str
        self.__filename = filename

    def __init__(self, recording_time=40, filename="vmstat.txt"):
        self.__recording_time = recording_time
        self.__filename = filename

    def __call__(self):
        subprocess.call("adb shell vmstat 1 " + str(self.__recording_time) + " > /data/local/tmp/" + self.__filename, shell=False)

    def pull_data(self, target_folder='./data/'):
        h.pull_data("/data/local/tmp/" + self.__filename, target_folder)
