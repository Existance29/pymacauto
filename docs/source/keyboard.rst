Keyboard
=====

Functions
----------------

keyDown(key)
"""""""""

Description:  

Presses the key down

Parameters:  

* key: key to press (see keyboard keys)

Example:

.. code:: python

  from pymacauto import *

  keyDown("a") #press down the a key

keyUp(key)
"""""""""

Description:  

Release the key

Parameters:  

* key: key to press (see keyboard keys)

Example:

.. code:: python

  from pymacauto import *

  keyUp("a") #releases the a key

press(key, delay=0.02)
"""""""""

Description:  

Presses the key down for a set amount of time

Parameters:  

* key: key to press (see keyboard keys)
* delay: how long to press the key for (in seconds)

Example:

.. code:: python

  from pymacauto import *

  press("a", 0.5) #Press the a key for 0.5s
