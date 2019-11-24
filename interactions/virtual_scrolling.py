from com.dtmilano.android.viewclient import ViewClient

class VirtualScrolling:

    def __init__(self, device, serialno):
        self.__device = device
        self.__serialno = serialno

    def __call__(self):
        vc = ViewClient(self.__device, self.__serialno)

        steps = 90
        start_factor = .75
        end_factor = .55

        if self.__serialno == "04a38409344082e7":
            steps = 90
            start_factor = .75
            end_factor = .55
        elif self.__serialno == "010e3939219f5389":
            steps = 155
            start_factor = .70
            end_factor = .45
        elif self.__serialno == "22db15d035057ece":
            steps = 200
            start_factor = .65
            end_factor = .35
        elif self.__serialno == "8aee2aaa":
            steps = 100
            start_factor = .75
            end_factor = .55


        info = self.__device.getDisplayInfo()
        x = int(info['width'] * .5)
        start_y = int(info['height'] * start_factor)
        end_y = int(info['height'] * end_factor)

        vc.swipe(x, start_y, x, end_y, steps)
        vc.sleep(2)
        vc.swipe(x, start_y, x, end_y, steps)
        vc.sleep(2)
        vc.swipe(x, start_y, x, end_y, steps)
