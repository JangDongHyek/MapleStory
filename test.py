import win32gui
import pyautogui
import newLIB as fc
import lib

fc.screenshot("A",[690, 170, 1230, 350])
fc.screenshot("full")

asd = fc.imageYolo(None,[690, 170, 1230, 350])

print(asd)