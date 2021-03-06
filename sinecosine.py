"""
sinecosine.py
Author: David Wilson
Credit: None

Assignment:

In this assignment you must use *list comprehensions* to generate sprites that show the behavior
of certain mathematical functions: sine and cosine. 

The sine and cosine functions are provided in the Python math library. These functions are used
to relate *angles* to *rectangular* (x,y) coordinate systems and can be very useful in computer
game design.

Unlike the last assignment using ggame`, this one will not provide any "skeleton" code to fill
in. You should use your submission for the Picture assignment 
(https://github.com/HHS-IntroProgramming/Picture) as a reference for starting this assignment. 

See:
https://github.com/HHS-IntroProgramming/Sine-Cosine/blob/master/README.md
for a detailed list of requirements for this assignment.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Programmed-Graphics
for general information on using list comprehensions to generate graphics.

http://brythonserver.github.io/ggame/
for detailed information on ggame.
"""

from ggame import App, Color, LineStyle, Sprite, CircleAsset
from math import sin, cos, radians

Black = Color(0x000000, 1.0)
Blue = Color(0x0000ff, 1.0)
Red = Color(0xff0000, 1.0)
Purple = Color(0x800080, 1.0)

Line = LineStyle(1, Black)

BlueCircle = CircleAsset(5, Line, Blue)
RedCircle = CircleAsset(5, Line, Red)
PurpleCircle = CircleAsset(5, Line, Purple)

XCorSC = range(0, 360, 10)
XCorCrc = [100+100*cos(radians(x)) for x in XCorSC]

SinGraph = [Sprite(BlueCircle, (x, 100+100*sin(radians(x)))) for x in XCorSC]
CosGraph = [Sprite(RedCircle, (x, 100+100*cos(radians(x)))) for x in XCorSC]
CrcGraph = [Sprite(PurpleCircle, (100+100*cos(radians(x)), 400+100*sin(radians(x)))) for x in XCorSC]

myapp = App()
myapp.run()