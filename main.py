from settings import url, api_token
import time
import requests
import json


def getPrinterStatus(): 
    """Get the status of Octoprint usin the local host url"""

    res = requests.get(url, headers={'X-Api-Key':api_token})
    
    if res.status_code == 200:
        data = json.load(res.content)
        return data['state']
    else:
        return 'Cant Connect'

def setColor(state):
    if state == 'Operational':
        # Set to color Green
    elif state == 'Printing':
        # Set to Green color flashing
    elif state == 'Paused' or state == 'Pausing':
        # Set color to yellow
    elif state == 'Cancelling' or state == "Error" or state == 'Offline' or state == 'Offline after error':
        # Set color to Red


while True:
    time.sleep(5)
    state = getPrinterStatus()
    print(state)
    setColor(state)
