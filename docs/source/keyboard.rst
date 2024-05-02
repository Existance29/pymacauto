Keyboard
=====

Keyboard Functions
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

write(message, interval=0.1, delay = 0.02)
"""""""""

Description:  

types out a string character by character

Parameters:  

* message: the string to write
* interval: the delay between characters (in seconds)
* delay: how long to press each key for (in seconds)

Example:

.. code:: python

  from pymacauto import *

  write("hello!", interval = 0.1, delay = 0.03) #Type hello! 

Keyboard Keys
----------------
The following are the valid string characters to pass to the ``key`` parameter of the functions

.. code-block::

  ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
  ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
  '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
  'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
  'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
  'browserback', 'browserfavorites', 'browserforward', 'browserhome',
  'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
  'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
  'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
  'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
  'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
  'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
  'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
  'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
  'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
  'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
  'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
  'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
  'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
  'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
  'command', 'option', 'optionleft', 'optionright']
