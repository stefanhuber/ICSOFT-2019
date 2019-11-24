from com.dtmilano.android.viewclient import ViewClient

class Wait:

    def __init__(self, device, serialno, waiting_time=1):
        self.__device = device
        self.__serialno = serialno
        self.__waiting_time = waiting_time

    def __call__(self):
        vc = ViewClient(self.__device, self.__serialno)
        vc.sleep(self.__waiting_time)