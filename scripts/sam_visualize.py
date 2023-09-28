# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:59:59 2023

@author: ardag
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

def show_mask(mask, ax, random_color=False, save = False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30/255, 144/255, 255/255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)

def visualize_mask (masks, img, path_to_imageseg, img_size = (256, 256), save = False):
    plt.figure(figsize=(8, 8))
    plt.imshow(cv2.resize(img, img_size))
    for mask in masks:
        show_mask(cv2.resize(mask, img_size), plt.gca(), random_color=True)
    plt.axis('off')
    if save == True:
        plt.savefig(path_to_imageseg, bbox_inches='tight', pad_inches = 0)
    plt.show()

def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))