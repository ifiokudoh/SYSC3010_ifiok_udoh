from sense_hat import SenseHat
import time

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
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, Y, Y, Y, Y, Y, Y, O,
  O, O, O, Y, Y, O, O, O,
  O, O, O, Y, Y, O, O, O,
  O, O, O, Y, Y, O, O, O,
  O, O, O, Y, Y, O, O, O,
  O, Y, Y, Y, Y, Y, Y, O,
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
  O, G, O, O, O, O, G, O,
  O, G, O, O, O, O, G, O,
  O, G, O, O, O, O, G, O,
  O, G, O, O, O, O, G, O,
  O, G, G, O, O, G, G, O,
  O, O, G, G, G, G, O, O,
  O, O, O, O, O, O, O, O,
  ]
  return logo
  
images = [first_Initial, last_Initial]
count = 0
while True:
  events = s.stick.get_events()
  if events:
    for event in events:
      if event.action == 'pressed':
        if count == 0:
          count = 1
        else:
          count = 0
            
        s.set_pixels(images[count]())
        