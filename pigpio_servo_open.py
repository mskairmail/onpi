#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pigpio
import sys

pi = pigpio.pi()

pi.set_mode(19, pigpio.OUTPUT) #GPIO 19 as output SDI
pi.set_mode(23, pigpio.OUTPUT) #GPIO 23 as output CLK
pi.set_mode(24, pigpio.OUTPUT) #GPIO 24 as output LATCH

pi.write(24, 0) #as LATCH Low
print (pi.read(24))

pi.write(19, 1) #as h
pi.write(23, 1)
pi.write(23, 0)

pi.write(19, 0) #as g
pi.write(23, 1)
pi.write(23, 0)

pi.write(19, 1) #as f
pi.write(23, 1)
pi.write(23, 0)

pi.write(19, 1) #as e
pi.write(23, 1)
pi.write(23, 0)

pi.write(19, 1) #as d
pi.write(23, 1)
pi.write(23, 0)

pi.write(19, 1) #as c
pi.write(23, 1)
pi.write(23, 0)

pi.write(19, 1) #as b
pi.write(23, 1)
pi.write(23, 0)

pi.write(19, 1) #as a
pi.write(23, 1)
pi.write(23, 0)

pi.write(24, 1) #as LATCH HIGH

print (pi.read(24))
print ("abcd efgh")
print ("1111 1101 as [O.]")

pi.set_servo_pulsewidth(21, 1350)
print ("Bar open")
sys.exit(0)
