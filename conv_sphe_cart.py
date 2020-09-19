# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 21:38:50 2020

@author: Neeraj R
"""

import numpy as np


def sphe_to_cart(rad, polar, azimuth):
    x = rad * np.cos(azimuth) * np.sin(polar)
    y = rad * np.sin(azimuth) * np.sin(polar)
    z = rad * np.cos(polar)
    return x,y,z

def cart_to_sphe(x, y, z):
    rad = (x*x) + (y*y) + (z*z)
    rad = rad**0.5
    azimuth = np.arctan2(y, x)
    polar = np.arccos(z/rad)
    return rad, polar, azimuth
