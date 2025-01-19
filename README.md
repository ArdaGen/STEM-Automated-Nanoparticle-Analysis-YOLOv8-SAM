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
[Please fill out the assessment form here to gain access to nanoDetect software](https://docs.google.com/forms/d/e/1FAIpQLScmBEpYrSrEPY_Y80fxzhahPQM6Qyug_sTkhP42lKNQTQ7Wmw/viewform?usp=header)

## Demo
![](https://github.com/ArdaGen/STEM-Automated-Nanoparticle-Analysis-YOLOv8-SAM/blob/main/images/nanoDetect_v2.2.gif)

## Cite
```
@misc{genc2024versatilemachinelearningworkflow,
      title={A versatile machine learning workflow for high-throughput analysis of supported metal catalyst particles}, 
      author={Arda Genc and Justin Marlowe and Anika Jalil and Libor Kovarik and Phillip Christopher},
      year={2024},
      eprint={2410.01213},
      archivePrefix={arXiv},
      primaryClass={cond-mat.mtrl-sci},
      url={https://arxiv.org/abs/2410.01213}, 
}

```




