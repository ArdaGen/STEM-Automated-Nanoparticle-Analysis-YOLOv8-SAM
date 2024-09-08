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
weights for YOLOv8 particle detection [here](https://drive.google.com/drive/folders/1-ooqb_eBRD0WLau7fTwLcZzDW7jWfmDM?usp=sharing)

## Cite
```
@article{10.1093/mam/ozae044.196,
    author = {Genc, Arda and Marlowe, Justin and Finzel, Jordan and Christopher, Phillip},
    title = "{AI-Enhanced Nanoparticle Analysis: Integrating Single-Shot Object Detection and Vision Transformer for Rapid and Accurate Characterization}",
    journal = {Microscopy and Microanalysis},
    volume = {30},
    number = {Supplement_1},
    pages = {ozae044.196},
    year = {2024},
    month = {07},
    abstract = "{Nanoparticles (NPs) are integral to a wide range of scientific, technological, and industrial applications due to their unique properties. Accurate and efficient analysis of NP characteristics is essential for advancing our understanding of their structure-property relationship and facilitating their applications. In this study, we introduce a novel AI prompt engineering approach to NP analysis, utilizing state-of-the-art single-shot detection (SSD) and vision transformer (ViT) techniques, including Ultralytics YOLOv8 and Meta AI segment-anything model (SAM) frameworks, as illustrated in Figure 1 [1, 2]. Our results demonstrate that AI-powered automated nanoparticle analysis is competitive with human-handcrafted manual methods, significantly reducing the processing and analysis time while maintaining high precision and accuracy.}",
    issn = {1431-9276},
    doi = {10.1093/mam/ozae044.196},
    url = {https://doi.org/10.1093/mam/ozae044.196},
    eprint = {https://academic.oup.com/mam/article-pdf/30/Supplement\_1/ozae044.196/58670943/ozae044.196.pdf},
}

```
## Demo
![](https://github.com/ArdaGen/STEM-Nanoparticle-Analysis-YOLOv8-SAM/blob/main/images/AI_nanoparticle_2.gif)





