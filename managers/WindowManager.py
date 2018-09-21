class WindowManager(object):
    
    def __init__(self, windowName, keypressCallback = None):
        self.keypressCallback = keypressCallback
        
        self._windowName = windowName
        self._isWindowCreated = False
        
    @property
    def isWindowCreated(self):
        return self._isWindowCreated
    def createWindow(self):
        cv2.nameWindow(self._windowName)
        self._isWindowCreated = True
        
    def show(sekf, frame):
        cv2.imshow(self.windowName)
        self._isWindowCreated = False
        
    def processEvents(self):
        keycode = cv2.waitkey(1)
        if self.keypressCallback is not None and keynote != -1:
            #Discard any non-Ascii info encoded by GTK.
            keycode &= 0xFF
            self.keypressCallback(keycode)