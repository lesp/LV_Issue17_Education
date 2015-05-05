#Import modules
import cwiid
from time import sleep
from datetime import datetime
import picamera
import os   

#Create variables
button_delay = 0.1


#Define functions

def takepic(pic):
    #CODE TO TAKE PIC
    #Buzz wiimote to indicate countdown
    #Do we need a flash?
    with picamera.PiCamera() as camera:
    camera.start_preview()
    for i in range(5):
        wii.rumble = 1
        sleep(1)
        wii.rumble = 0
    #time.sleep(5)
    camera.annotate_text = (pic)
    camera.capture('/home/pi/Desktop/'+(pic))
    camera.stop_preview()

def takevid(vid):
    #CODE TO TAKE VIDEO
    with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_recording((vid)+'.h264')
    camera.annotate_text = (vid)
    #camera.wait_recording
    for i in range(10):
        wii.rumble = 1
        camera.wait_recording(1)
        wii.rumble = 0
    camera.stop_recording()

def showpic():
    #CODE TO SHOW PIC
    #Use os.system(image viewer + name of file)
    os.system('IMAGEVIEWER',(pic))

#Main body
print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']


  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  elif (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    wii.led = 4
    wii.rumble = 1
    time.sleep(button_delay)
    wii.led = 0
    wii.rumble = 0

  elif(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    right()
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    forward()
    wii.rumble = 1
    time.sleep(button_delay)
    wii.rumble = 0
    
  elif (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    reverse()
    wii.rumble = 1
    time.sleep(button_delay)
    wii.rumble = 0
    
  elif (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_A):
    #print 'Button A pressed'
    pic = datetime.now().strftime('%Y-%m-%d %H:%M:%S')+(".jpg")
    takepic(pic)
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)          

  elif (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)           
    
  elif (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)   
    
  elif (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)


#Connect Wiimote and confirm
#Give instructions on what button to use
#Countdown from 5
#Take picture with date time stamp
#Show picture to user
#Close viewer
#Repeat until exit button pressed.
