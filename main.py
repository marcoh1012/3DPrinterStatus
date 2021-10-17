from settings import url, api_token
import time
import requests
import json


def getPrinterStatus(): 
    """Get the status of Octoprint usin the local host url"""

    res = requests.get(url, headers={'X-Api-Key':api_token})
    
    if res.status_code == 200:
        data = json.loads(res.content.decode('utf-8'))
        return data['state']
    else:
        return 'Cant Connect'

def setColor(state):
    if state == 'Operational':
        # Set to color Green
        print('connected')
    elif state == 'Printing':
        # Set to Green color flashing
        print('printing')
    elif state == 'Paused' or state == 'Pausing':
        # Set color to yellow
        print('paused')
    elif state == 'Cancelling' or state == "Error" or state == 'Offline' or state == 'Offline after error':
        # Set color to Red
        print('offline')


while True:
    time.sleep(5)
    state = getPrinterStatus()
    setColor(state)
