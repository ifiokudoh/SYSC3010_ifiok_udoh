from sense_emu import SenseHat
import time
from thermometer_emu import thermometer

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def first_Initial():
  G = green
  Y = yellow
  B = blue
  R = red
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, R, R, R, R, R, R, O,
  O, O, O, R, R, O, O, O,
  O, O, O, R, R, O, O, O,
  O, O, O, R, R, O, O, O,
  O, O, O, R, R, O, O, O,
  O, R, R, R, R, R, R, O,
  O, O, O, O, O, O, O, O,
  ]
  return logo
  
def last_Initial():
  G = green
  Y = yellow
  B = blue
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, B, O, O, O, O, B, O,
  O, B, O, O, O, O, B, O,
  O, B, O, O, O, O, B, O,
  O, B, O, O, O, O, B, O,
  O, B, B, O, O, B, B, O,
  O, O, B, B, B, B, O, O,
  O, O, O, O, O, O, O, O,
  ]
  return logo
  
images = [first_Initial, last_Initial]
count = 0
thermo = thermometer()

while True:
    time.sleep(1) 
    temp = thermo.read()
    if temp > 20:
        count = 1
        print("Temperature is" + str(temp) + "above 20 degress, set initial is U")

    else:
        count = 0
        print("Temperature is" + str(temp) + "below 20 degress, set initial is I")

            
    s.set_pixels(images[count]())
        