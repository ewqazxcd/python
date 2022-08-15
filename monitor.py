import time
import pyscreenshot as ImageGrab
from ftplib  import FTP
from pathlib import Path

while True:
  imgFull = ImageGrab.grab(backend="mss", childprocess=False)
  img = imgFull.resize((356, 200))
  img.save("../screen.jpeg", "JPEG")

  print(time.strftime("saved %H:%M:%S"))

  time.sleep(60)
