import ctypes
import keyboard
import time

# Get necessary functions from user32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010

def move_mouse(dx, dy):
    user32.mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)

def main():
        print("Use numpad keys to control the mouse:")
        print("i: Move Up | k: Move Down | j: Move Left | l: Move Right")
        print("u: Left Click | o: Right Click | /: Slow down | -: Quit")
        
        STEP = 30
        DELAY = 0.02
        STEP_SLOW = 10
        DELAY_SLOW = 0.1
        LEFT_MOUSE_DOWN = False
        RIGHT_MOUSE_DOWN = False

        while True:
            if keyboard.is_pressed("/"):
                step = STEP_SLOW
                delay = DELAY_SLOW
            else:
                step = STEP
                delay = DELAY

            if keyboard.is_pressed("i"):
                move_mouse(0, -step)
            elif keyboard.is_pressed("k"):
                move_mouse(0, step)
            if keyboard.is_pressed("j"):
                move_mouse(-step, 0)
            elif keyboard.is_pressed("l"):
                move_mouse(step, 0)
            
            if keyboard.is_pressed("u"): # Left click
                if LEFT_MOUSE_DOWN == False:
                    LEFT_MOUSE_DOWN = True
                    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            else:
                if LEFT_MOUSE_DOWN == True:
                    LEFT_MOUSE_DOWN = False
                    user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

            if keyboard.is_pressed("o"): # Right click
                if RIGHT_MOUSE_DOWN == False:
                    RIGHT_MOUSE_DOWN = True
                    user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            else:
                if RIGHT_MOUSE_DOWN == True:
                    RIGHT_MOUSE_DOWN = False
                    user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

            if keyboard.is_pressed("-"):
                print("Exiting.")
                break

            time.sleep(delay)

main()
print("Program interrupted.")
user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
