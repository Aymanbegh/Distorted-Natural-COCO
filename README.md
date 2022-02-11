# Object-Detection-under-Local-Distortions-

This repository provides an additional new benchmark dataset constructed for natural in-capture distortions from MS-COCO dataset to better assess the reliability
of the object detection models in case of real distortions. It serves as a complement to the study: conducted on the robustness to distortions of object detection models. It allows to evaluate the efficiency of the data augmentation through the generation of synthetic distorted images on the robustness of models in real images case.

Requirements
-----------------------------------

    MS-COCO 2017 dataset (validation set)
    Python 3.8 (Tested on it)
    Requirements of the object detection model to evaluate

Overview
-----------------------------------

In the existing methods, robustness evaluations of object detection algorithms were performed on synthetic distortions or specific datasets which limits the extension of those studies in real-world applications.
Therefore, we have done this manual identification of the natural distortions present in the MS-COCO validation set to better assess the robustness in real scenarios. 
It is worth noticing that the selected sub-sets from MS-COCO contain images with global distortions and the associated object annotations. Whereas,
in the case of local distortions, only affected objects are considered as in the following figure:

![image](https://user-images.githubusercontent.com/80038451/153636927-c59befa1-c96a-42a3-9e88-f3a4490e011b.png)

We established this benchmark framework for distortions evaluation using one of the most widespread databases for object detection (MS-COCO), even though restricted to a limited
set of seven natural distortions (see table below). In this way, we are laying the foundations for a future common evaluation method for evaluating object detection robustness. 

| | Noise| Contrast| Blur | Defocus  | Rain  | Local blur | Backlight illumination   | 
| ------ | ------ | ------ | ------ |  ------ | ------ | ------ | ------ | 
| Images | 44 | 42 | 32  | 201 | 21 | 127 |  128 | 
| Objects | 289 | 312 | 224  | 1299 | 110 | 464 |  934 | 
| Ratio | 1.0| 0.83 | 0.97  | 0.72 | 0.95 | 0.34 | 0.68 | 

Ratio: Number of retained objects/Number of annotated objects present in images.


Project tree structure
-----------------------------------

Create a data folder under the repository,

    cd {repo_root}
    mkdir natural_val2017
    
Then copy our depository inside.
    
- **MS-COCO natural distortion**: structure of each one of the 7 natural distortion folders withimage list, images and annotations
    ```
  *Distortion_name*
  ├── annotations
      └──instances_*distortion_name*.json
  │── images
      └── ****.jpg
  ├── list.txt
  ```
 
- **List.txt**: lists locations and names of each images
    ```
    Exemple:
    .\Backlight illumination\images\000000001268.jpg
    add your path directory:
    C:\Users\beghd\OneDrive\Bureau\natural_val2017\Backlight illumination\images\000000001268.jpg
    ```
    
 - **Natural COCO evaluation**: functions in python to evaluate the model performance
      ```
    ├── coco_eval: main function to launch the evaluation process
    ├── coco: extract inforamtion and annotations from the detected and ground truth JSON files (in folder "annotation": see **MS-COCO natural distortion** for the ground truth)
    ├── COCOevals: Compute the mIoU and AP scores for the selected distortion set
    ├── mask: function from the original "pycocotools" library 
      ```


How to launch the evaluation
-----------------------------------
**Required files**
- The ground truth json file (gt) corresponding to the desired natural distortion
- The detection json file (dt) corresponding to the result of the model detection on distorted set (bounding boxes and categories detected per images)

**Get results of the model detection on distorted set**
- Copy the corresponding list file in the model directory or the instance json file (by exemple: instances_noise.json to test the model on the noise distortion)
- Launch the test and get back the result path (dt_path/*name_results*.json)

**Launch the coco evaluation process**
- Go to the directory containing the coco_eval function:

        cd ~/natural_val2017
        
- Then call the main function:

        python coco_eval.py /gt_path/instances_*distortion_name*.json dt /dt_path/*name_results*.json bbox
        
"bbox" indicates the evaluation type, in the case of the noise evaluation, the calling function is:

        python coco_eval.py ./Noise/instances_noise.json /path_to_the_model_directory/results/coco_results.json bbox
        
or to get the results into a txt file:

        python coco_eval.py ./Noise/instances_noise.json /path_to_the_model_directory/results/coco_results.json bbox > *result_name*.txt
        

Experiments
-----------------------------------
We evaluated the YOLOv4-tiny pre-trained model (from: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights) by using NVIDIA RTX 2080Ti.
The YOLOv4 directory is as following:

            ```
        darknet
        ├── cfg
            └──includes the models configurations
        │── data
            └── includes the coco configuration and the images path (list.txt file)
                └── coco.names: names of coco's categories
                └── coco.data: include path to usefull directories   
                └── list.txt
        │── results
            └── includes result from the model test validation    
            ```
  
In our case, the coco.data file in the data directory is:

    classes= 80
    train =  ./*file_name_with_image_paths_for_training*.txt
    valid = ./list.txt
    names = ./coco.names
    backup = /path_to_darknet/backup/
    eval=coco

Below is mAP (mean average precision) with IoU=[0.50:0.95] (AP COCO metric) and mIoU (mean Intersection over Union) for our naturally distorted COCO val2017 sets:

| Metric | Noise| Contrast| Blur | Defocus  | Rain  | Local blur | Backlight illumination   |  MS-COCO validation set   | 
| ------ | ------ | ------ | ------ |  ------ | ------ | ------ | ------ | ------ | 
| AP | 0.298 | 0.186 | 0.215 | 0.137 | 0.270 | 0.183 | 0.131 | 0.221  | 
| mIoU | 0.773 | 0.744 | 0.760  | 0.746 | 0.762 | 0.755 | 0.749 | 0.758 | 

Here, MS-COCO validation set is the original validation set from COCO 2017 that contains 5K images.
Then, results for the model YOLOv4-tiny trained on the train2017 set from the MS-COCO dataset and trained on this train2017 set distorted (See repository:  ):
- Trained on MS-COCO train set (118k images)
- Trained on MS-COCO train set distorted (118k images): 5% of the contained images for each of the 10 distortion types




Metrics
-----------------------------------

Furthermore, this framework is an in-dept study with a wide scope that informs about the ability to detect distorted objects and the detection accuracy according to common metrics:

- mIoU metric : 

![image](https://user-images.githubusercontent.com/80038451/153515307-a4990af7-2350-44bb-89aa-912557968374.png)

- mAP metric :
![image](https://user-images.githubusercontent.com/80038451/153515751-639ea60a-5eaf-48b2-963f-7b061ee55b37.png)


Citation
-----------------------------------

Use this BibTeX to cite this repository:



Use this BibTeX to cite the corresponding paper:




