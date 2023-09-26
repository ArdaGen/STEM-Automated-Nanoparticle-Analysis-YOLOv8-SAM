## S/TEM-Nanoparticle-Analysis-Yolov8-SAM
Repository for automated nanoparticle analysis using Yolov8 and SAM in Scanning Transmission Electron Microscopy Images.
This material-agnostic ML workflow successfully detects and segments nanoparticles on different catalyst substrate materials.

* Velox emd
  Read Velox S/TEM images and metadata
* Detector
  Run Yolov8 on the S/TEM images and generate box prompts
* Segmentation
  Generate masks using SAM
* Analysis
  Particle size and area distribution
