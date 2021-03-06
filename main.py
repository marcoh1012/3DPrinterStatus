from settings import url, api_token
from rpi_ws281x import PixelStrip, Color
from lights import breathing, colorWipe, rainbowCycle
import time
import requests
import json




# LED strip configuration:
LED_COUNT = 60        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()



def getPrinterStatus(): 
    """Get the status of Octoprint usin the local host url"""

    res = requests.get(url, headers={'X-Api-Key':api_token})
    
    if res.status_code == 200:
        data = json.loads(res.content.decode('utf-8'))
        return data['state']
    else:
        rainbowCycle(strip)
        return 'Cant Connect'

def setColor(state):
    if state == 'Operational':
        colorWipe(strip, color=Color(0,255,0))
        # Set to color Green
        print('Operational')
    elif state == 'Printing':
        breathing(strip, color=Color(0,255,0))
        # Set to Green color flashing
        print('printing')
    elif state == 'Paused' or state == 'Pausing':
        # Set color to yellow
        colorWipe(strip,color=Color(255, 165, 0))
        print('paused')

    elif state == "Error" or state == "Offline after error":
        #Breathing color in Red
        breathing(strip,color=Color(255,0,0))
        print("Error")
    elif state == 'Cancelling' or state == 'Offline':
        # Set color to Red
        colorWipe(strip, color=Color(255,0,0))
        print('offline')
    else:
        rainbowCycle(strip)


print('Connecting to Printer')



while True:
    time.sleep(1)
    state = getPrinterStatus()
    setColor(state)
