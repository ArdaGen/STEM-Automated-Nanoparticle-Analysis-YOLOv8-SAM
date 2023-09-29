## S/TEM-Nanoparticle-Analysis-Yolov8-SAM
![8](https://github.com/ArdaGen/TEM-Nanoparticle-Analysis-Yolov8-SAM/assets/86938894/8e16d1c4-0ef7-496e-bc2b-3cfc1e19c18f)
<br>
<br>
Repository for automated nanoparticle analysis using Yolov8 and SAM in Scanning Transmission Electron Microscopy Images.
This material-agnostic ML workflow successfully detects and segments nanoparticles on different catalyst substrate materials.

## Scripts
* **Velox emd** <br>
  Read Velox S/TEM images and metadata
* **Detector** <br>
  Run Yolov8 on the S/TEM images and generate box prompts <br>
  Generate masks using SAM
* **SAM visualize** <br>
  Visualize segmentations
* **Analysis** <br>
  Particle size and area distribution
## Model weights
Weights for yolov8 nanoparticle object detection <br>
https://drive.google.com/file/d/18dHxlF30ZkPLlikhx7hBWgXhLkpwIk8v/view?usp=sharing

Weights for SAM <br>
https://drive.google.com/file/d/1iYPrlGzIoN8-sfg2khJIP6mGgFDSNP4-/view?usp=sharing 
<br>
<br>
## Installation
Install pytorch
```
https://pytorch.org/get-started/locally/
```
Install ultralytics for Yolov8
```
pip install ultralytics
```
Install segment anything model (SAM)
```
https://github.com/facebookresearch/segment-anything
```


https://github.com/ArdaGen/TEM-Nanoparticle-Analysis-Yolov8-SAM/assets/86938894/58c43ba5-14b6-4961-be76-50267595c13c





