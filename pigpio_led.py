#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pigpio
import time

pi = pigpio.pi()
pi.set_mode(21, pigpio.OUTPUT) #GPIO 21 as output Anode

counter = 0
while (counter < 5):
  pi.write(21, 0) #as Anode Low
  print (pi.read(21))
  time.sleep(0.5)
  pi.write(21, 1) #as Anode Hige
  print (pi.read(21))
  time.sleep(1)
  counter = counter + 1

pi.write(21, 0) #as Anode Low
print (".-.-.-.-.-.")

# cleanup
pi.set_mode(21, pigpio.INPUT)
pi.stop()
