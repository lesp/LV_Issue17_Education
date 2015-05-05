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
    with picamera.PiCamera() as camera:
        camera.start_preview()
        for i in range(5):
            wii.rumble = 1
            sleep(1)
            wii.rumble = 0
            sleep(1)
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
            sleep(1)
            wii.rumble = 0
            camera.wait_recording(1)
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
        if (i>2):
            quit()
            break
    print "Error opening wiimote connection"
    print("Attempt "+str(i))
    print 'Press 1 + 2 on your Wii Remote now ...'
    i = i + 1
    #quit()

print('Wii Remote connected...\n')
print('Press\n')
print('A to take a photo with a 5 second timer\n')
print('Countdown will be communicated using vibration motor in wiimote\n')
print('Up to display the last photo taken\n')
print('B to record 10 seconds of video\n')
print('Countdown will be communicated using vibration motor in wiimote\n')

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
