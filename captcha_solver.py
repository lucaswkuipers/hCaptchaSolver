import pyautogui as pg
import clicker as ck
import time
from PIL import Image, ImageOps, ImageEnhance
import pytesseract as pt

# Captcha

def captcha_click_pos():
    box_pos = pg.locateOnScreen("captcha.png")

    if not box_pos:
        print("Captcha box not found.")
        return None

    click_pos = box_pos[0] + 30, box_pos[1] + 35

    print(f"Captcha click pos - x: {click_pos[0]} y: {click_pos[1]}")
    return click_pos

def click_captcha():
    pos = captcha_click_pos()

    if not pos:
        print("Could not click on captcha box.")
        return None

    ck.click(pos[0], pos[1])
    print("Clicked on captcha.")
    return True

# Recaptcha

def recaptcha_pos():
    pos = pg.locateOnScreen("recaptcha_header.png")

    if not pos:
        print("Recaptcha header not found.")
        return None
    
    print(f"Recaptcha header pos - x: {pos[0]} y: {pos[1]}")
    return pos

def object_screenshot():
    header_pos = recaptcha_pos()

    if not header_pos:
        return None
    
    left = header_pos[0] + 110
    width = 60

    top= header_pos[1] + 35
    height = 30

    img = pg.screenshot(region=(left, top, width, height))
    time.sleep(1)
    img.save("object.png")
    print("Taken screenshot")

    pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    text = pt.image_to_string(Image.open('object.png'))
    print("What is that object?", text)
    return True