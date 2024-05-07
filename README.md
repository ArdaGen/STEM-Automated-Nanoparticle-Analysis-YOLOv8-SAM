## Automated S/TEM-Nanoparticle-Analysis-YOLOv8-SAM


![8](https://github.com/ArdaGen/STEM-Nanoparticle-Analysis-YOLOv8-SAM/blob/main/images/g37046.svg)


Repository for automated nanoparticle analysis of Scanning Transmission Electron Microscopy (S/TEM) images using [YOLOv8](https://github.com/ultralytics/ultralytics) and [segment anything model (SAM)](https://github.com/facebookresearch/segment-anything).
This material-agnostic ML workflow successfully detects and segments nanoparticles on different catalytic substrate materials.

![9](https://github.com/ArdaGen/STEM-Automated-Nanoparticle-Analysis-YOLOv8-SAM/blob/main/images/results10.png)

Sets of object detection, segmentation, and NP analysis results from BF-TEM image of Pt NPs on graphite support (above) and HAADF STEM image of Ru NPs on Alumina support materials (below).


## Scripts
* **Velox emd** <br>
  Read Thermo Fisher Scientific Velox S/TEM image and metadata
* **Detector** <br>
  Run YOLOv8 on the S/TEM images and generate box prompts <br>
  Segment nanoparticles using box prompts and SAM
* **SAM visualize** <br>
  Visualize segmentation
* **Analysis** <br>
  Particle size and area distribution <br>


## Installation
Install [PyTorch](https://pytorch.org/get-started/locally/)
<br>
<br>
Install Ultralytics for YOLOv8
```
pip install ultralytics
```
Install Segment Anything Model (SAM)
```
https://github.com/facebookresearch/segment-anything
```
## Cite
If you use this code in your research, please use the following DOI badge 
<br>
<br>
[![DOI](https://zenodo.org/badge/696562764.svg)](https://zenodo.org/badge/latestdoi/696562764)
## Demo
![](https://github.com/ArdaGen/STEM-Nanoparticle-Analysis-YOLOv8-SAM/blob/main/images/AI_nanoparticle_2.gif)





