#!/usr/bin/python
 
import spidev
import os
import time
 
# Define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
swt_channel = 0
vrx_channel = 1
vry_channel = 2
 
#Time delay, which tells how many seconds the value is read out
delay = 0.5
 
# Spi oeffnen
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Function for reading the MCP3008 channel between 0 and 7
def readChannel(channel):
  val = spi.xfer2([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data
 
 
# endless loop
while True:
 
  # Determine position
  vrx_pos = readChannel(vrx_channel)
  vry_pos = readChannel(vry_channel)
 
  # SW determine
  swt_val = readChannel(swt_channel)
 
  # output
  print("VRx : {}  VRy : {}  SW : {}".format(vrx_pos,vry_pos,swt_val))
 
  # wait
  time.sleep(delay)