Screen
=====


``Region`` Parameter
----------------
Region accepts a tuple/list containing 4 integers for the left, top, width and height of the area of the screen to capture. 

For example, region = (10,10,300,300) will capture a 300x300 area starting from (10,10) of the screen. If left blank, it will default to the entire screen

Screenshot
----------------

screenshot(region = None, output = None, byte = False)
"""""""""

Description:  

Takes a screenshot of the screen (first monitor) and returns the image 

Parameters:  

* region: area to screenshot (see region parameter above)
* output: image path to save the screenshot to (only png format accepted). If set to None, screenshot is not saved
* byte: convert the screenshot to bytes and return it instead of an mss image


Example:

.. code:: python

  from pymacauto import *
  screenshot(output = "screen.png") #take a screenshot and save it as "screen.png"

  byte_image = screenshot(region = (0,0,400,400), byte = True) #Take a screenshot of a 400x400 square and return the image as bytes 

OCR (Text Recognition)
----------------

Initalising an OCR Class
"""""""""

Example:

.. code:: python

  from pymacauto import *
  ocr = OCR(["en"]) #create an ocr class for english

Parameters:  

* langs: a list containing the languages for the model to detect. Language codes can be found `here <https://www.jaided.ai/easyocr/>`_

readScreen(region = None, textOnly = False)
"""""""""

Description:  

Reads all the text on screen and return a list containing the bounding box, the text, and confidence value for all texts detected

Parameters:  

* region: area to read (see region parameter above)
* textOnly: image path to save the screenshot to (only png format accepted). If set to None, screenshot is not saved
  
Example:

.. code:: python

  from pymacauto import *
  ocr = OCR(["en"]) #create an ocr class for english
  result = ocr.readScreen() #read all the text on the screen
  print(result)

locateTextOnScreen(text, region = None, limit = 1)
"""""""""

Description:  

Reads all the text on screen and return a list containing the bounding box, text, and confidence value of all texts detected. Will return None if the text cannot be found

Parameters:  

* Text: string to search for
* region: area to read (see region parameter above)
* limit: maximum number of successful searches (setting it to 0 will make it detect all)
  
Example:

.. code:: python

  from pymacauto import *
  
  ocr = OCR(["en"]) #create an ocr class for english
  result = ocr.locateTextOnScreen("file", limit = 0) #find all texts containing "file" on the screen
  print(result)
