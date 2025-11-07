import os
import time
import keyboard
from constants import FOV, TOGGLE_KEY

from termcolor import colored
from colorant import Colorant


CENTER_X, CENTER_Y = 1920 // 2, 1080 // 2

def main():
    os.system('title NguyenLuc - Aimbot Console')
    colorant = Colorant(CENTER_X - FOV // 2, CENTER_Y - FOV // 2, FOV)

    # ==== Giao diện khởi động ====
    print(colored("═══════════════════════════════════════════════════════════════", "cyan"))
    print(colored("                   EM LUC PROJECT - AIMBOT TOOL                ", "yellow"))
    print(colored("═══════════════════════════════════════════════════════════════", "cyan"))
    print()
    print(colored("[VERSION]", "cyan"), colored("v0.1 - Aimbot Only", "white"))
    print(colored("[INFO]", "cyan"), colored("Target color →", "white"), colored("PURPLE (Enemy Highlight)", "magenta"))
    print(colored("[INFO]", "cyan"), colored(f"Press {TOGGLE_KEY} to toggle Aimbot ON / OFF", "white"))
    print(colored("[DEFAULT]", "cyan"), 
          colored("Aimbot Key:", "white"), colored("A and D", "yellow"), " | ",
          colored("Trigger Key:", "white"), colored("None", "yellow"))
    print(colored("[AUTHOR]", "cyan"), colored("Developed by", "white"), colored("Nguyen Luc", "magenta"))
    print()
    print(colored("═══════════════════════════════════════════════════════════════", "cyan"))
    print()

    status = "Disabled"
    last_toggle_time = 0

    try:
        while True:
            # Chống spam toggle liên tục
            if keyboard.is_pressed(TOGGLE_KEY) and time.time() - last_toggle_time > 0.25:
                colorant.toggle()
                last_toggle_time = time.time()
                status = "Enabled " if colorant.toggled else "Disabled "

            status_color = "green" if colorant.toggled else "red"
            print(f'\r{colored("[STATUS]", "cyan")} {colored(status, status_color)}', end='')
            time.sleep(0.02)

    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[INFO]', 'cyan'), colored('Exiting', 'white'))
    finally:
        colorant.close()


if __name__ == '__main__':
    main()

