# Dataset Edelweis

<br>Tautan *dataset train*: [Data Edelweis Compressed 512/Train](https://drive.google.com/drive/folders/1W-SIS1jtiblMngLa8Te138jpf4oGLWOD?usp=drive_link)
<br>Tautan *dataset test*: [Data Edelweis Compressed 512/Test](https://drive.google.com/drive/folders/1tuaD-lj31lQcFDf8eOq5MR3zEK2nb3ZD?usp=drive_link)

<br>Sumber *dataset*: [Edelweis Flower Dataset(Malau, 2022)](https://www.kaggle.com/datasets/ndomalau/edelweis-flower)
<br>Pra-pemrosesan gambar:
1. Pengurangan dimensi dan penurunan kualitas menjadi 85% menggunakan *library* PIL
2. Normalisasi dengan membagi nilai piksel dengan 255 dan *split dataset train* menjadi *dataset train* dan *validation* dengan perbandingan train:validation = 80:20 menggunakan [ImageDataGenerator](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator)
3. Seragamkan ukuran menjadi (256,256) dan buat mini-batch dengan batch size 32 menggunakan [flow_from_directory](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator#flow_from_directory)



































