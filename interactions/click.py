from com.dtmilano.android.viewclient import ViewClient

class Click:

    def __init__(self, device, serialno, x, y):
        self.__device = device
        self.__serialno = serialno
        self.__x = x
        self.__y = y

    def __call__(self):
        vc = ViewClient(self.__device, self.__serialno)

        vc.click(self.__x, self.__y)
