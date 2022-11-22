Modified according to https://github.com/calmisential/TensorFlow2.0_ResNet

## Train

Requirements:
+ Python >= 3.6
+ Tensorflow == 2.0.0

1. Download the VOC2012 dataset
```
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
tar xvf ./VOCtrainval_11-May-2012.tar
./VOC2012_resplit.py # invalid behavior, simply to run this repo
```

2. The VOC2012 dataset will be put under the folder **original dataset**, and the directory would look like this:
```
|——original dataset
   |——class_name_0
   |——class_name_1
   |——class_name_2
   |——class_name_3
```
3. Run the script **split_dataset.py** to split the raw dataset into train set, valid set and test set.
4. Change the corresponding parameters in **config.py**.
5. Run **train.py** to start training.
5. Run **evaluate.py** to start training.
