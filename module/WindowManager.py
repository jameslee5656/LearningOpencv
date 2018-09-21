import cv2
import numpy as np
import time

class WindowManager(object):
    
    def __init__(self, windowName, keypressCallback = None):
        self.keypressCallback = keypressCallback
        
        self._windowName = windowName
        self._isWindowCreated = False
        
    @property
    def isWindowCreated(self):
        return self._isWindowCreated
    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True
        
    def show(sekf, frame):
        cv2.imshow(self.windowName, frame)
    
    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False
        
    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            #Discard any non-Ascii info encoded by GTK.
            keycode &= 0xFF
            self.keypressCallback(keycode)