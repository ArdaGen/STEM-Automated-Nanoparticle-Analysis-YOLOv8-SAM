# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:11:43 2023

@author: ardag
"""

from skimage.measure import regionprops,regionprops_table
from skimage.segmentation import clear_border
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def particle_analysis(masks, boxes, pixel_size,path_to_csv_file, save=False):
    Diameter = []
    Area = []
    pixel_size = pixel_size  #* pixel_scale 
    for i in range(len(boxes)):
      mask = masks[i,:,:]
      mask = clear_border(mask)
      properties = ['area']
      props = regionprops_table(mask, properties=properties)
      y = props['area']
      A = y*pixel_size*pixel_size
      Area.append(A)
      D = (np.sqrt(A/3.14))*2
      Diameter.append(D)
      
    
    Diameter = [i for i in Diameter if i > 0]
    Diameter = np.array(Diameter)
    Area = [i for i in Area if i > 0]
    Area = np.array(Area)
    print('Mean Diameter : ' + str(np.round(np.mean(Diameter),2)) +' nm')
    print('Mean Area : ' + str(np.round(np.mean(Area),2))+' nm\u00b2') 
    
    fig, axs = plt.subplots(1, 2, sharey = False, tight_layout = False, figsize=(5, 3))
    axs[0].hist(Diameter, bins = 30, facecolor='#2ab0ff', edgecolor='#e0e0e0', linewidth=0.5, alpha=0.7)
    axs[0].set_title("Diameter")
    axs[0].set_xlabel('nm')
    axs[1].hist(Area, bins = 30, facecolor='red', edgecolor='#e0e0e0', linewidth=0.5, alpha=0.7)
    axs[1].set_title("Area")
    axs[1].set_xlabel('nm\u00b2')
    
    if save == True:
        Diameter= np.concatenate(Diameter)
        Area = np.concatenate(Area)
        dict = {'Diameter (nm)' : Diameter,'Area (nm2)' : Area}
        df = pd.DataFrame(dict)
        df.to_csv(path_to_csv_file)
    plt.show()
    return Diameter, Area