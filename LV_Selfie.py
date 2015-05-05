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
            sleep(1)
        #time.sleep(5)
        camera.annotate_text = (pic)
        camera.capture((pic))
        camera.stop_preview()

def takevid(vid):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.start_recording((vid)+'.h264')
        camera.annotate_text = (vid)
        camera.start_preview()
        for i in range(10):
            wii.rumble = 1
            camera.wait_recording(1)
            wii.rumble = 0
            sleep(1)
        camera.stop_preview()
        camera.stop_recording()

def showpic():
    os.system(str('gpicview '+(pic)+(' &')))
    sleep(5)
    os.system('killall gpicview')

#Main body
print 'Press 1 + 2 on your Wii Remote now ...'
sleep(1)
wii = None
i = 1
while not wii:
    try:
      wii=cwiid.Wiimote()
    except RuntimeError:
        if (i>3):
            quit()
            break
    print "Error opening wiimote connection"
    print("attempt",str(i))
    print 'Press 1 + 2 on your Wii Remote now ...'
    i = i + 1
    #quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']


  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  elif (buttons & cwiid.BTN_UP):
      showpic()

  elif (buttons & cwiid.BTN_A):
    #print 'Button A pressed'
    pic = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')+(".jpg")
    print(pic)
    sleep(3)
    takepic(pic)
    sleep(button_delay)          

  elif (buttons & cwiid.BTN_B):
    #print 'Button B pressed'
    vid = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')+(".h264")
    takevid(vid) 
    sleep(button_delay)


#Connect Wiimote and confirm
#Give instructions on what button to use
#Countdown from 5
#Take picture with date time stamp
#Show picture to user
#Close viewer
#Repeat until exit button pressed.
