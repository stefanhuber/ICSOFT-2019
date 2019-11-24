import subprocess

def install_apk(apk):
    subprocess.call("adb install -r " + apk, shell=False)

def uninstall_apk(pkg):
    subprocess.call("adb uninstall " + pkg, shell=False)

def pull_data(file, target_folder):
    subprocess.call("adb pull " + file + " " + target_folder, shell=False)

def start_app(pkg, activity):
    subprocess.call("adb shell am start -n " + pkg + "/" + pkg + "." + activity, shell=False)

def stop_app(pkg):
    subprocess.call("adb shell am force-stop " + pkg, shell=False)

