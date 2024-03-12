import subprocess
import time
subprocess.run(["pip", "install", "mouse"])
time.sleep(3)
import mouse
while True:
    mouse.click(button='left')
    time.sleep(0.001)
