# Use the get_attention(headset) function in neurosky.py to get the current attention level
# Will need to find a way to constantly update the attention level 
# (something like an infinite loop, or constant calls to a function)

# Potential variables to create: attention_threshold, attention (= get_attention(headset))

import mindwave
import pandas as pd
import time

headset = None

def connect(version):
    '''
    Code to connect to Neurosky, adapted from neurosky.py.
    Make sure that the headset (MindWave Mobile) is connected to your computer 
    using Bluetooth to avoid connection issues.
    '''
    global headset
    
    print("Connecting...")
    if version == "mac":
        headset = mindwave.Headset('/dev/tty.MindWaveMobile-SerialPo') # mac version
    else:
        headset = mindwave.Headset('COM6') # windows version. set up COM port first (see video)
    print("Connected!")
    
    print("Starting...")
    # Wait for the headset to steady down
    while (headset.poor_signal > 5 or headset.attention == 0):
        time.sleep(0.1)
    print('Started!')
    
def get_attention():
    '''
    Obtain the current Neurosky attention level measure.
    Use this in the game code to print the attention measure.
    '''
    return headset.attention
    
def disconnect():
    '''
    Code to disconnect from Neurosky.
    '''
    headset.stop()
    print("Stopped!")
    
def test_connection(): 
    '''
    Testing if code runs as expected.
    '''
    connect("mac")
    
    t_end = time.time() + 10 # run for 10 seconds
    while time.time() < t_end:
        print(get_attention())
        time.sleep(0.01)
    
    disconnect()