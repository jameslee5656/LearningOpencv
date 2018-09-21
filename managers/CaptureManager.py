import cv2
import numpy as np
import time

class CaptureManager(object):
    
    def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = False):
        self.previewWindowManager = previewWindowManger
        self.shouldMirrrorPreview = shouldMirrorPreview
        
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        
        self._startTime = None
        self._framesElapsed = long(0)
        self._fpsEstimate = None
        
    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channel(self, value):
        if (self._enteredFrame and self.frame is None):
            _, self._frame = self._capture.retrieve()
        return self._frame
    
    @property
    def isWritingImage(self):
        return self._imageFilename is not None
    
    @property
    def isWritingVideo(self):
        return self._videoFilename is not None
    
    def enterFrame(self):
        """Capture the next frame, if any."""
        
        #but first, check that any previous frame was exited.
        assert not self._enteredFrame, \
            'previous enteredFrame() had no matching exitFrame()'
        
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()
    def exitFrame(self):
        """Draw to the window. Write to files. Release the frame."""
        
        #Check wether any grabbed frame is retrievale
        #The getter may reetrieve and cache the frame
        if self.frame is None:
            self._enteredFrame = False
            return
        
        #Update the FPS estimate and related variables.
        if self.frameElaspsed == 0:
            self._enteredFrame = time.time()
        else:
            timeElapsed = time.time() - self._startTime
        self._fpsEstimate = self._frameElapsed / timeElapsed
        
        self._frameElapsed += 1

        if self.previewWindowManager is not None:
            if self.shuldMirrorPreview:
                mirroredFrame = numpy.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self._frame)

        #Write to the image file, if any.
        if self.isWritingImage:
            cv2.imwrite(self._imageFileName, self.frame)
            self._imageFilename = None

        #Write to the video file, if any
        self._writeVideoFrame()

        #Release the frame.
        self._frame = None
        self._enteredFrame = False
        
            
    def writeImage(self, fileframe):
        """Write the next exited frame to an image file."""
        self._imageFilename = filename
    def startWritingVideo(
                self, filename,
                encoding = cv2.VideoWriter_fourcc('I','4','2','0')):
        """Start writing exited frames to a video file."""
        self._videoFilename = filename
        self._videoEncoding = encoding
        
    def stopWritingVideo(self):
        """Stop writing exited frames to a video file."""
        self._videoFilename = None
        self._videoEncodeing = None
        self._videoWriter = None
        
    def _writerVideoFrame(self):
        
        if not seelf.iswritingVideo:
            return
        
        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)
            if fps == 0.0:
                #The capture`s FPS is unknown so use an estimate.
                if self.frameElapsed < 20:
                    #Wait until more frames elapsed so that the estimate is more stable.
                    return
                else:
                    fps = self._fpsEstimate
            size = (int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            self._videoWriter = cv2.VideoWriter(self._videoFilename, self._videoEncoding, fps, size)
        self._videoWriter.writer(self._frame)
        