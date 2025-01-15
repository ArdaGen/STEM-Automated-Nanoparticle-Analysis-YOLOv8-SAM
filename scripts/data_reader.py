# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:12:23 2024

@author: ardag
"""

import cv2
from rsciio.digitalmicrograph import file_reader as dm_read
from rsciio.emd import file_reader as emd_read
from rsciio.tia import file_reader as tia_read
import os

def load(path):
    _, extension = os.path.splitext(path)
    if extension.lower() in ('.dm3', '.dm4'):
        
        dm =  dm_read(path)
        pixel_size = round(dm[0]['original_metadata']["ImageList"]["TagGroup0"]["ImageData"]["Calibrations"]["Dimension"]["TagGroup0"]["Scale"],4)
        img = dm[0]["data"]
        img = (img/img.max())*255
        img = cv2.normalize(img, None, 0,255.0, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img_x =cv2.bitwise_not(img)
    if extension.lower() == '.emd':
        emd = emd_read(path)
        pixel_size = round(float(emd[0]['original_metadata']["BinaryResult"]['PixelSize']["width"])*1e9,3)
        img = emd[0]["data"]
        img = cv2.normalize(img, None, 0,255.0, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img_x =cv2.bitwise_not(img)
    if extension.lower() == '.emi':
        tia = tia_read(path)
        pixel_size = round(tia[0]['original_metadata']['ser_header_parameters']['CalibrationDeltaX']*1e9, 3)
        img = tia[0]['data']
        img = (img/img.max())*255
        img = cv2.normalize(img, None, 0,255.0, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        img_x =cv2.bitwise_not(img)
    
    return img_x, img, pixel_size
