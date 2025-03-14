## Automated S/TEM-Nanoparticle-Analysis-YOLOv8-SAM


![8](https://github.com/ArdaGen/STEM-Nanoparticle-Analysis-YOLOv8-SAM/blob/main/images/flow.svg)


Repository for automated nanoparticle analysis of Scanning Transmission Electron Microscopy (S/TEM) images using [YOLOv8](https://github.com/ultralytics/ultralytics) and [segment anything model (SAM)](https://github.com/facebookresearch/segment-anything).
This material-agnostic ML workflow successfully detects and segments nanoparticles on different catalytic substrate materials.

![9](https://github.com/ArdaGen/STEM-Automated-Nanoparticle-Analysis-YOLOv8-SAM/blob/main/images/results10.png)

Sets of object detection, segmentation, and NP analysis results from BF-TEM image of Pt NPs on graphite support (above) and HAADF STEM image of Ru NPs on Alumina support materials (below).


## Scripts
* **Data reader** <br>
  Read ".emd", ".emi", ".dm3", ".dm4"
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
Install RosettaSciIO
```
pip install rosettasciio
```
Install Ultralytics for YOLOv8
```
pip install ultralytics
```
Install Segment Anything Model (SAM)
```
https://github.com/facebookresearch/segment-anything
```
weights for YOLOv8 particle detection [here](https://drive.google.com/drive/folders/1-ooqb_eBRD0WLau7fTwLcZzDW7jWfmDM?usp=sharing)
<br>
<br>
## AI-assisted particle analysis software nanoDetect
[Please fill out the form here to gain access to nanoDetect software installer](https://docs.google.com/forms/d/e/1FAIpQLScmBEpYrSrEPY_Y80fxzhahPQM6Qyug_sTkhP42lKNQTQ7Wmw/viewform?usp=header)

## Demo
![](https://github.com/ArdaGen/STEM-Automated-Nanoparticle-Analysis-YOLOv8-SAM/blob/main/images/nanoDetect_v2.2.gif)

## Cite
```
@article{GENC2025114116,
title = {A versatile machine learning workflow for high-throughput analysis of supported metal catalyst particles},
journal = {Ultramicroscopy},
volume = {271},
pages = {114116},
year = {2025},
issn = {0304-3991},
doi = {https://doi.org/10.1016/j.ultramic.2025.114116},
url = {https://www.sciencedirect.com/science/article/pii/S0304399125000154},
author = {Arda Genc and Justin Marlowe and Anika Jalil and Daniel Belzberg and Libor Kovarik and Phillip Christopher},
keywords = {Machine learning, Heterogeneous catalysts, Particle analysis, Transmission electron microscopy, Instance segmentation},
abstract = {Accurate and efficient characterization of nanoparticles (NPs), particularly regarding particle size distribution, is essential for advancing our understanding of their structure-property relationship and facilitating their design for various applications. In this study, we introduce a novel two-stage artificial intelligence (AI)-driven workflow for NP analysis that leverages prompt engineering techniques from state-of-the-art single-stage object detection and large-scale vision transformer (ViT) architectures. This methodology is applied to transmission electron microscopy (TEM) and scanning TEM (STEM) images of heterogeneous catalysts, enabling high-resolution, high-throughput analysis of particle size distributions for supported metal catalyst NPs. The model's performance in detecting and segmenting NPs is validated across diverse heterogeneous catalyst systems, including various metals (Ru, Cu, PtCo, and Pt), supports (silica (SiO2), γ-alumina (γ-Al2O3), and carbon black), and particle diameter size distributions with mean and standard deviations ranging from 1.6 ± 0.2 nm to 9.7 ± 4.6 nm. The proposed machine learning (ML) methodology achieved an average F1 overlap score of 0.91 ± 0.01 and demonstrated the ability to disentangle overlapping NPs anchored on catalytic support materials. The segmentation accuracy is further validated using the Hausdorff distance and robust Hausdorff distance metrics, with the 90th percent of the robust Hausdorff distance showing errors within 0.4 ± 0.1 nm to 1.4 ± 0.6 nm. Our AI-assisted NP analysis workflow demonstrates robust generalization across diverse datasets and can be readily applied to similar NP segmentation tasks without requiring costly model retraining.}
}

```




