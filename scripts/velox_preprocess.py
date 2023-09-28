# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:05:30 2023

@author: ardag
"""
import h5py
import json
import cv2
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt

def velox_emd (path, adap = False):
    file = h5py.File(path,'r', rdcc_nbytes=10485760)

    list_data= list(file['Data/Image'].values())
    group = list_data[0]
    data = group['Data']
    tempmetadata = group['Metadata'][:, 0]
    validmetadataindex = np.where(tempmetadata > 0)
    metadata = tempmetadata[validmetadataindex].tobytes()
    metadata_json = json.loads(metadata.decode('utf-8','ignore'))
    pixel_size = round(float(metadata_json["BinaryResult"]["PixelSize"]["width"]) * 1e9, 3) 
    detector = metadata_json["BinaryResult"]["Detector"]
    data_squeezed = np.squeeze(data[:])
    
    if adap == True:
        data_squeezed = exposure.equalize_adapthist(data_squeezed, clip_limit=0.01)
        
  
    if detector == 'HAADF':
        data_squeezed_8bit = ((data_squeezed/np.max(data_squeezed))*255).astype('uint8')
        data_squeezed_inverted =cv2.bitwise_not(data_squeezed_8bit)
        magnification = metadata_json['CustomProperties']['StemMagnification']['value']
        scan_size = metadata_json['Scan']['ScanSize']['width']
        img_x = cv2.cvtColor(data_squeezed_inverted, cv2.COLOR_GRAY2RGB)
        img =  cv2.cvtColor(data_squeezed_8bit, cv2.COLOR_GRAY2RGB) 
        print ( 'Detector : ' + str(detector))
        print( 'Mag : ' + str(magnification))
        print( 'Scan size :' + str(scan_size))
        print( 'Pixel size (nm) : ' + str(pixel_size))
        

    else :
        data_squeezed_8bit = ((data_squeezed/np.max(data_squeezed))*255).astype('uint8')
        img = cv2.cvtColor(data_squeezed_8bit, cv2.COLOR_GRAY2RGB) 
        magnification = round( float(metadata_json['Optics']['NominalMagnification']), 1)
        frame_size = data_squeezed_8bit.shape[0]
        print ( 'Detector : ' + str(detector))
        print( 'Mag : ' + str(magnification))
        print ('Image size :' + str(frame_size))
        print( 'Pixel size (nm) : ' + str(pixel_size))
        img_x = img
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    plt.imshow(img)
    return img_x, img, pixel_size

