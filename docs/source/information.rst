Information
=====

  
Pixel Count on retina displays
^^^^^^^^^
Retina displays' pixel size is doubled the screen's resolution. 
|For example, a resolution of 1440x900 would have 2880x1800 pixels
|This is because there are 2 pixels/unit.\n
|This doesnt affect the library, since screenshots are taken at the resolution's size

Mouse and Screen Position
^^^^^^^^^
The X and Y coordinates start at the top left of the screen at (0,0). 
|X coordinate increases going to the right, while Y increases going down
.. code:: python

  0,0       X increases -->
  +---------------------------+
  |                           | Y increases
  |                           |     |
  |   1440 x 900 screen       |     |
  |                           |     V
  |                           |
  |                           |
  +---------------------------+ 1439, 899

|The bottom-right coordinates will be the resolution - 1. This is because the coordinates start at (0,0)
