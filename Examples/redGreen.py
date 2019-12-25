##################################################
## Switch only green and red to random          ##
## brightness                                   ##
## Example by tng - @TommyBobbins               ##
##################################################

from piglow import PiGlow
from time import sleep
import random

# Maximum random sleep between switching an LED on or off
sleep_period = 0.1

piglow = PiGlow()
# Switch off all the lights first
piglow.all(0)

# We only want to select the Red, and Green LEDs (redGreen)
redGreen_leds = [ "01", "07", "13","04", "10", "16" ]
#red: 01, 07, 13
#green: 04, 10, 16

def random_brightness():
    sleep(random.uniform(0,sleep_period))
    return random.randint(100,255)

while True:
    # Switch one random roy LED to one random brightness
    led_to_switch = int(random.choice(redGreen_leds))
    piglow.led(led_to_switch, random_brightness())
    # Switch one random redGreen LED off 
    led_to_switch = int(random.choice(redGreen_leds))
    piglow.led(led_to_switch, 0)
