import threading, os, time
from com.dtmilano.android.viewclient import ViewClient
from interactions import Click, VirtualScrolling, OpenCloseDrawer
from perfs import Vmstat, Gfxinfo
import helpers as h

device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device, serialno)
info = device.getDisplayInfo()

ocd = OpenCloseDrawer(device, serialno)
vs = VirtualScrolling(device, serialno)
clk1 = Click(device, serialno, int(info['width'] * 0.9), int(info['height'] * 0.1))
clk2 = Click(device, serialno, int(info['width'] * 0.1), int(info['height'] * 0.1))

apps = [
    {
        "type": "native",
        "package": "at.stefanhuber.contactappnative",
        "activity": "MainActivity"
    },
    {
        "type": "reactnative",
        "package": "com.contactappreact",
        "activity": "MainActivity"
    },
    {
        "type": "capacitor",
        "package": "at.stefanhuber.contactappcapacitor",
        "activity": "MainActivity"
    }
]

def swipe():
    vs()


def drawer():
    ocd()


def transition():
    clk1()
    time.sleep(2)
    clk2()


interactions = [
    {
        "name": "swipe",
        "func": swipe
    },
    {
        "name": "transition",
        "func": transition
    },
    {
        "name": "drawer",
        "func": drawer
    }
]


def runAll():

    for j in range(25, 26):
        for i in range(0, len(interactions)):
            for a in range(0, len(apps)):
                vmstat = Vmstat(30, "vmstat_{}_{}_{}_{}.txt".format(serialno, apps[a]["type"], interactions[i]['name'], j))
                gfxinfo = Gfxinfo(apps[a]["package"], "gfxinfo_{}_{}_{}_{}.txt".format(serialno, apps[a]["type"], interactions[i]['name'], j))

                # install and start app
                h.install_apk("{}/./apks/contactapp-{}.apk".format(os.getcwd(), apps[a]["type"]))
                h.start_app(apps[a]["package"], apps[a]["activity"])

                # sleep until app is started
                time.sleep(50)

                # start performance metering
                systrace_thread = threading.Thread(target=vmstat, name="perf-vmstat-thread")
                systrace_thread.start()

                # sleep until metering is started
                time.sleep(3)

                # run interaction
                interactions[i]['func']()

                # sleep and get gfxinfo
                time.sleep(5)
                systrace_thread = threading.Thread(target=gfxinfo, name="perf-gfxinfo-thread")
                systrace_thread.start()
                time.sleep(15)

                # stop and uninstall app
                h.stop_app(apps[a]["package"])
                h.uninstall_apk(apps[a]["package"])

                time.sleep(25)

                # store perf stats
                vmstat.pull_data()
                gfxinfo.pull_data()

runAll()

