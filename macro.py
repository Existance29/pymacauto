import pyautogui as pag
import time
import os
import subprocess
import mss
import numpy as np
import pyscreeze
import paddleocr
#TODO: Add image recognition + mouse controls
print("Initalising library")
#disable the default pyautogui delay
pag.PAUSE = 0

#get screen size
width, height = pag.size()

#check for retina display
sh, sw, _ = np.array(pag.screenshot()).shape
retina = (height*2 == sh)

#initialise ocr
ocr = PaddleOCR(lang='en', show_log = False, use_angle_cls=False)

print("done intialising")

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
def openApp(app):
    cmd = """ osascript -e 'activate application "{}"' """.format(app)
    os.system(cmd)

def closeApp(app):
    cmd = """ osascript -e 'tell application "{}" to quit' """.format(app)
    os.system(cmd)

def getShellOutput(cmd):
    return subprocess.check_output(cmd, shell=True)

def screenSize():
    output = {
        "mouse": (width,height)
        "screen": (sw, sh)
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

#This seems to be the most reliable way to get accurate pixel colours
#Take a screenshot of one pixel, and convert it to a numpy array
#return in rgba format
def getPixel(x1,y1):
    im = np.array(screenshot(region = (x1,y1,1,1)))
    #convert the unit8 data type to regular integers
    col = tuple([int(x) for x in im[0,0]])
    return col

#Read text from screen
def screenOCR(region = None, textOnly = False):
    imageName = "{}.png".format(time.time()) #use current time for unique image name
    screenshot(region, output = imageName)
    result = ocr.ocr(imageName,cls=False)[0]
    os.remove("{}.png".format(imageName))
    if not result: return None
    
    if textOnly:
        return ''.join([x[1][0] for x in result])
    return result
