Screen
=====


``Region`` Parameter
----------------
Region accepts a tuple/list containing 4 integers for the left, top, width and height of the area of the screen to capture. 

For example, region = (10,10,300,300) will capture a 300x300 area starting from (10,10) of the screen

Functions
----------------

Screenshot
^^^^^^^^^

screenshot(region, output = None, byte = False)
"""""""""

Description:  

Takes a screenshot of the screen (first monitor) and returns the image 

Parameters:  

* region: area to screenshot (see information)
* output: image path to save the screenshot to (only png format accepted). If set to None, screenshot is not saved
* byte: convert the screenshot to bytes and return it instead of an mss image


Example:

.. code:: python

  from pymacauto import *
  screenshot(output = "screen.png") #take a screenshot and save it as "screen.png"

  byte_image = screenshot(region = (0,0,400,400), byte = True) #Take a screenshot of a 400x400 square and return the image as bytes 

  
