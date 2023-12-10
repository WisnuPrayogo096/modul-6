# Rock Paper Scissors Prediction

## Overview

Project ini adalah untuk tugas pratikum mata kuliah Machine Learning Fakultas Teknik Informatika UMM
**_Link Dataset yang digunakan :_** [rps dataset](https://drive.google.com/drive/folders/1kgyN9Ah_w6MvxsRxANh3TfB9S-bCVZMv).

Preprocessing yang digunakan : Konversi mode warna, Pengubahan ukuran, Konversi ke array, Ekspansi dimensi, Normalisasi

Model yang digunakan : Deep Learning Method Convolutional Neural Network dengan arsitektur seperti gambar di bawah ini
![image](assets/cnn.png)

Selain itu, menambahkan dengan method pre-train yaitu MobileNetV2 dan ResNet50

MobileNetV2

![image](assets/mobilenetv2.png)

ResNet50

![image](assets/resnet.png)

**Akurasi** yang didapatkan dengan menggunakan model CNN adalah : **97.22%**

Sedangkan dengan tambahan method pre-trained yaitu model MobileNetV2 dan Resnet50 adalah : **92.85%** dan **90.47%**

## Overview Dataset

**_Link Dataset yang digunakan :_** [rps dataset](https://drive.google.com/drive/folders/1kgyN9Ah_w6MvxsRxANh3TfB9S-bCVZMv).
Gambar yang digunakan adalah Rock, Paper dan Scissors dengan total gambar 2.520 gambar. Terdiri dari 840 gambar jenis Rock, 840 gambar jenis Paper dan 840 gambar jenis Scissors

Splitting Dataset : Training = 70%, Validation = 20%, Testing = 10%.

## Preprocessing dan Modelling

- **Preprocessing Model** : resize(150,150), rescale=1./255, rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest'
- Modelling Model CNN :

  Summary Model CNN :

  ![image](assets/summary_cnn.png)

  Graph Loss dan Accuracy Model CNN :

  ![image](assets/graph_acc_cnn.png)
  ![image](assets/graph_loss_cnn.png)

  Evaluation Matrix Model CNN :

  ![image](assets/eva_cnn.png)

  - Modelling Model MobileNetV2 :

  Summary Model MobileNetV2 :

  ![image](assets/summary_mobilenetv2.png)

  Graph Loss dan Accuracy MobileNetV2 :

  ![image](assets/graph_acc_net.png)
  ![image](assets/graph_loss_net.png)

  Evaluation Matrix Model MobileNetV2 :

  ![image](assets/eva_net.png)

  - Modelling Model ResNet50 :

  Summary Model ResNet50 :

  ![image](assets/summary_resnet50.png)

  Graph Loss dan Accuracy ResNet50 :

  ![image](assets/graph_acc_resnet.png)
  ![image](assets/graph_loss_resnet.png)

  Evaluation Matrix Model ResNet50 :

  ![image](assets/eva_resnet.png)

  ## Predict Data

- Predict Data dengan Model CNN :

1. ![image](assets/predict_cnn.png)

2. ![image](assets/predict_cnn_2.png)

3. ![image](assets/predict_cnn_3.png)

- Predict Data dengan Model MobileNetV2 :

1. ![image](assets/predict_net.png)

2. ![image](assets/predict_net_2.png)

3. ![image](assets/predict_net_3.png)

- Predict Data dengan Model ResNet50 :

1. ![image](assets/predict_resnet.png)

2. ![image](assets/predict_resnet_2.png)

3. ![image](assets/predict_resnet_3.png)

## Local Development

![image](assets/page_1.png)

![image](assets/page_2.png)
