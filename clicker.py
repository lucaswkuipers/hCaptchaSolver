import pyautogui as pg
import time as tm
import numpy as np
import math
from scipy import interpolate
from random import randint

pg.PAUSE = 0

def click(x, y):
    pg.moveTo(x, y, 0.7)
    tm.sleep(1.25)
    pg.click(x, y)

def dist(x0, y0, x, y):
    return math.sqrt((x - x0) ** 2 + (y - y0) ** 2)

def move(x, y):
    x0, y0 = pg.position() # Current position

    # Control points
    num_ctrl_pts = random.randint(4, 6) 
    x_pts = np.linspace(x0, x, num=num_ctrl_pts, dtype='int')
    y_pts = np.linspace(y0, y, num=num_ctrl_pts, dtype='int')

    # Randomizing inner points
    max_offset = 10
    xr = [randint(-max_offset, max_offset) for k in range(num_ctrl_pts)]
    yr = [randint(-max_offset, max_offset) for k in range(num_ctrl_pts)]
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline.
    deg = 3 
    tck, u = interpolate.splprep([x, y], k=deg)