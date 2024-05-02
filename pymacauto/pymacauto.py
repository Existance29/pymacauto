
import pyautogui as pag
import time
import os
import subprocess
import mss
import numpy as np
import pyscreeze
import paddleocr
#TODO: Add image recognition + mouse controls

#disable the default pyautogui delay
pag.PAUSE = 0

#get screen size
width, height = pag.size()

#check for retina display
sh, sw, _ = np.array(pag.screenshot()).shape
retina = (height*2 == sh)

#A more accurate sleep funcrion
def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()
        
#wrapper for pyautogui's keydown and keyup
def keyDown(key):
    pag.keyDown(key)

def keyUp(key):
    pag.keyDown(key)

#hold key down for x seconds
def press(key, delay = 0.02):
    keyDown(key)
    sleep(delay)
    keyUp(key)


def isRetina():
    return retina

def runAppleScript(code):
    cmd = " osascript -e '{}' ".format(code)
    os.system(cmd)
    
def openApp(app):
    runAppleScript('activate application "{}"'.format(app))
                   
def quitApp(app):
    runAppleScript('tell application "{}" to quit'.format(app))

def getShellOutput(cmd):
    return subprocess.check_output(cmd, shell=True)

def getCenter(coords, rounded = False):
    out = ((coords[0]+coords[2])/2, (coords[1]+coords[3])/2)
    if not rounded: return out
    return tuple([round(x) for x in out])

def screenSize():
    output = {
        "screen": (width,height)
        "pixel": (sw, sh)
    }
    return output

#wrapper for mss
#use region in the same format as pyscreeze's
def screenshot(region = (0,0,width,height), output = None)

    mssRegion = {'top': region[0], 'left': region[1], 'width': region[2], 'height': region[3]}
    with mss.mss() as sct:
        img = sct.grab(region)
        
    if output is not None:
        mss.tools.to_png(img.rgb, img.size, output=output)
    return img
#Replace pyscreeze's screenshots with mss'
#pyscreeze.screenshot = screenshot

#This seems to be the most reliable way to get accurate pixel colours
#Take a screenshot of one pixel, and convert it to a numpy array
#return in rgba format
def getPixel(x1,y1):
    im = np.array(screenshot(region = (x1,y1,1,1)))
    #convert the unit8 data type to regular integers
    col = tuple([int(x) for x in im[0,0]])
    return col

def locateImageOnScreen(needleImage, region = None, method = "pyscreezepillow", var = 0, confidence = 0.9, grayscale = None, limit = 1):
    method = method.lower()
    if method == "pyscreezepillow":
        locateFunc = _locateAll_pillow
    elif method == "pyscreezecv"
        locateFunc = _locateAll_opencv
    locateFunc(needleImage, screenshot(region), grayscale = grayscale, limit = limit, confidence = confidence)
#OCR related functions
class OCR:
    def __init__(self, **kwargs):
        #initialise ocr
        defaultKwargs = {"lang": "en", "show_log": False, "use_angle_cls": False}
        kwargs = { **defaultKwargs, **kwargs }
        self.ocr = PaddleOCR(kwargs)
        
    #Read text from screen
    def readScreen(region = None, textOnly = False):
        imageName = "{}.png".format(time.time()) #use current time for unique image name
        screenshot(region, output = imageName)
        result = self.ocr.ocr(imageName,cls=False)[0]
        os.remove("{}.png".format(imageName))
        if not result: return None
        
        if textOnly:
            return ''.join([x[1][0] for x in result])
        return result

    def locateTextOnScreen(text, region = None):
        res = readScreen(region = region)
        for i in res:
            if text in i[1][0]:
                return i
        return None
