# DinosaurGame.py - Plays the dinosaur game in Google Chrome

from PIL import Image
import pyautogui
import mss
import mss.tools
import time
import pyscreenshot as ImageGrab


class Coordinates():
    replayBtn = (684, 231)
    dino = (453, 236)


def restart():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown('down')


def jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('up')
    print('Oink')
    time.sleep(0.15)
    pyautogui.keyUp('up')
    pyautogui.keyDown('down')


print('Screenshot in:')
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# with mss.mss() as sct:
    # The screen part to capture
#    img = sct.grab(x, y, 1, 1)

    # Save to the picture file
#    mss.tools.to_png(img.rgb, img.size, output='oinkster.png')

# with mss.mss() as sct:
    # Use the 1st monitor
    #    monitor = sct.monitors[1]

    # Capture a bbox using percent values
    #    left = monitor["left"] + monitor["width"] * 5 // 100  # 5% from the left
    #    top = monitor["top"] + monitor["height"] * 5 // 100  # 5% from the top
    # lower = top + 400  # 400px height
    #    bbox = (x, y, x, y)

    # Grab the picture
    # Using PIL would be something like:
    # im = ImageGrab(bbox=bbox)
    # im = sct.grab(bbox)  # type: ignore
while True:
    try:
        #            x, y = pyautogui.position()
        bbox = {"top": 236, "left": 453, "width": 1, "height": 3}
#            im = sct.grab(bbox)
#            print(im.size)
#            img = Image.frombytes('RGB', im.size, im.rgb)
#            color = img.getpixel((0, 0))
#            print(color)
        img = ImageGrab.grab((236, 453, 237, 454))
        rGB = img.getpixel((0, 0))
        print(rGB)
        if pyautogui.pixelMatchesColor(236, 453, (51, 57, 59)) is True:
            pyautogui.press('space')
            pyautogui.moveTo(540, 255)
            print('Matched')
    except mss.exception.ScreenShotError as err:
        print(err)
        time.sleep(1)
