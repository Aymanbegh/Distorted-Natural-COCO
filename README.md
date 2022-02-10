# Object-Detection-under-Local-Distortions-

This repository provides additional new benchmark dataset constructed for natural in-capture distortions from MS-COCO dataset to better assess the reliability
of the object detection models in case of real distortions.

Requirements
-----------------------------------

    MS-COCO 2017 dataset (validation set)
    Python 3.8 (Tested on it)
    Requirement of object detction model tested

Overview
-----------------------------------

In the existing methods, robustness evaluations of object detection algorithms were performed on synthetic distortions or specific datasets which limits the extension of those studies in real-world applications.
Therefore, we have done a manual identification of the natural distortions present in the MS-COCO validation set to better assess the robustness in real scenarios. 
It is worth noticing that the selected sub-sets from MS-COCO contain images with global distortions and the associated object annotations. Whereas,
in the case of local distortions, only affected objects are considered as in the following figure:

![image](https://user-images.githubusercontent.com/80038451/153512080-b0fd582b-9d8d-4651-b576-1a9d6f87a484.png)

we established a benchmark framework for distortions evaluation using one of the most widespread databases for object detection (MS-COCO), even though restricted to a limited
set of seven natural distortions (see table I). In this way, we are laying the foundations for a future common evaluation method for evaluating object detection robustness. 

| | Noise| Contrast| Blur | Defocus  | Rain  | Local blur | Backlight illumination   | 
| ------ | ------ | ------ | ------ |  ------ | ------ | ------ | ------ | 
| Images | 44 | 42 | 32  | 201 | 21 | 127 |  128 | 
| Objects | 289 | 312 | 224  | 1299 | 110 | 464 |  934 | 
| Ratio | 1.0| 0.83 | 0.97  | 0.72 | 0.95 | 0.34 | 0.68 | 
Ratio: Number of retained objects/Number of annotated objects present in images.
Furthermore, this framework is an in-dept study with a wide scope that informs about the ability to detect distorted objects and the detection accuracy according to common metrics:

    mIoU metric : 
![image](https://user-images.githubusercontent.com/80038451/153515307-a4990af7-2350-44bb-89aa-912557968374.png)

    mAP metric :
![image](https://user-images.githubusercontent.com/80038451/153515751-639ea60a-5eaf-48b2-963f-7b061ee55b37.png)

Image Distortions
-----------------------------------

- Global distortions: affect the image as a whole and come from different sources related in general to the acquisition conditions. Some are directly dependent on the physical characteristics of the camera and are of photometric or geometric origin. Among the most common distortions that affect the quality of the signal are defocusing blur, photon noise, geometric or chromatic aberrations, and blur due to the movement of the camera or the movement of objects. The other types of degradation are related to the environment and more particularly the lighting and atmospheric disturbances in the case of outdoor scenes. Compression and image transmission artifacts are another source of degradation that is difficult to control. These common distortions have been already considered in benchmarking the performance of some models.
- Local distortions: are undesirable signals affecting one or more localized areas in the image (see figure 1). A typical case is the blurring due to the movement of an object of relatively high speed. Another photometric distortion is the appearance of a halo around the object contours due to the limited sensitivity of the sensors or backlight illumination (BI). The artistic blur affecting a particular part of the targeted scene, the object to be highlighted by the pro-shooter, is another type of local distortion. Thus, integrating the local distortions in the database increases its size and makes it richer and more representative of scenarios close to real applications which improves the relevance of trained models.



