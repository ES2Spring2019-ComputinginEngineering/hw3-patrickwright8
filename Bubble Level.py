# Name: Patrick Wright
# Partners: Nick Ragusa and David Fricke

import microbit
import math

while True:
    microbit.sleep(200)
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()
    if z ==0:
        z=1
    t1 = (math.atan(x/z))*57.3
    t2 = (math.atan(y/z))*57.3
    print ((t1, t2)) #This line plots the two angles for debugging purposes
    # The following lines are a series of conditionals that determine where the bubble should
    # be placed based on angles t1 and t2
    # Note: this program uses an LED bubble rather than an arrow to measure the angle.
    # Therefore, a dot on LED (4, 4) would mean that the microbit must be tilted in the direction
    # of the LED.
    if t1>-5 and t1<5 and t2>-5 and t2<5:
        microbit.display.clear()
        microbit.display.set_pixel(2, 2, 9)
    elif t1<-5 and t1>-15 and t2>-5 and t2<5:
        microbit.display.clear()
        microbit.display.set_pixel(1, 2, 9)
    elif t1<-15 and t2>-5 and t2<5:
        microbit.display.clear()
        microbit.display.set_pixel(0, 2, 9)
    elif t1>5 and t1<15 and t2>-5 and t2<5:
        microbit.display.clear()
        microbit.display.set_pixel(3, 2, 9)
    elif t1>15 and t2>-5 and t2<5:
        microbit.display.clear()
        microbit.display.set_pixel(4, 2, 9)
    elif t1<5 and t1>-5 and t2<-5 and t2>-15:
        microbit.display.clear()
        microbit.display.set_pixel(2, 1, 9)
    elif t1<5 and t1>-5 and t2<-15:
        microbit.display.clear()
        microbit.display.set_pixel(2, 0, 9)
    elif t1<5 and t1>-5 and t2<15 and t2>5:
        microbit.display.clear()
        microbit.display.set_pixel(2, 3, 9)
    elif t1<5 and t1>-5 and t2>15:
        microbit.display.clear()
        microbit.display.set_pixel(2, 4, 9)
    elif t1>-15 and t1<-5 and t2>-15 and t2<-5:
        microbit.display.clear()
        microbit.display.set_pixel(1, 1, 9)
    elif t1<-15 and t2<-15:
        microbit.display.clear()
        microbit.display.set_pixel(0, 0, 9)
    elif t1>5 and t1<15 and t2>5 and t2<15:
        microbit.display.clear()
        microbit.display.set_pixel(3, 3, 9)
    elif t1>15 and t2>15:
        microbit.display.clear()
        microbit.display.set_pixel(4, 4, 9)
    elif t1>5 and t1<15 and t2>-15 and t2<-5:
        microbit.display.clear()
        microbit.display.set_pixel(3, 1, 9)
    elif t1>15 and t2<-15:
        microbit.display.clear()
        microbit.display.set_pixel(4, 0, 9)
    elif t2>5 and t2<15 and t1>-15 and t1<-5:
        microbit.display.clear()
        microbit.display.set_pixel(1, 3, 9)
    elif t2>15 and t1<-15:
        microbit.display.clear()
        microbit.display.set_pixel(0, 4, 9)
    else:
        microbit.display.clear()