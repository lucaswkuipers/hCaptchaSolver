# hCaptchaSolver
Work in progress solver for hCaptcha using autogui and tesseract with python. Added simple tkinter interface for faster testing.

Solver works by:
1. Locating captcha box
2. Clicking on captcha automatically (moves mouse in a human-like way using randomized bezier curve)
3. Screenshotting region that displays object to be detected
4. Converting screenshot to text
5. Locating images of object from given text ("bus", "boat"...)


Obs: Works only on english browser, hCaptcha with 100% zoom. (To be expanded)
