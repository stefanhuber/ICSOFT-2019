from com.dtmilano.android.viewclient import ViewClient

class OpenCloseDrawer:

    def __init__(self, device, serialno):
        self.__device = device
        self.__serialno = serialno

    def __call__(self):
        vc = ViewClient(self.__device, self.__serialno)

        info = self.__device.getDisplayInfo()
        end_x = int(info['width'] / 4)
        start_y = int(info['height'] / 2)

        if self.__serialno == "04a38409344082e7":
            vc.swipe(0, start_y, end_x, start_y, 100)
        elif self.__serialno == "010e3939219f5389":
            vc.swipe(0, start_y, end_x, start_y, 150)

        vc.swipe(0, start_y, end_x, start_y, 100)

        vc.sleep(2)

        vc.touch(int(end_x * 4 * .9), start_y)
