import tkinter as tk
import pyautogui as pg
import captcha_solver as cs

class Window:
    title = "Captcha Solver"
    width = "300"
    height = "25"
    geometry = f"{width}x{height}"

root = tk.Tk()
root.title(Window.title)
root.geometry(Window.geometry)

# Buttons

click_captcha_btn = tk.Button(root, text="Click captcha", command=cs.click_captcha)
click_captcha_btn.pack(side=tk.LEFT)

find_recaptcha_btn = tk.Button(root, text="Object Screenshot", command=cs.object_screenshot)
find_recaptcha_btn.pack(side=tk.RIGHT)

root.mainloop()