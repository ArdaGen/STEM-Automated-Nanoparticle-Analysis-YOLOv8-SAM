## S/TEM-Nanoparticle-Analysis-Yolov8-SAM
Repository for automated nanoparticle analysis using Yolov8 and SAM in Scanning Transmission Electron Microscopy Images.
This material-agnostic ML workflow successfully detects and segments nanoparticles on different catalyst substrate materials.

* **Velox emd** <br>
  Read Velox S/TEM images and metadata
* **Detector** <br>
  Run Yolov8 on the S/TEM images and generate box prompts
* **Segmentation** <br>
  Generate masks using SAM
* **Analysis** <br>
  Particle size and area distribution
