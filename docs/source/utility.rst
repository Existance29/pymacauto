Utility
=====

Utility Functions
----------------

isRetina()
"""""""""

Description:  

Returns true if the mac has a retina display

Example:

.. code:: python

  from pymacauto import *

  print(isRetina())


runAppleScript(code)
"""""""""

Description:  

Execute an applescript code

Parameters:  

* code: applescript code to run

Example:

.. code:: python

  from pymacauto import *

  runAppleScript('display dialog "Hello!"') #display a pop-up containing text

openApp(app)
"""""""""

Description:  

Opens an application and send it to front

Parameters:  

* app: name of application to open

Example:

.. code:: python

  from pymacauto import *

  openApp("safari") #open the safari app

quitApp(app)
"""""""""

Description:  

Closes an application

Parameters:  

* app: name of application to close

Example:

.. code:: python

  from pymacauto import *

  closeApp("safari") #close safari

screenSize()
"""""""""

Description:  

Returns a dictionary containing the pixel size and the resolution of the screen. Explaination for resolution and pixel sizes can be found in the information section

Example:

.. code:: python

  from pymacauto import *

  print(screenSize())

getShellOutput(cmd)
"""""""""

Description:  

Returns the output of a shell command

Parameters:  

* cmd: command to run

Example:

.. code:: python

  from pymacauto import *

  print(getShellOutput("system_profiler SPDisplaysDataTyp")) #print out display information of the mac
