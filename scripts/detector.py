# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:57:48 2023

@author: ardag
"""


import numpy as np
import cv2
import matplotlib.pyplot as plt
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
from segment_anything.utils import transforms
import torch
from sam_visualize import show_mask
import sys
sys.path.append("..")


def object_detection (img_x, img, path_to_image, img_size=1024, pred_score = 0.25, overlap_thr =0.5, save = False, s_txt = False):
    from ultralytics import YOLO
    path_to_weights_obj = "best12x.pt" # Weights for the YOLO
    model = YOLO(path_to_weights_obj)
    model.to('cuda')
    # Run detection on the image
    results = model.predict(source = img_x, imgsz = img_size, conf = pred_score, max_det= 4000, iou = overlap_thr, save_txt = s_txt)
    
    # Get bounding boxes
    for result in results:
        boxes = result.boxes
     
    bbox = boxes.xyxy.tolist()
    #class_id=results[0].boxes.cls.cpu().numpy().astype(int)
    #points = [item[:2] for item in bbox]
    # Visualize bounding boxes
    res_plotted = results[0].plot(labels=False, line_width=2, img=img)
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    plt.imshow(res_plotted)
    if save == True:
        plt.savefig(path_to_image,bbox_inches='tight', pad_inches = 0)
    plt.show()
    #plot_bboxes(img, results[0].boxes.boxes, score=False)
    
    return bbox


def segmentation(img, bbox, erode = False, dilate = False, kernel_size =(5, 5) ):


    # Load the model
    sam_checkpoint = "sam_vit_b_01ec64.pth" # weights for the SAM
    model_type = "vit_b"
    device = "cuda"
    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)
    predictor = SamPredictor(sam)


    # Run model on the image
    predictor.set_image(img)


    input_boxes = torch.tensor(bbox, device=predictor.device)
    transformed_boxes = predictor.transform.apply_boxes_torch(input_boxes, img.shape[:2])
    masks, _, _ = predictor.predict_torch(
        point_coords=None,
        point_labels=None,
        boxes=transformed_boxes,
        multimask_output=False,
    )
    
    masks_array = masks.cpu().numpy().squeeze()
    masks3D_array = masks_array.astype('uint8')
    
    if erode == True:
        # Erode
        
        kernel = np.ones((kernel_size), np.uint8)
        masks3D_erode = []
        for mask in masks3D_array:
            mask = cv2.erode(mask, kernel)
            masks3D_erode.append(mask)
        masks3D_erode = np.asarray(masks3D_erode)
        masks3D_array = masks3D_erode 
        
    if dilate == True:
        # Erode
        
        kernel = np.ones((kernel_size), np.uint8)
        masks3D_erode = []
        for mask in masks3D_array:
            mask = cv2.dilate(mask, kernel)
            masks3D_erode.append(mask)
        masks3D_erode = np.asarray(masks3D_erode)
        masks3D_array = masks3D_erode 
    
    return masks3D_array


def segmentation_fast(img, bbox):


    from ultralytics import SAM
    model = SAM('mobile_sam.pt')
    device = "cpu"

    results = model.predict(img, bboxes=bbox, save=False, device=device)

    for result in results:
        mask = result.masks
    masks3D_array = mask.data
    masks3D_array = masks3D_array.cpu().numpy()
    masks3D_array= masks3D_array.astype('uint8')
    
    return masks3D_array
